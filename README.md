[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/Ei5Ot7FV)
# Estimation of Primary Air Pollutants near a Pharmaceutical Industrial Cluster

### Team 16: Venky Chicken

---

## Project Overview

This project focuses on **air quality monitoring near pharmaceutical industries** using an ESP32-based multi-sensor environmental monitoring system. The system continuously tracks key air pollutants and environmental parameters to assess industrial emissions and their impact on surrounding areas.

### Key Objectives
- Monitor baseline air quality in pharmaceutical industrial zones
- Assess pollutant dispersion patterns from manufacturing facilities
- Validate compliance with Indian NAAQS standards
- Quantify public health exposure risks in industrial-residential interface zones

---

## System Specifications

### Hardware Platform
- **Microcontroller**: ESP32
- **Sensors**: 
  - SDS011 (PM2.5, PM10)
  - SGP30 (TVOC, eCO2)
  - AHT10 (Temperature, Humidity)
  - MICS-2714 (NO2)
- **Storage**: SD Card for local logging
- **Connectivity**: WiFi with ThingSpeak cloud integration

### Monitored Parameters
- **Particulate Matter**: PM2.5, PM10 (µg/m³)
- **Air Quality Gases**: TVOC (ppb), eCO2 (ppm), NO2 (ppm)
- **Environmental**: Temperature (°C), Humidity (%)
- **Network**: RSSI (signal strength)

### Data Collection
- **Logging Frequency**: 6-second local, 15-second cloud upload
- **Operation**: 24/7 continuous monitoring
- **Time Sync**: NTP for accurate timestamps (IST)

---

## Repository Structure

### 📁 `Code/`
Contains the production firmware deployed on the ESP32 node.

- **`ESP32_Node/`**: Complete Arduino sketch with multi-sensor integration
  - Hardware initialization and sensor configuration
  - WiFi connectivity and ThingSpeak API integration
  - SD card logging with CSV format
  - Real-time serial monitoring

### 📁 `Demos/`
Field deployment documentation and analysis visualizations.

- **`Bachupally_Deployment/`**: Primary deployment site documentation (13 photos)
  - Node hardware setup and camera integration
  - Deployment building and site context
  - Factory proximity views (day and night)
  
- **`Analysis_Plots/`**: Data visualization
  - `November_Monitoring_Plots.jpg`: 24-hour monitoring analysis (Nov 14-15, 2025)
  
- **Diwali Study**: Validation deployment
  - `Diwali_Deployment_Node.jpg`, `Diwali_Deployment_Site.jpg`
  - `Diwali_Analysis_Plots/`: 6 time-series plots of pollutant trends

### 📁 `Report/`
Comprehensive analysis reports and findings.

- **`One_Day_Report.pdf`**: Primary deployment analysis (Nov 14-15, 2025)
  - 24-hour continuous monitoring at Bachupally
  - Industrial baseline establishment
  - Diurnal pattern analysis
  - NAAQS compliance assessment
  
- **`Diwali_Study_Report.pdf`**: System validation study
  - Stress test under extreme pollution conditions
  - Firecracker emission impact analysis
  - WHO and NAAQS standards comparison

### 📁 `Presentation/`
Final evaluation presentation materials (PDF format).

---

## Deployments

### 1. Primary Deployment - Bachupally (November 2025)
**Location**: Bachupally, Hyderabad (Pharmaceutical industrial zone)  
**Duration**: Long-term continuous monitoring  
**Focus**: Industrial emissions and baseline air quality

**Key Features**:
- Strategic location near multiple pharma manufacturing units
- Residential-industrial interface zone
- 24/7 operation with dual logging (SD + Cloud)

### 2. Validation Study - Diwali (2025)
**Purpose**: System stress test and validation  
**Scenario**: High-pollution event (firecracker emissions)  
**Outcome**: Verified sensor reliability and accuracy under extreme conditions

---

## Technical Highlights

### Multi-Sensor Integration
- Dual I2C buses for concurrent sensor operation
- Hardware serial for PM sensor (UART)
- Analog inputs for gas sensors

### Robust Data Management
- Local SD card backup (power-safe logging)
- Cloud upload with retry mechanism
- Offline mode with uptime-based timestamps

### Real-Time Monitoring
- Serial console with formatted output
- Network diagnostics (IP, MAC, RSSI)
- Sensor health monitoring

---

## Key Findings

### Industrial Monitoring (Bachupally)
- Established baseline pollutant concentrations
- Identified diurnal patterns linked to industrial operations
- Documented meteorological influence on pollutant dispersion
- Assessed exposure levels for nearby residential areas

### Diwali Validation Study
- Severe air quality deterioration during peak hours
- Significant exceedances of WHO and NAAQS standards
- Rapid pollutant accumulation and recovery patterns
- System validated under high-stress conditions

---

## Repository Contents

📂 **Code**: ESP32 production firmware  
📂 **Demos**: 15+ deployment photos, 7 analysis plots  
📂 **Report**: 2 comprehensive analysis reports  
📂 **Presentation**: Final evaluation materials

---

## Team

**Team 16: Venky Chicken**  
Embedded Systems Workshop Project  
Focus: Environmental Monitoring & Air Quality Assessment

---

## Notes

- All code is production-ready and field-tested
- Documentation includes detailed setup and configuration guides
- Analysis reports provide data-driven insights into industrial air quality
- System demonstrates reliability in both normal and extreme pollution conditions
 