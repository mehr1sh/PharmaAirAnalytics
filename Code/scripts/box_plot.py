import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# ==========================================
# 1. LOAD DATA
# ==========================================
file_path = './datasets/final_dataset.csv'
df = pd.read_csv(file_path)

# Filter the NO2 spikes > 8 ppm (consistency with previous step)
df.loc[df['nox_ppm'] > 8, 'nox_ppm'] = np.nan

# ==========================================
# 2. PREPARE DATA FOR BOX PLOT
# ==========================================
print("Generating Statistical Box Plot...")

# We select all relevant parameters
params = ['pm25', 'pm10', 'nox_ppm', 'co2_ppm', 'temp_C', 'hum_percent']
df_subset = df[params]

# "Melt" the dataframe: Converts it from wide format (cols) to long format (rows)
# This is required for Seaborn to plot them side-by-side
df_melted = df_subset.melt(var_name='Parameter', value_name='Value')

# ==========================================
# 3. VISUALIZE
# ==========================================
plt.figure(figsize=(12, 8))

# Create the Box Plot
# showfliers=True means "Show the outlier dots"
sns.boxplot(x='Parameter', y='Value', data=df_melted, palette="Set2", showfliers=True)

# Use Log Scale because values range from 0.1 (NOx) to 1000 (CO2)
plt.yscale('log')

# Decoration
plt.title('Statistical Distribution of All Parameters (Log Scale)', fontsize=16)
plt.ylabel('Value (Log Scale)', fontsize=12)
plt.xlabel('Sensor Parameter', fontsize=12)
plt.grid(True, which="both", ls="--", alpha=0.5)

# Add Annotation for Evaluators
plt.text(x=0.5, y=0.5, s="Dots = Transient Events\nLine = Median Baseline", 
         transform=plt.gca().transAxes, 
         bbox=dict(facecolor='white', alpha=0.8), ha='center')

plt.tight_layout()

save_path = './plots/box_plot.png'
plt.savefig(save_path, dpi=300, bbox_inches='tight')

plt.show()