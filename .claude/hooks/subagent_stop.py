#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///

import argparse
import json
import os
import sys
import subprocess
from pathlib import Path
from datetime import datetime


def _log_error(error_message):
    """Log errors to .claude/hooks/errors.log with timestamp"""
    try:
        log_file = Path(__file__).parent / "errors.log"
        timestamp = datetime.now().isoformat()
        with open(log_file, 'a') as f:
            f.write(f"[{timestamp}] subagent_stop.py: {error_message}\n")
    except Exception:
        pass  # Don't fail if logging fails


def get_tts_script_path():
    """Get offline TTS script path (pyttsx3 only)."""
    # Get current script directory and construct utils/tts path
    script_dir = Path(__file__).parent
    tts_dir = script_dir / "utils" / "tts"

    # Use pyttsx3 for offline TTS (no API key required)
    pyttsx3_script = tts_dir / "pyttsx3_tts.py"
    if pyttsx3_script.exists():
        return str(pyttsx3_script)

    return None


def generate_subagent_completion_summary(transcript_path):
    """
    Generate an AI summary of what the subagent accomplished.

    Args:
        transcript_path: Path to the .jsonl transcript file

    Returns:
        Summary string, or None if error
    """
    try:
        # Handle import for script execution context
        try:
            from .utils.llm.conversation_summarizer import summarize_conversation
        except ImportError:
            # Running as script, use absolute import
            import sys
            from pathlib import Path
            script_dir = Path(__file__).parent
            sys.path.insert(0, str(script_dir))
            from utils.llm.conversation_summarizer import summarize_conversation

        return summarize_conversation(transcript_path, "completion")
    except Exception as e:
        # Log error for debugging
        import sys
        print(f"Error generating summary: {e}", file=sys.stderr)
        return None


def announce_subagent_completion(summary_message=None):
    """
    Announce subagent completion using offline TTS.

    Args:
        summary_message: Optional AI-generated summary to speak.
                        If None, uses fixed "Subagent Complete" message.
    """
    try:
        tts_script = get_tts_script_path()
        if not tts_script:
            _log_error("No TTS script found")
            return  # No TTS scripts available

        # Use provided summary or fall back to fixed message
        if summary_message:
            completion_message = summary_message
        else:
            completion_message = "Subagent Complete"

        # Call the TTS script with the completion message
        subprocess.run([
            "uv", "run", tts_script, completion_message
        ],
        capture_output=True,  # Suppress output
        timeout=10  # 10-second timeout
        )

    except subprocess.TimeoutExpired as e:
        _log_error(f"TTS timeout after 10 seconds: {e}")
    except (subprocess.SubprocessError, FileNotFoundError) as e:
        _log_error(f"TTS subprocess error: {e}")
    except Exception as e:
        _log_error(f"Unexpected TTS error: {e}")


def main():
    try:
        # Parse command line arguments
        parser = argparse.ArgumentParser()
        parser.add_argument('--chat', action='store_true', help='Copy transcript to chat.json')
        parser.add_argument('--notify', action='store_true', help='Enable TTS completion announcement')
        parser.add_argument('--summary', action='store_true', help='Generate AI summary of subagent work')
        args = parser.parse_args()
        
        # Read JSON input from stdin
        input_data = json.load(sys.stdin)

        # Extract required fields
        session_id = input_data.get("session_id", "")
        stop_hook_active = input_data.get("stop_hook_active", False)
        transcript_path = input_data.get("transcript_path", "")

        # Generate subagent summary if --summary flag is set
        summary = None
        if args.summary and transcript_path:
            summary = generate_subagent_completion_summary(transcript_path)
            if summary:
                # Add summary to input_data for logging
                input_data["generated_summary"] = summary

        # Ensure log directory exists
        log_dir = os.path.join(Path(__file__).parent.parent, "logs")
        os.makedirs(log_dir, exist_ok=True)
        log_path = os.path.join(log_dir, "subagent_stop.json")

        # Read existing log data or initialize empty list
        if os.path.exists(log_path):
            with open(log_path, 'r') as f:
                try:
                    log_data = json.load(f)
                except (json.JSONDecodeError, ValueError):
                    log_data = []
        else:
            log_data = []
        
        # Append new data
        log_data.append(input_data)
        
        # Write back to file with formatting
        with open(log_path, 'w') as f:
            json.dump(log_data, f, indent=2)
        
        # Handle --chat switch (same as stop.py)
        if args.chat and 'transcript_path' in input_data:
            transcript_path = input_data['transcript_path']
            if os.path.exists(transcript_path):
                # Read .jsonl file and convert to JSON array
                chat_data = []
                try:
                    with open(transcript_path, 'r') as f:
                        for line in f:
                            line = line.strip()
                            if line:
                                try:
                                    chat_data.append(json.loads(line))
                                except json.JSONDecodeError:
                                    pass  # Skip invalid lines
                    
                    # Write to logs/chat.json
                    chat_file = os.path.join(log_dir, 'chat.json')
                    with open(chat_file, 'w') as f:
                        json.dump(chat_data, f, indent=2)
                except Exception:
                    pass  # Fail silently

        # Announce subagent completion via TTS (only if --notify flag is set)
        if args.notify:
            announce_subagent_completion(summary)

        sys.exit(0)

    except json.JSONDecodeError:
        # Handle JSON decode errors gracefully
        sys.exit(0)
    except Exception:
        # Handle any other errors gracefully
        sys.exit(0)


if __name__ == "__main__":
    main()