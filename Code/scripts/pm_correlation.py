import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


file_path = './datasets/final_dataset.csv'
df = pd.read_csv(file_path)

# ==========================================
# 2. CALCULATE THE RATIO
# ==========================================
# We use numpy to avoid "Division by Zero" errors if PM10 is 0
# Logic: If PM10 is 0, the ratio is NaN (we drop it later)
df['pm_ratio'] = df['pm25'] / df['pm10'].replace(0, np.nan)

# PHYSICS FIX:
# Ideally, PM2.5 <= PM10. If a sensor glitch makes Ratio > 1.0, we cap it at 1.0.
df['pm_ratio'] = df['pm_ratio'].clip(upper=1.0)
df = df.dropna(subset=['pm_ratio'])

# ==========================================
# 3. STATISTICAL DIAGNOSIS
# ==========================================
avg_ratio = df['pm_ratio'].mean()
median_ratio = df['pm_ratio'].median()

# Count how many points fall into each category
fine_count = (df['pm_ratio'] > 0.6).sum()
coarse_count = (df['pm_ratio'] < 0.4).sum()
total_count = len(df)

print(f"--- PARTICLE COMPOSITION REPORT ---")
print(f"Average Ratio: {avg_ratio:.3f}")
print(f"Median Ratio:  {median_ratio:.3f}")
print(f"Total Data Points: {total_count}")
print(f" -> % Fine (Smoke/Aerosol):   {(fine_count/total_count)*100:.1f}%")
print(f" -> % Coarse (Dust/Soil):     {(coarse_count/total_count)*100:.1f}%")

# Automatic Conclusion
if avg_ratio > 0.55:
    print("\nVERDICT: COMBUSTION / AEROSOL DOMINANT")
    print("The pollution is mostly fine particles. Likely sources: Boilers, Vehicles, Chemical Vents.")
elif avg_ratio < 0.45:
    print("\nVERDICT: DUST / MECHANICAL DOMINANT")
    print("The pollution is mostly coarse particles. Likely sources: Road Dust, Construction, Powder Handling.")
else:
    print("\nVERDICT: MIXED MODE")
    print("A complex mix of dust and smoke.")

# ==========================================
# 4. VISUALIZATION (The Histogram)
# ==========================================
plt.figure(figsize=(12, 6))

# Plot the distribution
sns.histplot(df['pm_ratio'], bins=50, kde=True, color='purple', alpha=0.4, element='step')

# Add Safety Zones
plt.axvline(x=0.6, color='red', linestyle='--', linewidth=2, label='Chemical/Smoke (>0.6)')
plt.axvline(x=0.4, color='green', linestyle='--', linewidth=2, label='Dust/Soil (<0.4)')
plt.axvline(x=median_ratio, color='black', linestyle='-', linewidth=3, label=f'Your Median ({median_ratio:.2f})')

plt.title('Analysis of Pollution Type: PM2.5 to PM10 Ratio', fontsize=16)
plt.xlabel('Ratio (0 = Pure Dust, 1 = Pure Smoke)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()

save_path = './plots/PM2.5vsPM10.png'
plt.savefig(save_path, dpi=300, bbox_inches='tight')

plt.show()