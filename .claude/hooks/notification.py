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
import random
from pathlib import Path
from datetime import datetime


def _log_error(error_message):
    """Log errors to .claude/hooks/errors.log with timestamp"""
    try:
        log_file = Path(__file__).parent / "errors.log"
        timestamp = datetime.now().isoformat()
        with open(log_file, 'a') as f:
            f.write(f"[{timestamp}] notification.py: {error_message}\n")
    except Exception:
        pass  # Don't fail if logging fails


def get_tts_script_path():
    """
    Determine which TTS script to use based on available API keys.
    Priority order: ElevenLabs > OpenAI > pyttsx3
    """
    # Get current script directory and construct utils/tts path
    script_dir = Path(__file__).parent
    tts_dir = script_dir / "utils" / "tts"
    pyttsx3_script = tts_dir / "pyttsx3_tts.py"
    if pyttsx3_script.exists():
        return str(pyttsx3_script)

    return None


def generate_waiting_summary(transcript_path):
    """
    Generate an AI summary of what input Claude is waiting for.

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

        return summarize_conversation(transcript_path, "waiting")
    except Exception as e:
        # Log error for debugging
        import sys
        print(f"Error generating waiting summary: {e}", file=sys.stderr)
        return None


def announce_notification(notification_message=None):
    """
    Announce that the agent needs user input.

    Args:
        notification_message: Optional AI-generated summary of what input is needed.
                             If None, uses generic notification message.
    """
    try:
        tts_script = get_tts_script_path()
        if not tts_script:
            _log_error("No TTS script found")
            return  # No TTS scripts available

        # Use provided summary or fall back to generic message
        if notification_message:
            message = notification_message
        else:
            # Hardcoded engineer name
            engineer_name = 'Omer'

            # Create notification message with 30% chance to include name
            if engineer_name and random.random() < 0.3:
                message = f"{engineer_name}, your agent needs your input"
            else:
                message = "Your agent needs your input"

        # Log that we're about to speak
        _log_error(f"[DEBUG] About to speak: {message}")

        # Call the TTS script with the notification message (blocking to ensure it completes)
        result = subprocess.run([
            "uv", "run", "--no-sync", "--offline", "python", tts_script, message
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
        parser.add_argument('--notify', action='store_true', help='Enable TTS notifications')
        parser.add_argument('--summary', action='store_true', help='Generate AI summary of what input is needed')
        args = parser.parse_args()

        # Read JSON input from stdin
        input_data = json.loads(sys.stdin.read())

        # Extract transcript path
        transcript_path = input_data.get("transcript_path", "")

        # Ensure log directory exists
        import os
        log_dir = os.path.join(Path(__file__).parent.parent, 'logs')
        os.makedirs(log_dir, exist_ok=True)
        log_file = os.path.join(log_dir, 'notification.json')

        # Unified synchronous flag-based logic
        if args.summary and transcript_path:
            # Generate summary synchronously
            summary = generate_waiting_summary(transcript_path)

            if summary:
                # Add summary to input_data for logging
                input_data["generated_summary"] = summary

                # Decide whether to speak based on flags
                if args.notify and args.summary:
                    # Case 3: Both flags - generate summary and speak it
                    announce_notification(summary)
                # Case 2: Summary only - do nothing (already logged)

        elif args.notify:
            # Case 1: Notify only - speak random/generic message without summary
            announce_notification(None)  # Will use random/generic message

        # Log the data (with or without summary)
        if os.path.exists(log_file):
            with open(log_file, 'r') as f:
                try:
                    log_data = json.load(f)
                except (json.JSONDecodeError, ValueError):
                    log_data = []
        else:
            log_data = []

        # Append new data
        log_data.append(input_data)

        # Write back to file with formatting
        with open(log_file, 'w') as f:
            json.dump(log_data, f, indent=2)

        sys.exit(0)

    except json.JSONDecodeError:
        # Handle JSON decode errors gracefully
        sys.exit(0)
    except Exception:
        # Handle any other errors gracefully
        sys.exit(0)


if __name__ == '__main__':
    main()
