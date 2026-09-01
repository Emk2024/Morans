# -*- coding: utf-8 -*-
"""
⏰ שעון גדול וברור עם ספירה לאחור
Large visual countdown timer with operation tracking
"""

import time
import sys
import os
from datetime import datetime, timedelta
import threading

class BigClock:
    """שעון גדול וברור"""
    
    # ספרות גדולות בצורת ASCII
    DIGITS = {
        '0': [
            "  ███████  ",
            " ██     ██ ",
            "██       ██",
            "██       ██",
            "██       ██",
            " ██     ██ ",
            "  ███████  "
        ],
        '1': [
            "     ██ ",
            "    ███ ",
            "      ██",
            "      ██",
            "      ██",
            "      ██",
            "   ██████"
        ],
        '2': [
            "  ███████  ",
            " ██     ██ ",
            "       ██  ",
            "  ███████  ",
            " ██        ",
            "██         ",
            " ██████████"
        ],
        '3': [
            "  ███████  ",
            " ██     ██ ",
            "       ██  ",
            "   ██████  ",
            "       ██  ",
            " ██     ██ ",
            "  ███████  "
        ],
        '4': [
            "██       ██",
            "██       ██",
            "██       ██",
            " ██████████",
            "       ██  ",
            "       ██  ",
            "       ██  "
        ],
        '5': [
            " ██████████",
            "██         ",
            "██ ███████ ",
            "       ██  ",
            "       ██  ",
            " ██     ██ ",
            "  ███████  "
        ],
        '6': [
            "  ███████  ",
            " ██     ██ ",
            "██         ",
            "██ ███████ ",
            "██       ██",
            " ██     ██ ",
            "  ███████  "
        ],
        '7': [
            " ██████████",
            "       ██  ",
            "      ██   ",
            "     ██    ",
            "    ██     ",
            "   ██      ",
            "  ██       "
        ],
        '8': [
            "  ███████  ",
            " ██     ██ ",
            "██       ██",
            "  ███████  ",
            "██       ██",
            " ██     ██ ",
            "  ███████  "
        ],
        '9': [
            "  ███████  ",
            " ██     ██ ",
            "██       ██",
            " ██████████",
            "       ██  ",
            " ██     ██ ",
            "  ███████  "
        ],
        ':': [
            "  ",
            "██",
            "██",
            "  ",
            "██",
            "██",
            "  "
        ]
    }
    
    def __init__(self, operation_name: str = "", estimated_seconds: int = 0):
        self.operation_name = operation_name
        self.estimated_seconds = estimated_seconds
        self.start_time = time.time()
        self.is_running = True
        
    def clear_screen(self):
        """נקה את המסך"""
        os.system('clear' if os.name == 'posix' else 'cls')
    
    def draw_digit_line(self, digit: str, line_num: int) -> str:
        """צייר שורה של ספרה"""
        if digit in self.DIGITS:
            return self.DIGITS[digit][line_num]
        return ""
    
    def draw_time(self, seconds_left: int):
        """צייר שעון גדול"""
        self.clear_screen()
        
        # כותרת
        print("\n")
        print("╔" + "═" * 70 + "╗")
        print("║" + f"🏥 {self.operation_name}".center(70) + "║")
        print("╚" + "═" * 70 + "╝")
        print("\n")
        
        # המר שניות לפורמט HH:MM:SS
        hours = seconds_left // 3600
        minutes = (seconds_left % 3600) // 60
        seconds = seconds_left % 60
        
        time_str = f"{minutes:02d}:{seconds:02d}"
        
        # צייר כל שורה של הספרות
        for line_num in range(7):
            line = ""
            for char in time_str:
                line += self.draw_digit_line(char, line_num) + "  "
            print(line)
        
        print("\n")
        
        # פרטים
        elapsed = time.time() - self.start_time
        progress = (elapsed / self.estimated_seconds * 100) if self.estimated_seconds > 0 else 0
        
        print("┌" + "─" * 70 + "┐")
        print(f"│ ⏱️  זמן שחלף: {elapsed:.1f}s | הערכה: {self.estimated_seconds}s | התקדמות: {progress:.0f}%".ljust(71) + "│")
        print("└" + "─" * 70 + "┘")
        
        # שורת התקדמות
        bar_length = 60
        filled = int(bar_length * (elapsed / self.estimated_seconds)) if self.estimated_seconds > 0 else 0
        bar = "█" * filled + "░" * (bar_length - filled)
        print(f"\n  [{bar}]\n")
        
        # הודעה
        if seconds_left <= 5 and seconds_left > 0:
            print("  ⏰ זמן מדוד! עוד כמה שניות...\n")
        elif seconds_left <= 0:
            print("  ✅ סיים! הפעולה הושלמה!\n")

    def show_countdown(self):
        """הצג ספירה לאחור"""
        while self.is_running and self.estimated_seconds > 0:
            elapsed = time.time() - self.start_time
            remaining = max(0, self.estimated_seconds - elapsed)
            
            self.draw_time(int(remaining))
            
            if remaining <= 0:
                self.is_running = False
                time.sleep(0.5)
                break
            
            time.sleep(0.1)
    
    def start(self):
        """התחל את הספירה"""
        self.show_countdown()


class SimpleTimer:
    """טיימר פשוט יותר ללא ASCII art"""
    
    def __init__(self, operation_name: str, estimated_seconds: int):
        self.operation_name = operation_name
        self.estimated_seconds = estimated_seconds
        self.start_time = time.time()
    
    def show(self):
        """הצג את הטיימר"""
        elapsed = time.time() - self.start_time
        remaining = max(0, self.estimated_seconds - elapsed)
        
        # כותרת
        print("\n" + "╔" + "═" * 60 + "╗")
        print("║" + f"⏰ {self.operation_name}".center(60) + "║")
        print("╚" + "═" * 60 + "╝\n")
        
        # הצג זמן בגודל גדול
        minutes = int(remaining) // 60
        seconds = int(remaining) % 60
        
        print(f"\n{'█' * 30}")
        print(f"  ⏳ זמן שנותר: {minutes:02d}:{seconds:02d}")
        print(f"{'█' * 30}\n")
        
        # התקדמות
        progress = (elapsed / self.estimated_seconds * 100) if self.estimated_seconds > 0 else 0
        bar_length = 40
        filled = int(bar_length * progress / 100)
        bar = "▰" * filled + "▱" * (bar_length - filled)
        
        print(f"  [{bar}] {progress:.0f}%\n")
        print(f"  ⏱️  זמן שחלף: {elapsed:.1f}s\n")


# דוגמאות שימוש
if __name__ == "__main__":
    import time
    
    # דוגמה 1: שעון גדול עם ספירה לאחור
    print("\n🏥 דוגמה 1: שעון גדול\n")
    
    clock = BigClock("טעינת תרופות 💊", 10)
    
    # הצג את השעון בחוט נפרד
    timer_thread = threading.Thread(target=clock.show_countdown)
    timer_thread.start()
    
    # בינתיים, עשה עבודה
    for i in range(10):
        time.sleep(1)
    
    clock.is_running = False
    timer_thread.join()
    
    print("\n✅ סיים!\n")
