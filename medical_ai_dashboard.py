# -*- coding: utf-8 -*-
"""
🏥 Medical AI Dashboard - local launcher entrypoint
"""

from datetime import datetime
import os
from pathlib import Path


def print_header() -> None:
    print("\n" + "=" * 70)
    print("🏥 MEDICAL AI DASHBOARD")
    print("🕒 " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("=" * 70)


def print_status() -> None:
    env_root = os.environ.get("MORANS_PROJECT_ROOT")
    root = Path(env_root).expanduser().resolve() if env_root else Path(__file__).resolve().parent
    big_clock_exists = (root / "big_clock.py").exists()
    time_tracker_exists = (root / "time_tracker.py").exists()
    ios_exists = (root / "MedicalAI-iOS" / "MedicalAIApp.swift").exists()

    def mark(value: bool) -> str:
        return "✅" if value else "❌"

    print("\nמצב גרסה נוכחית:")
    print(f"• {mark(big_clock_exists)} Big Clock זמין")
    print(f"• {mark(time_tracker_exists)} Time Tracker זמין")
    print(f"• {mark(ios_exists)} iOS SwiftUI source קיים")
    if ios_exists:
        print("• ℹ️ להרצת iOS צריך Xcode במחשב שלך")


def print_icon_help() -> None:
    print("\nהאייקון ללחיצה במחשב:")
    print("• launch.command")
    print("• לרוב יופיע עם אייקון של Terminal")


def main() -> None:
    print_header()
    print_status()
    print_icon_help()
    print("\nהבדיקה הושלמה.")


if __name__ == "__main__":
    main()
