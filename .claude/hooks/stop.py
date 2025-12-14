#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///

import argparse
import json
import os
import sys
import random
import subprocess
from pathlib import Path
from datetime import datetime


def _log_error(error_message):
    """Log errors to .claude/hooks/errors.log with timestamp"""
    try:
        log_file = Path(__file__).parent / "errors.log"
        timestamp = datetime.now().isoformat()
        with open(log_file, 'a') as f:
            f.write(f"[{timestamp}] stop.py: {error_message}\n")
    except Exception:
        pass  # Don't fail if logging fails


def get_completion_messages():
    """Return list of friendly completion messages."""
    return [
        "Work complete!",
        "All done!",
        "Task finished!",
        "Job complete!",
        "Ready for next task!"
    ]


def generate_completion_summary(transcript_path):
    """
    Generate an AI summary of what was accomplished in the conversation.

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


def announce_completion(summary_message=None):
    """
    Announce completion using offline TTS.

    Args:
        summary_message: Optional AI-generated summary to speak.
                        If None, uses random predefined messages.
    """
    try:
        # Get pyttsx3 TTS script path (offline only)
        script_dir = Path(__file__).parent
        tts_script = script_dir / "utils" / "tts" / "pyttsx3_tts.py"

        if not tts_script.exists():
            _log_error("No TTS script found")
            return  # No TTS script available

        # Use provided summary or fall back to random message
        if summary_message:
            completion_message = summary_message
        else:
            completion_message = random.choice(get_completion_messages())

        # Log that we're about to speak
        _log_error(f"[DEBUG] About to speak: {completion_message}")

        # Call the TTS script with the completion message (blocking to ensure it completes)
        result = subprocess.run([
            "uv", "run", "--no-sync", "--offline", "python", str(tts_script), completion_message
        ],
        capture_output=True,
        text=True,
        timeout=20,  # 20 second timeout
        check=False  # Don't raise exception on non-zero exit
        )

        # Log the result
        _log_error(f"[DEBUG] TTS subprocess completed with return code: {result.returncode}")
        if result.stdout:
            _log_error(f"[DEBUG] TTS stdout: {result.stdout}")
        if result.stderr:
            _log_error(f"[DEBUG] TTS stderr: {result.stderr}")

    except subprocess.TimeoutExpired as e:
        _log_error(f"TTS timeout after 20 seconds: {e}")
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
        parser.add_argument('--summary', action='store_true', help='Generate AI summary of conversation')
        args = parser.parse_args()

        # Read JSON input from stdin
        input_data = json.load(sys.stdin)

        # Extract required fields
        session_id = input_data.get("session_id", "")
        stop_hook_active = input_data.get("stop_hook_active", False)
        transcript_path = input_data.get("transcript_path", "")

        # Ensure log directory exists
        log_dir = os.path.join(Path(__file__).parent.parent, "logs")
        os.makedirs(log_dir, exist_ok=True)
        log_path = os.path.join(log_dir, "stop.json")

        # Handle --chat switch
        if args.chat and transcript_path:
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

        # Unified synchronous flag-based logic
        if args.summary and transcript_path:
            # Generate summary synchronously
            summary = generate_completion_summary(transcript_path)

            if summary:
                # Add summary to input_data for logging
                input_data["generated_summary"] = summary

                # Decide whether to speak based on flags
                if args.notify and args.summary:
                    # Case 3: Both flags - generate summary and speak it
                    announce_completion(summary)
                # Case 2: Summary only - do nothing (already logged)

        elif args.notify:
            # Case 1: Notify only - speak random message without summary
            announce_completion(None)  # Will use random message

        # Log the data (with or without summary)
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

        sys.exit(0)

    except json.JSONDecodeError:
        # Handle JSON decode errors gracefully
        sys.exit(0)
    except Exception:
        # Handle any other errors gracefully
        sys.exit(0)


if __name__ == "__main__":
    main()
