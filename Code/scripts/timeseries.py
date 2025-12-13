import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
import numpy as np  # Needed for masking bad data

# ==========================================
# 1. LOAD DATA
# ==========================================
file_path = './datasets/final_dataset.csv'
df = pd.read_csv(file_path)
df['timestamp'] = pd.to_datetime(df['timestamp'])
df = df.set_index('timestamp')

sns.set_theme(style="whitegrid")

# ==========================================
# 2. FILTER ANOMALIES (The Fix)
# ==========================================
# You mentioned spikes of 10-14 ppm. Real ambient NO2 is rarely above 1-2 ppm.
# We replace anything > 8 ppm with NaN (Not a Number) so it doesn't plot.
print(f"Removing {len(df[df['nox_ppm'] > 5])} NO2 spikes > 8 ppm...")
df.loc[df['nox_ppm'] > 5, 'nox_ppm'] = np.nan

# ==========================================
# 3. GENERATE STACKED TIME SERIES
# ==========================================
print("Generating Cleaned Time Series Analysis...")

# Create 3 subplots vertically (Share the X-axis so zooming works on all)
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(14, 10), sharex=True)

# --- PLOT 1: Particulate Matter (PM2.5 & PM10) ---
ax1.plot(df.index, df['pm10'], color='orange', alpha=0.5, linewidth=1, label='PM 10')
ax1.plot(df.index, df['pm25'], color='red', alpha=0.8, linewidth=1.2, label='PM 2.5')
ax1.set_ylabel('Concentration (µg/m³)', fontsize=10)
ax1.set_title('Particulate Matter Trends (Dust & Smoke)', fontsize=12, loc='left')
ax1.legend(loc='upper right')
ax1.grid(True, linestyle='--', alpha=0.5)

# --- PLOT 2: Nitrogen Oxides (NOx) ---
# Now filtered to show only real data
ax2.plot(df.index, df['nox_ppm'], color='green', alpha=0.8, linewidth=1, label='NOx')
ax2.set_ylabel('Concentration (ppm)', fontsize=10)
ax2.set_title('Nitrogen Oxide Trends (Traffic/Combustion)', fontsize=12, loc='left')
ax2.legend(loc='upper right')
ax2.grid(True, linestyle='--', alpha=0.5)

# --- PLOT 3: Carbon Dioxide (CO2) ---
ax3.plot(df.index, df['co2_ppm'], color='purple', alpha=0.8, linewidth=1, label='CO2')
ax3.set_ylabel('Concentration (ppm)', fontsize=10)
ax3.set_title('CO2 Trends (Ventilation/Activity)', fontsize=12, loc='left')
ax3.legend(loc='upper right')
ax3.grid(True, linestyle='--', alpha=0.5)

# --- FORMATTING ---
ax3.set_xlabel('Date (Day-Month)', fontsize=12)
ax3.xaxis.set_major_locator(mdates.DayLocator(interval=2)) # Tick every 2 days
ax3.xaxis.set_major_formatter(mdates.DateFormatter('%d-%b'))
plt.xticks(rotation=45)

plt.suptitle(f'30-Day Air Quality Monitoring: General Time Series', fontsize=16)
plt.tight_layout()

save_path = './plots/time_series.png'
plt.savefig(save_path, dpi=300, bbox_inches='tight')

plt.show()