# Project Reports

## Diwali_Study_Report.pdf

### Study Title
**Environmental Impact Analysis of Firecracker Emissions During Diwali Festival**

### Abstract
This study analyzes the environmental impact of firecracker emissions during Diwali by quantifying changes in pollutant concentrations before, during, and after the festival period. The report presents temporal pollutant trends, statistical summaries, and exceedances of WHO and Indian NAAQS (National Ambient Air Quality Standards), revealing the severe deterioration of air quality due to short-term yet intense emissions.

### Study Context
While the core focus of our larger project is **air quality monitoring near pharmaceutical industries**, this Diwali-based study serves as:
- **Stress test** for the monitoring system under extreme conditions
- **Validation scenario** for sensor accuracy and reliability
- **Benchmark study** for comparing industrial vs. event-based pollution

### Key Contents
1. **Temporal Analysis** - Before, during, and after Diwali pollution patterns
2. **Statistical Summaries** - Mean, median, peak concentrations, and variability
3. **Standards Compliance** - Comparison with WHO guidelines and Indian NAAQS limits
4. **Pollutant Correlations** - Multi-parameter relationship analysis
5. **Health Implications** - Air quality index and exposure risk assessment

### Parameters Monitored
- PM2.5 and PM10 (Particulate Matter)
- TVOC (Total Volatile Organic Compounds)
- eCO2 (Equivalent Carbon Dioxide)
- Temperature and Humidity
- UV Intensity
- NO2 (Nitrogen Dioxide)

### Deployment Details
- **Location**: Field deployment site (residential area)
- **Duration**: Pre-Diwali, Diwali night, and post-Diwali recovery period
- **Hardware**: ESP32-based multi-sensor environmental monitoring node
- **Data Frequency**: 6-second local logging, 15-second cloud upload

### Key Findings
- **Severe exceedances** of air quality standards during peak firecracker hours
- **Rapid concentration spikes** in PM2.5, PM10, and TVOC
- **Prolonged recovery period** with sustained elevated pollution levels
- **System validation** demonstrating sensor reliability under high-stress conditions

### Related Materials
- Deployment photos: `Demos/Diwali_Deployment_Node.jpg`, `Demos/Diwali_Deployment_Site.jpg`
- Analysis plots: `Demos/Diwali_Analysis_Plots/`
- Source code: `Code/ESP32_Node/`

---

## One_Day_Report.pdf

### Study Title
**One-Day Air Quality Monitoring in Pharmaceutical Industrial Zone**

### Study Period
**November 14-15, 2025** (24-hour continuous monitoring)

### Abstract
This report presents comprehensive air quality analysis from the primary deployment site at Bachupally. The study captures baseline environmental conditions near pharmaceutical industries over a 24-hour monitoring period, providing insights into industrial emission patterns, diurnal variations, and compliance with ambient air quality standards.

### Study Context
This represents the **core project deployment** for pharmaceutical industry air quality monitoring. Unlike the Diwali validation study (short-term event analysis), this one-day intensive monitoring establishes:
- **Industrial baseline** under normal operational conditions
- **Temporal patterns** (diurnal day-night cycles)
- **Meteorological correlations** with pollution levels
- **Exposure assessment** for nearby residential areas

### Key Contents
1. **24-Hour Time-Series Analysis** - Continuous pollutant trends
2. **Diurnal Pattern Recognition** - Day-night variations
3. **Industrial Correlation** - Relationship between factory operations and air quality
4. **Standards Compliance** - Comparison with Indian NAAQS limits
5. **Meteorological Impact** - Temperature, humidity influence on pollutant dispersion

### Monitoring Location
- **Site**: Bachupally, Hyderabad
- **Environment**: Residential building adjacent to pharmaceutical manufacturing zone
- **Elevation**: Rooftop deployment for representative air sampling
- **Industrial Proximity**: Multiple pharma units within 500m radius

### Parameters Monitored
- PM2.5 and PM10 (Particulate Matter)
- TVOC (Total Volatile Organic Compounds)
- eCO2 (Equivalent Carbon Dioxide)
- Temperature and Humidity
- NO2 (Nitrogen Dioxide)
- Network RSSI (connectivity monitoring)

### Data Characteristics
- **Duration**: 24 hours (Nov 14-15, 2025)
- **Frequency**: 6-second local logging, 15-second cloud upload
- **Total Data Points**: ~5,760+ sensor readings per parameter
- **Data Quality**: Continuous operation with minimal gaps

### Key Findings
- **Industrial baseline** pollutant concentrations established
- **Diurnal patterns** showing elevated levels during operational hours
- **Meteorological influence** on pollutant dispersion observed
- **Compliance assessment** against NAAQS standards
- **System reliability** demonstrated over continuous deployment

### Related Materials
- Deployment site photos: `Demos/Bachupally_Deployment/` (13 images)
- Analysis plots: `Demos/Analysis_Plots/November_Monitoring_Plots.jpg`
- Source code: `Code/ESP32_Node/`

---

## Future Reports
Additional project reports and documentation will be added here as the project progresses.
