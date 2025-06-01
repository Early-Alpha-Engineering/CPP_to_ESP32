# CPP_to_ESP32

**Version 1.0.0** - Complete ESP32 Development Workflow with PlatformIO

A streamlined development environment for compiling C++ code and deploying to ESP32 microcontrollers using PlatformIO.

## 🚀 Features

- **Complete Workflow**: Edit C++ → Build → Flash → Monitor
- **PlatformIO Integration**: Modern, reliable ESP32 development platform
- **Arduino Framework**: Easy-to-use Arduino-style programming
- **Automated Deployment**: One-command build and flash process
- **Serial Monitoring**: Real-time output monitoring
- **Minimal Setup**: Clean, minimal project structure
- **Cross-Platform**: Works on Windows, macOS, and Linux

## 📁 Project Structure

```
📁 CPP_to_ESP32/
├── 📄 README.md               (This documentation)
├── 📄 CHANGELOG.md            (Version history)
├── 📄 platformio.ini          (PlatformIO project configuration)
├── 📄 deploy.py               (🚀 Legacy ESP-IDF automation)
├── 📄 monitor.py              (📡 Serial monitor utility)
└── 📁 src/
    └── 📄 main.cpp            (📝 Your ESP32 C++ code)
```

## 🛠️ Installation

### Prerequisites

- **Python 3.7+** installed on your system
- **USB Cable** to connect ESP32 to your computer
- **ESP32 Development Board**

### Step 1: Install PlatformIO Core

#### Option A: Install via pip (Recommended)
```bash
pip install platformio
```

#### Option B: Install via installer script
```bash
# Windows PowerShell
iex (New-Object System.Net.WebClient).DownloadString('https://raw.githubusercontent.com/platformio/platformio-core-installer/main/get-platformio.py')

# macOS/Linux
curl -fsSL https://raw.githubusercontent.com/platformio/platformio-core-installer/main/get-platformio.py | python3
```

### Step 2: Clone the Repository
```bash
git clone https://github.com/Early-Alpha-Engineering/CPP_to_ESP32.git
cd CPP_to_ESP32
```

### Step 3: Install Project Dependencies
```bash
# PlatformIO will automatically download ESP32 platform and toolchain
pio run
```

### Step 4: Connect Your ESP32
1. Connect ESP32 to your computer via USB
2. Note the COM port (Windows) or device path (macOS/Linux)
3. Update `platformio.ini` if using a different port than COM5

## ⚡ Quick Start

### 1. **Edit Your Code**
```cpp
// Edit src/main.cpp with your ESP32 program
#include <Arduino.h>

void setup() {
    Serial.begin(115200);
    Serial.println("Hello ESP32!");
}

void loop() {
    Serial.println("ESP32 is running...");
    delay(1000);
}
```

### 2. **Build & Deploy**
```bash
# Build the project
pio run

# Build and upload to ESP32
pio run --target upload

# Build, upload, and monitor
pio run --target upload --target monitor
```

### 3. **Monitor Output**
```bash
# Using PlatformIO monitor
pio device monitor --port COM5 --baud 115200

# Or using the legacy monitor script
python monitor.py
```

## 📝 Usage Guide

### Development Workflow

1. **Write C++ Code**: Edit `src/main.cpp`
2. **Build & Flash**: Run `pio run --target upload`
3. **Monitor**: Run `pio device monitor` to see serial output
4. **Iterate**: Repeat the cycle

### PlatformIO Commands

#### Building
```bash
pio run                    # Build project
pio run -v                 # Verbose build output
pio run --target clean     # Clean build files
```

#### Uploading
```bash
pio run --target upload              # Upload to ESP32
pio run --target upload --port COM3  # Upload to specific port
```

#### Monitoring
```bash
pio device monitor                   # Start serial monitor
pio device monitor --port COM5       # Monitor specific port
pio device monitor --baud 9600       # Custom baud rate
```

#### Combined Operations
```bash
pio run --target upload --target monitor  # Upload and monitor
```

### Legacy Scripts (ESP-IDF)

For reference, the original ESP-IDF scripts are still available:

#### `deploy.py` - ESP-IDF Build & Flash
- ✅ Checks ESP32 connection  
- ✅ Compiles using ESP-IDF
- ✅ Flashes firmware to ESP32
- ⚠️ Requires ESP-IDF installation

#### `monitor.py` - Serial Monitor
- 📡 Connects to ESP32 serial output
- 📤 Displays real-time messages
- 🔧 UTF-8 encoding support
- ⏹️ Ctrl+C to stop monitoring

## 🔧 Configuration

### PlatformIO Configuration (`platformio.ini`)

```ini
[env:esp32dev]
platform = espressif32
board = esp32dev
framework = arduino
monitor_speed = 115200
upload_port = COM5
monitor_port = COM5
upload_speed = 921600

; Custom build flags
build_flags = 
    -DCORE_DEBUG_LEVEL=3

; Library dependencies
lib_deps = 
    ; Add libraries here
```

