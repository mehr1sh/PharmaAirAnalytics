import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


file_path = './datasets/final_dataset.csv'
df = pd.read_csv(file_path)

# Select only the numeric sensor columns
# We drop 'timestamp' or 'millis' because you can't correlate time with chemistry
sensor_cols = ['pm25', 'pm10', 'nox_ppm', 'co2_ppm', 'temp_C', 'hum_percent']
df_corr = df[sensor_cols]

# The .corr() method uses Pearson correlation by default
corr_matrix = df_corr.corr()

# Let's print the specific numbers for your investigation
nox_temp_corr = corr_matrix.loc['nox_ppm', 'temp_C']
nox_pm_corr = corr_matrix.loc['nox_ppm', 'pm25']

print("--- INVESTIGATION RESULTS ---")
print(f"Correlation: NOx vs Temp  = {nox_temp_corr:.4f}")
print(f"Correlation: NOx vs PM2.5 = {nox_pm_corr:.4f}")


plt.figure(figsize=(10, 8))

# Draw the heatmap
# vmin=-1, vmax=1 ensures the colors are balanced (Blue=Neg, Red=Pos)
sns.heatmap(corr_matrix, 
            annot=True,       # Show the numbers in the boxes
            cmap='coolwarm',  # Red-Blue color scheme
            fmt=".2f",        # 2 decimal places
            vmin=-1, vmax=1,  # Lock scale to -1 to 1
            linewidths=1,     # Add white lines between boxes
            linecolor='black')

plt.title('Pharma Air Quality: Sensor Correlation Matrix', fontsize=16)
plt.tight_layout()

save_path = './plots/correlation_heatmap.png'
plt.savefig(save_path, dpi=300, bbox_inches='tight')
print(f"Saved plot to {save_path}")

plt.show()