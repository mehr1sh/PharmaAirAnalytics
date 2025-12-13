import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


file_path = './datasets/final_dataset.csv'  # Using your cleaned file
df = pd.read_csv(file_path)

# Ensure Time is the Index
df['timestamp'] = pd.to_datetime(df['timestamp'])
df = df.set_index('timestamp')


df['Hour'] = df.index.hour

# Calculate the Mean (Average) for each hour across the whole month
hourly_avg = df.groupby('Hour')[['pm25', 'pm10', 'nox_ppm', 'co2_ppm', 'hum_percent']].mean()


print("--- Average Hourly Values ---")
print(hourly_avg.round(2)) # Rounded to 2 decimal places for readability

plt.figure(figsize=(14, 8))

# We normalize the data (0 to 1) just for the plot so trends are comparable
# Formula: (Value - Min) / (Max - Min)
normalized_df = (hourly_avg - hourly_avg.min()) / (hourly_avg.max() - hourly_avg.min())

# Plotting
sns.lineplot(data=normalized_df, linewidth=2.5)

# Decoration
plt.title('Diurnal Cycle: Normalized Daily Trends (0-23 Hours)', fontsize=16)
plt.xlabel('Hour of Day', fontsize=12)
plt.ylabel('Normalized Intensity (0 = Daily Low, 1 = Daily High)', fontsize=12)
plt.xticks(range(0, 24)) # Show every hour mark
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(title='Parameters', loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=6)

plt.tight_layout()

save_path = './plots/diurnal_plot.png'
plt.savefig(save_path, dpi=300, bbox_inches='tight')
print(f"Saved plot to {save_path}")

plt.show()