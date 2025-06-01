#!/usr/bin/env python3
"""
ESP32 Build and Deploy Script - CPP_to_ESP32 v1.1.0
Modern PlatformIO-based build and flash automation for ESP32

Project: https://github.com/Early-Alpha-Engineering/CPP_to_ESP32
Author: Early Alpha Engineering
License: MIT
"""

import subprocess
import sys
import os
import argparse

VERSION = "1.1.0"
COM_PORT = "COM5"

def run_command(cmd, description, show_output=False):
    """Run a command and handle errors"""
    print(f"🔧 {description}...")
    try:
        if show_output:
            # Show real-time output for build process
            result = subprocess.run(cmd, shell=True, check=True)
        else:
            # Capture output for simple commands
            result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} successful!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed!")
        if not show_output and hasattr(e, 'stderr') and e.stderr:
            print(f"Error: {e.stderr}")
        return False

def check_platformio():
    """Check if PlatformIO is installed"""
    try:
        result = subprocess.run("pio --version", shell=True, check=True, capture_output=True, text=True)
        print(f"✅ PlatformIO found: {result.stdout.strip()}")
        return True
    except subprocess.CalledProcessError:
        print("❌ PlatformIO not found!")
        print("💡 Install PlatformIO with: pip install platformio")
        return False

def check_connection():
    """Check if ESP32 is connected"""
    cmd = f'pio device list'
    print("🔍 Checking connected devices...")
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        if COM_PORT in result.stdout:
            print(f"✅ ESP32 found on {COM_PORT}")
            return True
        else:
            print(f"⚠️  {COM_PORT} not found in device list")
            print("📋 Available devices:")
            print(result.stdout)
            return True  # Continue anyway, user might know what they're doing
    except subprocess.CalledProcessError as e:
        print(f"❌ Device check failed: {e.stderr}")
        return False

def build_project():
    """Build the ESP32 project using PlatformIO"""
    cmd = "pio run"
    return run_command(cmd, "Building ESP32 project", show_output=True)

def upload_project():
    """Upload the project to ESP32 using PlatformIO"""
    cmd = f"pio run --target upload"
    return run_command(cmd, f"Uploading to ESP32 on {COM_PORT}", show_output=True)

def clean_project():
    """Clean build artifacts"""
    cmd = "pio run --target clean"
    return run_command(cmd, "Cleaning build files")

def monitor_serial():
    """Start serial monitor"""
    print(f"📡 Starting serial monitor on {COM_PORT}...")
    print("💡 Press Ctrl+C to stop monitoring")
    try:
        subprocess.run(f"pio device monitor --port {COM_PORT} --baud 115200", shell=True, check=True)
    except KeyboardInterrupt:
        print("\n📴 Serial monitoring stopped")
    except subprocess.CalledProcessError as e:
        print(f"❌ Serial monitor failed: {e}")

def main():
    global COM_PORT
    
    parser = argparse.ArgumentParser(description="ESP32 Build and Deploy Tool (PlatformIO)")
    parser.add_argument("--build-only", action="store_true", help="Only build, don't upload")
    parser.add_argument("--upload-only", action="store_true", help="Only upload, don't build")
    parser.add_argument("--monitor", action="store_true", help="Start serial monitor after upload")
    parser.add_argument("--clean", action="store_true", help="Clean build files before building")
    parser.add_argument("--port", default=COM_PORT, help=f"COM port (default: {COM_PORT})")
    parser.add_argument("--version", action="version", version=f"CPP_to_ESP32 Deploy Script v{VERSION}")
    
    args = parser.parse_args()
    
    # Update COM_PORT if specified
    COM_PORT = args.port
    
    print("🚀 ESP32 Build and Deploy Script (PlatformIO)")
    print("=" * 50)
    print(f"Version: {VERSION}")
    print(f"Target Port: {COM_PORT}")
    print()
    
    # Check PlatformIO installation
    if not check_platformio():
        sys.exit(1)
    
    # Clean if requested
    if args.clean:
        if not clean_project():
            print("❌ Clean failed. Continuing anyway...")
    
    # Build phase
    if not args.upload_only:
        if not build_project():
            print("❌ Build failed. Please check your code.")
            sys.exit(1)
    
    # Upload phase
    if not args.build_only:
        # Check connection before upload
        if not check_connection():
            print(f"⚠️  Warning: Could not verify ESP32 connection on {COM_PORT}")
            response = input("Continue anyway? (y/N): ")
            if response.lower() != 'y':
                sys.exit(1)
        
        if not upload_project():
            print("❌ Upload failed. Please check connection and try again.")
            sys.exit(1)
    
    # Success message
    if args.build_only:
        print("\n🎉 BUILD SUCCESS! Firmware ready for upload.")
        print(f"💡 Run 'pio run --target upload' to flash to ESP32")
    elif args.upload_only:
        print("\n🎉 UPLOAD SUCCESS! ESP32 programmed successfully!")
    else:
        print("\n🎉 BUILD & UPLOAD SUCCESS! ESP32 programmed successfully!")
    
    # Optional monitoring
    if args.monitor:
        print()
        monitor_serial()
    else:
        print(f"💡 Run 'pio device monitor --port {COM_PORT}' to see the output")
        print(f"💡 Or run 'python deploy.py --monitor' to build, upload, and monitor")

if __name__ == "__main__":
    main() 