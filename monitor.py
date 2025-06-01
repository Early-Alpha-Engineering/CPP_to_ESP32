#!/usr/bin/env python3
"""
ESP32 Serial Monitor - CPP_to_ESP32 v1.0.0
Real-time serial output monitoring for ESP32 development

Project: https://github.com/Early-Alpha-Engineering/CPP_to_ESP32  
Author: Early Alpha Engineering
License: MIT
"""

import serial
import time

VERSION = "1.0.0"

try:
    ser = serial.Serial('COM5', 115200, timeout=1)
    print("🔌 Connected to ESP32 on COM5")
    print("📡 Monitoring output (Press Ctrl+C to stop)...")
    print("-" * 50)
    
    while True:
        if ser.in_waiting:
            data = ser.readline().decode('utf-8', errors='ignore').strip()
            if data:
                print(f"📤 {data}")
        time.sleep(0.1)
        
except KeyboardInterrupt:
    print("\n⏹️  Monitoring stopped")
except Exception as e:
    print(f"❌ Error: {e}")
finally:
    if 'ser' in locals():
        ser.close() 