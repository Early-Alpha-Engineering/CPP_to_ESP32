# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2024-12-19

### 🎉 Major Platform Migration

#### Added
- **PlatformIO Integration**
  - Complete migration from ESP-IDF to PlatformIO platform
  - Arduino framework support for easier development
  - Automatic platform and toolchain management
  - Cross-platform compatibility (Windows, macOS, Linux)

- **Enhanced Documentation**
  - Comprehensive installation section with step-by-step instructions
  - PlatformIO command reference
  - Multiple installation methods (pip, installer script)
  - WiFi connection example code
  - Migration guide from ESP-IDF to PlatformIO

- **New Project Structure**
  - `platformio.ini` - Modern project configuration
  - `src/main.cpp` - Arduino-style source code
  - `.gitignore` - Proper build artifact exclusion
  - Removed legacy ESP-IDF CMakeLists.txt files

- **Improved Build System**
  - One-command build and upload: `pio run --target upload`
  - Built-in serial monitor: `pio device monitor`
  - Automatic dependency management
  - Faster, more reliable builds

#### Changed
- **Code Framework**: Migrated from ESP-IDF native to Arduino framework
  - Replaced `app_main()` with `setup()` and `loop()`
  - Using `Serial` instead of UART drivers
  - Simplified API calls and better debugging support

- **Project Structure**: 
  - Moved `main/main.cpp` to `src/main.cpp`
  - Replaced CMakeLists.txt with platformio.ini
  - Updated deploy.py for better ESP-IDF environment handling

- **Documentation**: Complete rewrite of README.md
  - Added comprehensive installation guide
  - Updated all examples to PlatformIO/Arduino framework
  - Added troubleshooting for PlatformIO-specific issues

#### Fixed
- **Build Reliability**: Resolved ESP-IDF gdbinit.cmake compatibility issues
- **Environment Setup**: Better Python environment detection and configuration
- **Toolchain Management**: Automatic ESP32 toolchain installation via PlatformIO

#### Technical Details
- **Platform**: PlatformIO with Espressif 32 platform
- **Framework**: Arduino for ESP32
- **Board**: esp32dev (generic ESP32)
- **Upload Speed**: 921600 baud
- **Monitor Speed**: 115200 baud

## [1.0.0] - 2024-12-19

### 🎉 Initial Release

#### Added
- **Complete ESP32 Development Workflow**
  - C++ source code compilation
  - Automated build and flash process
  - Real-time serial monitoring
  
- **Core Scripts**
  - `deploy.py` - Automated build and flash tool
  - `monitor.py` - Serial monitor utility
  - `main/main.cpp` - Hello World ESP32 example
  
- **Project Structure**
  - ESP-IDF compatible CMakeLists.txt files
  - Minimal, clean project organization
  - Documentation and examples

- **Features**
  - ✅ ESP32 connection verification
  - ✅ One-command deployment (`python deploy.py`)
  - ✅ Real-time serial output monitoring
  - ✅ Error handling and user feedback
  - ✅ UTF-8 encoding support
  - ✅ Cross-platform compatibility

- **Documentation**
  - Comprehensive README.md
  - Usage guide and examples
  - Troubleshooting section
  - Configuration instructions

#### Technical Details
- **ESP-IDF Version**: 5.4.1 compatible
- **Target Platform**: ESP32 (ESP32-D0WDQ6)
- **Communication**: COM5 @ 115200 baud (configurable)
- **Build System**: ESP-IDF + CMake
- **Programming Language**: C++ for ESP32, Python for tooling

#### Tested Hardware
- ESP32-D0WDQ6 (revision v1.1)
- 4MB Flash memory
- Windows 10/11 development environment

### 🔧 Configuration
- Default COM port: COM5
- Default baud rate: 115200
- ESP-IDF path: `C:\Espressif\frameworks\esp-idf-v5.4.1`
- Python environment: `idf5.4_py3.11_env`

---

## [Unreleased]

### Planned Features
- [ ] Multi-platform COM port auto-detection
- [ ] Configuration file support
- [ ] Additional ESP32 example projects
- [ ] Unit testing framework
- [ ] Continuous integration setup
- [ ] GUI version of deployment tool
- [ ] ESP32-S3 and ESP32-C3 board support
- [ ] Library dependency examples

---

## Version History

- **v1.1.0** - PlatformIO migration with Arduino framework
- **v1.0.0** - Initial release with ESP-IDF workflow

---

**Legend:**
- 🎉 Major release
- ✨ New feature
- 🔧 Configuration change
- 🐛 Bug fix
- 📝 Documentation
- 🗑️ Removed feature
- ⚠️ Breaking change 