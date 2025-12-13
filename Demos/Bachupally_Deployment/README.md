# Final Deployment - Bachupally

## Deployment Overview

**Location**: Bachupally, Hyderabad  
**Purpose**: Air quality monitoring near pharmaceutical and industrial facilities  
**Deployment Type**: Long-term environmental monitoring station  
**System**: ESP32-based multi-sensor node with camera integration

---

## Site Context

### Industrial Environment
Bachupally is located in proximity to multiple pharmaceutical manufacturing units and industrial facilities. This deployment site was strategically selected to:
- Monitor baseline air quality in industrial zones
- Assess pollutant dispersion patterns from nearby factories
- Validate sensor performance in real industrial conditions
- Collect long-term environmental data for pharmaceutical zone analysis

---

## Deployment Documentation

### Node Hardware Setup

#### `nodedeployment.jpg`
Primary environmental monitoring node showing the ESP32 system with all integrated sensors (PM2.5/PM10, TVOC, eCO2, Temperature, Humidity, NO2) in weatherproof housing.

#### `nodedeployment2.jpg`
Alternate view of the sensor node deployment, highlighting mounting configuration and sensor positioning for optimal air sampling.

### Camera Integration

#### `cameranodedeployment.jpg`
Camera module integrated with the monitoring system for visual documentation and site surveillance.

#### `cameranodedeployment2.jpg`
Camera deployment angle and coverage area, capturing the industrial surroundings and pollution sources.

#### `cameranodedeployment3.jpg`
Complete camera node setup showing power supply, connectivity, and environmental protection measures.

---

## Site Characteristics

### Deployment Building

#### `deploymentbuilding.jpg`
The residential building where the monitoring node is installed, showing elevation and positioning relative to surrounding structures.

#### `deploymentbuilding2.jpg`
Additional view of the deployment building, illustrating the strategic rooftop/elevated placement for representative air quality sampling.

### Daytime Site Conditions

#### `deploymentsiteday.jpg`
Daytime panoramic view of the deployment site showing clear visibility of surrounding pharmaceutical factories and industrial units.

#### `deploymentsiteday2.jpg`
Additional daytime perspective capturing the industrial landscape and proximity to emission sources.

### Factory Proximity

#### `deploymentsitefactory.jpg`
Direct view of nearby pharmaceutical manufacturing facility, demonstrating the close industrial proximity that justifies continuous air quality monitoring.

#### `deploymentsitefactory2.jpg`
Additional factory view showing multiple industrial structures and potential emission points in the monitoring zone.

### Nighttime Monitoring

#### `deploymentsitenight.jpg`
Nighttime view of the deployment site, showing illuminated industrial facilities and 24/7 operational visibility.

#### `deploymentsitenight2.jpg`
Night scene capturing active industrial operations, relevant for analyzing day-night pollution variation patterns.

---

## Monitoring Objectives

### Deployment Period
**November 14-15, 2025** - 24-hour continuous monitoring capturing full diurnal cycle of industrial air quality.

### Primary Goals
1. **Industrial Baseline Monitoring** - Establish air quality baseline near pharmaceutical facilities
2. **Emission Pattern Analysis** - Identify temporal pollution trends (daily, weekly cycles)
3. **Compliance Verification** - Compare measured levels against NAAQS standards
4. **Public Health Assessment** - Quantify exposure levels for nearby residential areas

### Data Collection
- **Continuous monitoring**: 24/7 operation
- **Data frequency**: 6-second local logging, 15-second cloud upload
- **Parameters tracked**: PM2.5, PM10, TVOC, eCO2, Temperature, Humidity, NO2
- **Storage**: Local SD card + ThingSpeak cloud platform

### Expected Insights
- Correlation between industrial activity and pollutant levels
- Seasonal and meteorological impact on air quality
- Effectiveness of emission control measures
- Long-term exposure risk assessment

---

## Strategic Significance

### Why Synergy Hilltop, Bachupally?
1. **Pharmaceutical Hub** - Multiple pharma units in immediate vicinity
2. **Residential Proximity** - Public health impact assessment
3. **Representative Location** - Typical industrial-residential interface zone
4. **Accessibility** - Reliable power, network connectivity for continuous operation

### Comparison with Diwali Study
Unlike the temporary Diwali deployment (event-based stress test), this represents:
## Strategic Significance

### Why Bachupally?
1. **Pharmaceutical Hub** - Multiple pharma units in immediate vicinity
2. **Residential Proximity** - Public health impact assessment
3. **Representative Location** - Typical industrial-residential interface zone
4. **Accessibility** - Reliable power, network connectivity for continuous operation
## Technical Details
- **Hardware**: ESP32 + Multi-sensor array + Camera module
- **Connectivity**: WiFi with ThingSpeak integration
- **Power**: Continuous mains supply with backup
- **Protection**: Weatherproof enclosures for electronics and sensors
- **Maintenance**: Periodic sensor calibration and SD card data retrieval
## Related Documentation
- System code: `Code/ESP32_Node/`
- Multi-day analysis report: `Report/Synergy_Deployment_Nov4-15_Report.pdf`
- Diwali validation study: `Demos/` (Diwali deployment)
- All project reports: `Report/`
- System code: `Code/ESP32_Node/`
- Diwali validation study: `Demos/` (Diwali deployment)
- Analysis reports: `Report/`
## Related Documentation
- System code: `Code/ESP32_Node/`
- Multi-day analysis report: `Report/One_Day_Report.pdf`
- Analysis plots: `Demos/Analysis_Plots/`
- Diwali validation study: `Demos/` (Diwali deployment)
- All project reports: `Report/`