# CPP_to_ESP32

**Version 1.0.0** - Complete ESP32 Development Workflow

A streamlined development environment for compiling C++ code and deploying to ESP32 microcontrollers.

## 🚀 Features

- **Complete Workflow**: Edit C++ → Build → Flash → Monitor
- **Automated Deployment**: One-command build and flash process
- **Serial Monitoring**: Real-time output monitoring
- **Minimal Setup**: Clean, minimal project structure
- **Cross-Platform**: Works with ESP-IDF framework

## 📁 Project Structure

```
📁 CPP_to_ESP32/
├── 📄 README.md               (This documentation)
├── 📄 CHANGELOG.md            (Version history)
├── 📄 CMakeLists.txt          (ESP-IDF project configuration)
├── 📄 deploy.py               (🚀 Build & flash automation)
├── 📄 monitor.py              (📡 Serial monitor utility)
└── 📁 main/
    ├── 📄 main.cpp            (📝 Your ESP32 C++ code)
    └── 📄 CMakeLists.txt      (Component configuration)
```

## 🛠️ Prerequisites

- **ESP-IDF**: Espressif IoT Development Framework installed
- **Python**: Python 3.7+ with pyserial (`pip install pyserial`)
- **ESP32**: Connected via USB (COM5 by default)
- **Hardware**: ESP32 development board

## ⚡ Quick Start

### 1. **Edit Your Code**
```cpp
// Edit main/main.cpp with your ESP32 program
#include "esp_system.h"
// Your code here...
```

### 2. **Build & Deploy**
```bash
python deploy.py
```

### 3. **Monitor Output**
```bash
python monitor.py
```

## 📝 Usage Guide

### Development Workflow

1. **Write C++ Code**: Edit `main/main.cpp`
2. **Build & Flash**: Run `python deploy.py`
3. **Monitor**: Run `python monitor.py` to see serial output
4. **Iterate**: Repeat the cycle

### Scripts Overview

#### `deploy.py` - Build & Flash Automation
- ✅ Checks ESP32 connection
- ✅ Compiles C++ source code
- ✅ Flashes firmware to ESP32
- ✅ Handles errors gracefully

#### `monitor.py` - Serial Monitor
- 📡 Connects to ESP32 serial output
- 📤 Displays real-time messages
- 🔧 UTF-8 encoding support
- ⏹️ Ctrl+C to stop monitoring

## 🔧 Configuration

### COM Port Settings
Default: `COM5` (Windows)

To change the COM port, edit both scripts:
```python
# In deploy.py and monitor.py
COM_PORT = "COM3"  # Change to your port
```

### ESP-IDF Path
Update paths in `deploy.py` if your ESP-IDF installation differs:
```python
ESP_IDF_PATH = r"C:\Espressif\frameworks\esp-idf-v5.4.1"
ESP_PYTHON = r"C:\Espressif\python_env\idf5.4_py3.11_env\Scripts\python.exe"
```

## 📋 Example Code

The included `main.cpp` demonstrates:
```cpp
extern "C" void app_main() {
    printf("Hello World from ESP32!\n");
    
    while (1) {
        printf("ESP32 is running...\n");
        vTaskDelay(1000 / portTICK_PERIOD_MS);
    }
}
```

## 🐛 Troubleshooting

### Common Issues

**ESP32 Not Detected**
```bash
# Check if device is connected
python -m esptool --port COM5 chip_id
```

**Build Errors**
- Verify ESP-IDF installation
- Check C++ syntax in `main.cpp`
- Ensure CMakeLists.txt is properly configured

**Flash Errors**
- Check COM port availability
- Verify ESP32 is in download mode
- Try different USB cable/port

**Monitor Issues**
- Ensure correct COM port
- Check baud rate (115200)
- Verify ESP32 is running

## 🏗️ Build Process

1. **CMake Configuration**: ESP-IDF generates build files
2. **Compilation**: C++ code compiled with ESP32 toolchain
3. **Linking**: Creates firmware binary files
4. **Flashing**: Uploads to ESP32 flash memory

## 📊 System Requirements

- **OS**: Windows 10/11, macOS, Linux
- **Memory**: 4GB RAM minimum
- **Storage**: 2GB free space
- **USB**: Available USB port for ESP32

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Resources

- [ESP-IDF Programming Guide](https://docs.espressif.com/projects/esp-idf/en/latest/)
- [ESP32 Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf)
- [Espressif GitHub](https://github.com/espressif/esp-idf)

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/Early-Alpha-Engineering/CPP_to_ESP32/issues)
- **Documentation**: This README
- **Community**: ESP32 Forums

---

**Made with ❤️ for ESP32 developers**

*Happy coding! 🚀* 