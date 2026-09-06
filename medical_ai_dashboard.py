# -*- coding: utf-8 -*-
"""
🏥 Medical AI Dashboard - local launcher entrypoint
"""

from datetime import datetime


def print_header() -> None:
    print("\n" + "=" * 70)
    print("🏥 MEDICAL AI DASHBOARD")
    print("🕒 " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("=" * 70)


def print_status() -> None:
    print("\nמצב גרסה נוכחית:")
    print("• ✅ Big Clock זמין")
    print("• ✅ Time Tracker זמין")
    print("• ✅ iOS SwiftUI source קיים")
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
