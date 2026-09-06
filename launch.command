#!/bin/bash

# 🏥 Medical AI Dashboard Launcher
# לחץ על הקובץ הזה כדי להתחיל את האפליקציה

cd "$(dirname "$0")"
export MORANS_PROJECT_ROOT="$(pwd)"
python3 "$MORANS_PROJECT_ROOT/medical_ai_dashboard.py"
