from __future__ import annotations

import os
import sys
from pathlib import Path
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://api-inference.huggingface.co/models/openai/whisper-large-v2"


def transcribe_audio(audio_path: Path, hf_api_token: str) -> str:
    """Send an audio file to Hugging Face Inference API and return the transcription."""
    if not audio_path.exists():
        raise FileNotFoundError(f"Audio file not found: {audio_path}")

    with audio_path.open("rb") as audio_file:
        audio_bytes = audio_file.read()

    headers = {
        "Authorization": f"Bearer {hf_api_token}",
        "Accept": "application/json",
    }

    response = requests.post(API_URL, headers=headers, data=audio_bytes)
    response.raise_for_status()

    payload: dict[str, Any] = response.json()
    if "error" in payload:
        raise RuntimeError(f"Whisper error: {payload['error']}")

    return payload.get("text", "")


def main() -> int:
    hf_api_token = os.getenv("HF_API_TOKEN")
    if not hf_api_token:
        print("ERROR: set HF_API_TOKEN in the environment before running this script.")
        return 1

    if len(sys.argv) != 2:
        print("Usage: python src/phase1/whisper_example.py path/to/audio.wav")
        return 1

    audio_path = Path(sys.argv[1])
    print(f"Transcribing {audio_path} with Hugging Face Whisper...")

    try:
        transcript = transcribe_audio(audio_path, hf_api_token)
        print("Transcript:")
        print(transcript)
        return 0
    except Exception as exc:
        print(f"Failed to transcribe audio: {exc}")
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
