#!/usr/bin/env python3
"""
ESP32 Build and Deploy Script - CPP_to_ESP32 v1.0.0
Compiles the C++ code and flashes it to ESP32 on COM5

Project: https://github.com/Early-Alpha-Engineering/CPP_to_ESP32
Author: Early Alpha Engineering
License: MIT
"""

import subprocess
import sys
import os

VERSION = "1.0.0"
ESP_IDF_PATH = r"C:\Espressif\frameworks\esp-idf-v5.4.1"
ESP_PYTHON = r"C:\Users\Eaea\.espressif\python_env\idf5.4_py3.12_env\Scripts\python.exe"
IDF_PY = os.path.join(ESP_IDF_PATH, "tools", "idf.py")
COM_PORT = "COM5"

def run_command(cmd, description):
    """Run a command and handle errors"""
    print(f"🔧 {description}...")
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} successful!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed!")
        print(f"Error: {e.stderr}")
        return False

def build_project():
    """Build the ESP32 project"""
    # Set environment variables
    env = os.environ.copy()
    env['IDF_PATH'] = ESP_IDF_PATH
    env['IDF_PYTHON_ENV_PATH'] = os.path.dirname(os.path.dirname(ESP_PYTHON))
    env['IDF_TARGET'] = 'esp32'
    
    # Add ESP-IDF tools to PATH (includes cmake and ninja)
    esp_tools_path = os.path.join(ESP_IDF_PATH, "tools")
    cmake_path = r"C:\Espressif\tools\cmake\3.30.2\bin"
    ninja_path = r"C:\Espressif\tools\ninja\1.12.1"
    toolchain_path = r"C:\Espressif\tools\xtensa-esp-elf\esp-14.2.0_20241119\xtensa-esp-elf\bin"
    env['PATH'] = f"{os.path.dirname(ESP_PYTHON)};{cmake_path};{ninja_path};{toolchain_path};{esp_tools_path};{env.get('PATH', '')}"
    
    # Build command using the full Python path
    build_cmd = f'"{ESP_PYTHON}" "{IDF_PY}" build'
    
    print("🏗️  Building ESP32 project...")
    print(f"Command: {build_cmd}")
    try:
        result = subprocess.run(build_cmd, shell=True, check=True, env=env, cwd=os.getcwd())
        print("✅ Build successful!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Build failed with exit code: {e.returncode}")
        return False

def flash_project():
    """Flash the project to ESP32"""
    env = os.environ.copy()
    env['IDF_PATH'] = ESP_IDF_PATH
    env['IDF_PYTHON_ENV_PATH'] = os.path.dirname(os.path.dirname(ESP_PYTHON))
    env['IDF_TARGET'] = 'esp32'
    
    # Add ESP-IDF tools to PATH (includes cmake and ninja)
    esp_tools_path = os.path.join(ESP_IDF_PATH, "tools")
    cmake_path = r"C:\Espressif\tools\cmake\3.30.2\bin"
    ninja_path = r"C:\Espressif\tools\ninja\1.12.1"
    toolchain_path = r"C:\Espressif\tools\xtensa-esp-elf\esp-14.2.0_20241119\xtensa-esp-elf\bin"
    env['PATH'] = f"{os.path.dirname(ESP_PYTHON)};{cmake_path};{ninja_path};{toolchain_path};{esp_tools_path};{env.get('PATH', '')}"
    
    flash_cmd = f'"{ESP_PYTHON}" "{IDF_PY}" -p {COM_PORT} flash'
    
    print(f"📱 Flashing to {COM_PORT}...")
    try:
        result = subprocess.run(flash_cmd, shell=True, check=True,
                              capture_output=True, text=True, env=env, cwd=os.getcwd())
        print("✅ Flash successful!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Flash failed: {e.stderr}")
        print(f"Output: {e.stdout}")
        return False

def check_connection():
    """Check if ESP32 is connected"""
    cmd = f'python -m esptool --port {COM_PORT} chip_id'
    return run_command(cmd, "Checking ESP32 connection")

def main():
    print("🚀 ESP32 Build and Deploy Script")
    print("=" * 40)
    
    # Check connection first
    if not check_connection():
        print(f"❌ Cannot connect to ESP32 on {COM_PORT}")
        sys.exit(1)
    
    # Build project
    if not build_project():
        print("❌ Build failed. Please check your code.")
        sys.exit(1)
    
    # Flash project  
    if not flash_project():
        print("❌ Flash failed. Please check connection.")
        sys.exit(1)
    
    print("\n🎉 SUCCESS! ESP32 programmed successfully!")
    print(f"💡 Run 'python monitor.py' to see the output")

if __name__ == "__main__":
    main() 