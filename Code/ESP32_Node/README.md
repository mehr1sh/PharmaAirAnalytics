# ESP32 Environmental Monitoring Node

## Overview
This is the final production code deployed on the ESP32 node for environmental monitoring. The system collects air quality and environmental data from multiple sensors and uploads it to ThingSpeak for remote monitoring.

## Hardware Components

### Sensors
- **SDS011** - Particulate Matter (PM2.5, PM10) sensor
- **SGP30** - Air Quality sensor (TVOC, eCO2)
- **AHT10** - Temperature & Humidity sensor
- **MICS-2714** - NO2 concentration sensor (analog)

### Storage & Communication
- **SD Card Module** - Local data logging
- **WiFi** - Cloud connectivity for ThingSpeak upload

## Pin Configuration

| Component | Pin(s) |
|-----------|--------|
| SDS011 RX | GPIO 16 |
| SDS011 TX | GPIO 17 |
| SGP30 I2C | SDA: GPIO 21, SCL: GPIO 22 |
| AHT10 I2C | SDA: GPIO 25, SCL: GPIO 26 |
| MICS-2714 | GPIO 35 (Analog) |
| SD Card CS | GPIO 5 |

## Features

### Data Collection
- PM2.5 and PM10 measurements (µg/m³)
- Total Volatile Organic Compounds (TVOC) in ppb
- Equivalent CO2 (eCO2) in ppm
- Temperature (°C) and Humidity (%)
- NO2 concentration (estimated)

### Data Logging
- **Local Storage**: Data logged to SD card (`env_data.csv`) every 6 seconds
- **Cloud Upload**: ThingSpeak upload every 15 seconds (when WiFi connected)
- **Serial Monitor**: Real-time data display with network status

### Network Features
- WiFi connectivity with 10-second timeout
- NTP time synchronization (IST timezone)
- Offline mode with uptime tracking
- RSSI monitoring and logging

## ThingSpeak Integration

### Field Mapping
- Field 1: PM2.5 (µg/m³)
- Field 2: PM10 (µg/m³)
- Field 3: TVOC (ppb)
- Field 4: eCO2 (ppm)
- Field 5: Temperature (°C)
- Field 6: Humidity (%)
- Field 8: NO2 Concentration

## Configuration

### WiFi Credentials
Update these in the code:
```cpp
const char* ssid = "YOUR_SSID";
const char* password = "YOUR_PASSWORD";
```

### ThingSpeak API Key
Replace with your channel's Write API Key:
```cpp
String thingSpeakAPIKey = "YOUR_API_KEY";
```

## Data Output Format

### SD Card CSV Structure
```
Date,Time,PM2.5,PM10,TVOC,eCO2,Temp,Humidity,NO2,RSSI
```

### Serial Monitor Output
```
=== ENVIRONMENTAL NODE ===
2025-12-03 14:30:45
IP: 192.168.x.x | MAC: XX:XX:XX:XX:XX:XX | RSSI: -65 dBm
--------------------------
PM2.5: 12.3 | PM10: 18.5 µg/m³
TVOC: 45 ppb | eCO2: 420 ppm
T: 26.5 °C | H: 65.2 %
NO2 (est): 1.23
==========================
```

## Required Libraries
- Adafruit_SGP30
- Adafruit_AHTX0
- SD
- WiFi
- HTTPClient
- Wire
- SPI

## Installation
1. Install required libraries via Arduino Library Manager
2. Update WiFi credentials and ThingSpeak API key
3. Upload to ESP32 board
4. Insert formatted SD card (FAT32)
5. Power on and monitor via Serial Monitor (115200 baud)

## Operating Modes

### Online Mode
- WiFi connected
- Real-time clock via NTP
- ThingSpeak uploads enabled
- Full logging with RSSI

### Offline Mode
- No WiFi connection
- Uptime-based timestamps
- Local SD logging only
- Reduced power consumption

## Notes
- Minimum 15-second interval between ThingSpeak uploads (API limit)
- SGP30 uses AHT10 data for humidity compensation
- System continues operation even if individual sensors fail
- Automatic CSV header creation on first run
