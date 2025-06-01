#include <Arduino.h>
#include <WiFi.h>

void setup() {
    // Initialize serial communication
    Serial.begin(115200);
    
    // Wait for serial port to connect
    while (!Serial) {
        delay(10);
    }
    
    // Print chip information
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