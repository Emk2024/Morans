# -*- coding: utf-8 -*-
"""
⏱️ מעקב זמן לכל פעולה
Time tracker for all operations
"""

import time
import sys
from datetime import datetime, timedelta
from typing import Callable, Any, Dict
import threading

class OperationTimer:
    """מעקב זמן עם שעון ספירה לאחור"""
    
    # הערכות זמן לפעולות שונות (בשניות)
    TIME_ESTIMATES = {
        "load_dashboard": 3,
        "load_medications": 2,
        "load_alerts": 2,
        "analyze_image": 5,
        "send_report": 8,
        "search_research": 6,
        "search_doctors": 4,
        "load_profile": 2,
        "save_data": 1,
        "generate_report": 10,
        "check_interactions": 3,
        "upload_image": 2,
        "send_email": 4,
        "search_pubmed": 7,
        "parse_json": 1,
    }
    
    def __init__(self, operation_name: str, estimated_seconds: int = None):
        self.operation_name = operation_name
        self.estimated_seconds = estimated_seconds or self.TIME_ESTIMATES.get(operation_name, 3)
        self.start_time = None
        self.end_time = None
        self.is_running = False
        
    def __enter__(self):
        """התחל את שעון המעקב"""
        self.start_time = time.time()
        self.is_running = True
        self.show_header()
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        """סיים את שעון המעקב"""
        self.end_time = time.time()
        self.is_running = False
        self.show_footer()
        
    def show_header(self):
        """הצג כותרת עם הערכת זמן"""
        print("\n" + "=" * 80)
        print(f"⏱️  {self.operation_name.upper()}")
        print(f"⏳ הערכת זמן: ~{self.estimated_seconds} שניות")
        print("=" * 80)
        print()
        
        # התחל שעון ספירה לאחור
        self.show_countdown()
        
    def show_footer(self):
        """הצג סיכום זמן בסוף"""
        elapsed = self.end_time - self.start_time
        status = "✅ הסתיים בהצלחה" if elapsed < self.estimated_seconds * 1.5 else "⚠️ לקח יותר מהצפוי"
        
        print("\n" + "=" * 80)
        print(f"{status}")
        print(f"⏱️  זמן בפועל: {elapsed:.1f} שניות")
        print(f"⏳ הערכה: {self.estimated_seconds} שניות")
        if elapsed > self.estimated_seconds:
            extra = elapsed - self.estimated_seconds
            print(f"⚠️  יותר ממוצפה ב: +{extra:.1f} שניות")
        else:
            saved = self.estimated_seconds - elapsed
            print(f"✨ מהר יותר ב: -{saved:.1f} שניות")
        print("=" * 80 + "\n")
    
    def show_countdown(self):
        """הצג שעון ספירה לאחור (בברקגראונד)"""
        def countdown():
            for i in range(self.estimated_seconds, 0, -1):
                if not self.is_running:
                    break
                remaining_text = f"⏳ נותר: {i} שניות"
                sys.stdout.write(f"\r{remaining_text}")
                sys.stdout.flush()
                time.sleep(1)
            if self.is_running:
                sys.stdout.write("\r✅ סיים!           \n")
                sys.stdout.flush()
        
        thread = threading.Thread(target=countdown, daemon=True)
        thread.start()
    
    def get_elapsed_time(self):
        """קבל זמן שחלף עד כה"""
        if self.start_time:
            return time.time() - self.start_time
        return 0
    
    def get_remaining_time(self):
        """קבל זמן שנותר בהערכה"""
        elapsed = self.get_elapsed_time()
        remaining = max(0, self.estimated_seconds - elapsed)
        return remaining


class ProgressBar:
    """שורת התקדמות עם זמן"""
    
    def __init__(self, total: int, operation: str = "עבודה"):
        self.total = total
        self.current = 0
        self.operation = operation
        self.start_time = time.time()
        
    def update(self, amount: int = 1):
        """עדכן התקדמות"""
        self.current += amount
        self.show()
        
    def show(self):
        """הצג את שורת ההתקדמות"""
        elapsed = time.time() - self.start_time
        progress = self.current / self.total
        
        # חשב זמן שנותר
        if progress > 0:
            total_time = elapsed / progress
            remaining = total_time - elapsed
        else:
            remaining = 0
        
        # צייר את השורה
        bar_length = 40
        filled = int(bar_length * progress)
        bar = "█" * filled + "░" * (bar_length - filled)
        
        percentage = int(progress * 100)
        
        print(f"\r{self.operation}: [{bar}] {percentage}% | ⏱️  {elapsed:.0f}s | ⏳ {remaining:.0f}s", end="")
        
        if self.current == self.total:
            print()  # ירידת שורה בסוף


def timed_operation(operation_name: str, estimated_seconds: int = None):
    """דקורטור להוספת מעקב זמן לפונקציה"""
    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs) -> Any:
            with OperationTimer(operation_name, estimated_seconds) as timer:
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


# דוגמאות שימוש
if __name__ == "__main__":
    print("\n🏥 דוגמה 1: מעקב זמן לפעולה\n")
    
    with OperationTimer("load_medications", 5):
        time.sleep(3)
        print("🔄 טוען תרופות...")
    
    print("\n🏥 דוגמה 2: שורת התקדמות\n")
    
    bar = ProgressBar(100, "ניתוח בדיקה")
    for i in range(100):
        bar.update(1)
        time.sleep(0.05)
    
    print("\n✅ סיים!\n")
