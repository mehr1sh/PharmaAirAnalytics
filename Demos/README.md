# Demonstrations and Analysis

## Final Deployment - Bachupally

### Primary Project Deployment
**Location**: Bachupally, Hyderabad  
**Focus**: Long-term air quality monitoring near pharmaceutical industries

This is the core deployment for our pharmaceutical industry air quality monitoring project. The site is strategically located in proximity to multiple pharmaceutical manufacturing facilities, enabling continuous monitoring of industrial emissions and their impact on air quality.

**Documentation**: See `Bachupally_Deployment/` for complete deployment photos including:
- Node hardware setup (2 images)
- Camera integration (3 images)
- Deployment building context (2 images)
- Site conditions - day and night (4 images)
- Factory proximity views (2 images)

---

## Diwali Deployment Study

### Overview
This deployment served as a stress test and validation scenario for our environmental monitoring system. The study analyzed the severe environmental impact of firecracker emissions during Diwali by quantifying changes in pollutant concentrations before, during, and after the festival period.

### Study Objectives
- Validate sensor accuracy under high pollution conditions
- Quantify short-term but intense emission impacts
- Compare pollutant levels against WHO and Indian NAAQS standards
- Generate temporal trend analysis of air quality deterioration

---

## Deployment Photos

### `Diwali_Deployment_Node.jpg`
Hardware setup showing the ESP32 environmental monitoring node with all sensors integrated and operational during the Diwali deployment period.

### `Diwali_Deployment_Site.jpg`
Field deployment location and site context where the monitoring node was installed to capture firecracker emission data.

---

## Data Analysis & Visualizations

### `Diwali_Analysis_Plots/`
Time-series plots showing pollutant concentration trends throughout the Diwali period:

| Plot File | Parameter | Description |
|-----------|-----------|-------------|
| `full_timeseries2_plot_field2.png` | **PM10** | Particulate Matter (10 µm) trends |
| `full_timeseries2_plot_field3.png` | **TVOC** | Total Volatile Organic Compounds |
| `full_timeseries2_plot_field4.png` | **eCO2** | Equivalent CO2 levels |
| `full_timeseries2_plot_field5.png` | **Temperature** | Ambient temperature variations |
| `full_timeseries2_plot_field6.png` | **Humidity** | Relative humidity trends |


### Key Findings
The plots reveal:
- **Severe air quality deterioration** during peak Diwali hours
- **Significant exceedances** of WHO and Indian NAAQS standards
- **Rapid pollutant accumulation** during firecracker bursting
- **Recovery patterns** in the post-festival period
- **Correlation between multiple pollutants** during emission events

---

## Study Significance

### Validation Use Case
While our primary project focuses on air quality monitoring near pharmaceutical industries, this Diwali study provided:
- **Real-world stress testing** under extreme pollution conditions
- **System reliability validation** during sustained high-concentration events
- **Multi-pollutant correlation** analysis capabilities
- **Baseline for industrial monitoring** comparison

### Environmental Impact
The study quantifies the **short-term yet severe** degradation of air quality caused by festive firecracker usage, providing data-driven insights into:
- Public health risks during festival periods
- Need for emission control measures
- Effectiveness of environmental monitoring systems

---

## Related Documentation
- Detailed analysis: See `Report/Diwali_Study_Report.pdf`
- Hardware configuration: See `Code/ESP32_Node/README.md`
- Sensor specifications and pin mappings in code documentation