### Changing COM Port
Update `platformio.ini`:
```ini
upload_port = COM3      ; Windows
; upload_port = /dev/ttyUSB0  ; Linux
; upload_port = /dev/cu.usbserial-*  ; macOS
```

### Board Configuration
For different ESP32 boards, update the `board` setting:
```ini
board = esp32dev        ; Generic ESP32
board = esp32-s3-devkitc-1  ; ESP32-S3
board = esp32-c3-devkitm-1   ; ESP32-C3
```

## 📋 Example Code

### Basic Hello World
```cpp
#include <Arduino.h>

void setup() {
    Serial.begin(115200);
    
    Serial.println("ESP32 Hello World!");
    Serial.printf("ESP32 Chip model: %s\n", ESP.getChipModel());
    Serial.printf("Number of cores: %d\n", ESP.getChipCores());
    Serial.printf("CPU Frequency: %d MHz\n", ESP.getCpuFreqMHz());
    Serial.printf("Flash size: %d MB\n", ESP.getFlashChipSize() / (1024 * 1024));
    Serial.printf("Free heap: %d bytes\n", ESP.getFreeHeap());
    Serial.println("Setup complete!");
}

void loop() {
    Serial.println("Hello World from ESP32!");
    delay(1000);  // Delay for 1 second
}
```

### WiFi Connection Example
```cpp
#include <Arduino.h>
#include <WiFi.h>

const char* ssid = "your_wifi_name";
const char* password = "your_wifi_password";

void setup() {
    Serial.begin(115200);
    
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED) {
        delay(1000);
        Serial.println("Connecting to WiFi...");
    }
    
    Serial.println("WiFi connected!");
    Serial.print("IP address: ");
    Serial.println(WiFi.localIP());
}

void loop() {
    // Your main code here
    delay(1000);
}
```

## 🐛 Troubleshooting

### Installation Issues

**PlatformIO not found**
```bash
# Add to PATH or use full path
~/.platformio/penv/bin/pio run
```

**Permission denied (Linux/macOS)**
```bash
sudo usermod -a -G dialout $USER  # Add user to dialout group
sudo chmod 666 /dev/ttyUSB0        # Grant permissions to device
```

### Build Issues

**Platform not installed**
```bash
pio platform install espressif32
```

**Library dependency errors**
```bash
pio lib install "Library Name"
```

### Upload Issues

**Device not found**
```bash
# List available devices
pio device list

# Check if ESP32 is detected
pio device monitor --port COM5
```

**Permission errors (Windows)**
- Close other programs using the COM port
- Try different USB port
- Update ESP32 drivers

### Monitor Issues

**No output**
- Check baud rate matches (115200)
- Verify ESP32 is running
- Try resetting ESP32

## 🏗️ Build Process

### PlatformIO Build Pipeline

1. **Platform Detection**: Identifies ESP32 platform requirements
2. **Toolchain Download**: Downloads ESP32 compiler toolchain
3. **Framework Setup**: Configures Arduino framework
4. **Compilation**: Compiles C++ code with ESP32 toolchain
5. **Linking**: Creates firmware binary files
6. **Upload**: Flashes firmware to ESP32 via serial

### Build Artifacts

```
.pio/build/esp32dev/
├── firmware.bin        # Main firmware binary
├── firmware.elf        # ELF executable
├── bootloader.bin      # ESP32 bootloader
└── partitions.bin      # Partition table
```

## 📊 System Requirements

- **OS**: Windows 10/11, macOS 10.13+, Linux (Ubuntu 16.04+)
- **Python**: 3.7+ with pip
- **Memory**: 2GB RAM minimum
- **Storage**: 1GB free space
- **USB**: Available USB port for ESP32

## 🔄 Migration from ESP-IDF

If migrating from pure ESP-IDF:

1. **Install PlatformIO** (see installation section)
2. **Create platformio.ini** configuration
3. **Move code** from `main/main.cpp` to `src/main.cpp`
4. **Convert code** from ESP-IDF to Arduino framework:
   - Replace `app_main()` with `setup()` and `loop()`
   - Use `Serial` instead of `printf`
   - Include `<Arduino.h>` instead of ESP-IDF headers

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Resources

- [PlatformIO Documentation](https://docs.platformio.org/)
- [ESP32 Arduino Core](https://github.com/espressif/arduino-esp32)
- [ESP32 Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf)
- [Espressif GitHub](https://github.com/espressif)

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/Early-Alpha-Engineering/CPP_to_ESP32/issues)
- **Documentation**: This README
- **Community**: [PlatformIO Community](https://community.platformio.org/)

---

**Made with ❤️ for ESP32 developers**

*Happy coding! 🚀* 