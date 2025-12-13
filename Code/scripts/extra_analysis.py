import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# ==========================================
# 1. LOAD DATA
# ==========================================
df = pd.read_csv('./datasets/final_dataset.csv')
df['timestamp'] = pd.to_datetime(df['timestamp'])
df = df.set_index('timestamp')

# Set thresholds (Use WHO or Local Industrial Standards)
SAFE_LIMIT_PM25 = 60.0  # Example: Indian CPCB Industrial Limit (24h is 60-80 usually)

# ==========================================
# PART A: HYGROSCOPIC GROWTH CURVE (Physics)
# ==========================================
print("Generating Hygroscopic Growth Model...")

# 1. Filter data to remove Combustion Events
# We want to see how DUST behaves with humidity, not how SMOKE behaves.
# So we only look at times when NOx is LOW (no trucks/boilers).
dust_df = df[df['nox_ppm'] < df['nox_ppm'].quantile(0.5)].copy()

# 2. Bin Humidity into 5% buckets (0-5%, 5-10%...)
dust_df['hum_bucket'] = (dust_df['hum_percent'] // 5) * 5

# 3. Calculate Mean PM2.5 for each bucket
growth_curve = dust_df.groupby('hum_bucket')['pm25'].agg(['mean', 'std']).reset_index()
# Filter out empty buckets or buckets with too few points (outliers)
growth_curve = growth_curve[growth_curve['hum_bucket'].between(20, 95)] 

# 4. Plot
plt.figure(figsize=(10, 6))
sns.regplot(x='hum_bucket', y='mean', data=growth_curve, order=2, scatter_kws={'s': 100}, line_kws={'color':'red'})

plt.xlabel('Relative Humidity (%)', fontsize=12)
plt.ylabel('Average PM 2.5 Concentration (µg/m³)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
save_path = './plots/humidityvsPM2.5.png'
plt.savefig(save_path, dpi=300, bbox_inches='tight')
print(f"Saved plot to {save_path}")
plt.show()