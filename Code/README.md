# Code Structure

## ESP32_Node/
Production code for the deployed ESP32 environmental monitoring node.

### Features
- Multi-sensor data acquisition (PM2.5, PM10, TVOC, eCO2, Temperature, Humidity, NO2)
- Local SD card logging
- Cloud connectivity via ThingSpeak
- NTP time synchronization
- Offline fallback mode

### Sensors Used
- SDS011 (Particulate Matter)
- SGP30 (Air Quality)
- AHT10 (Temperature & Humidity)
- MICS-2714 (NO2)

See `ESP32_Node/README.md` for detailed documentation, pin configuration, and setup instructions.