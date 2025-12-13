import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# CONFIGURATION
# ==========================================
FILE_PATH = './datasets/krrish_node.csv'  # Replace with your filename
OUTPUT_PATH = './datasets/cleaned_data.csv'

# Your specific "Wiggle" thresholds (Max allowed jump from the local median)
THRESHOLDS = {
    'pm25': 35.0,        # +/- 45 ug/m3
    'pm10': 35.0,        # +/- 45 ug/m3
    'temp_C': 3.0,       # +/- 3 Degrees
    'hum_percent': 5.0,  # +/- 5 %
    'nox_ppm': 1.0,      # +/- 1 ppm
    'co2_ppm': 100.0     # +/- 200 ppm
}

# Window size for the rolling filter 
WINDOW_SIZE = '15min'

df = pd.read_csv(FILE_PATH)

# Parse Time (expect format: YYYY-MM-DD HH:MM:SS)
df['timestamp'] = pd.to_datetime(df['millis'], format='%Y-%m-%d %H:%M:%S', errors='coerce')
# Inform the user if some timestamps could not be parsed
n_coerced = df['timestamp'].isna().sum()
if n_coerced > 0:
    print(f"Warning: {n_coerced} rows have unparsable timestamps and will be dropped.")
df = df.dropna(subset=['timestamp'])
df = df.sort_values('timestamp').drop_duplicates().reset_index(drop=True)
df = df.set_index('timestamp') # Index must be datetime for rolling logic
df = df.drop(columns=['millis'], errors='ignore')

initial_count = len(df)
print(f"Initial Data Points: {initial_count}")


physics_mask = (
    (df['temp_C'].between(-10, 60)) &
    (df['hum_percent'].between(0, 100)) &
    (df['co2_ppm'].between(350, 5000)) & 
    (df['nox_ppm'] >= 0) &
    (df['pm25'].between(0, 2000)) &  
    (df['pm10'].between(0, 3000))
)

df_physics = df[physics_mask].copy()
print(f"Removed by Physics Filter: {initial_count - len(df_physics)}")

def filter_by_rolling_deviation(df, col, window, limit):
    # Calculate local median
    rolling_median = df[col].rolling(window=window, center=True, min_periods=1).median()
    
    # Calculate difference
    diff = np.abs(df[col] - rolling_median)
    
    # Keep only points within the limit
    return diff <= limit

# Apply to all columns
mask_rolling = pd.Series(True, index=df_physics.index)

for col, limit in THRESHOLDS.items():
    if col in df_physics.columns:
        # Generate mask for this specific column
        col_mask = filter_by_rolling_deviation(df_physics, col, WINDOW_SIZE, limit)
        # Combine with main mask (Logic: must pass ALL checks)
        mask_rolling = mask_rolling & col_mask

df_final = df_physics[mask_rolling].copy()
print(f"Removed by Rolling Filter: {len(df_physics) - len(df_final)}")
print(f"Final Data Count: {len(df_final)}")


df_final.reset_index().to_csv(OUTPUT_PATH, index=False)
print(f"Saved cleaned data to: {OUTPUT_PATH}")

# Optional: Plot a small sample to show the User the difference
try:
    # Take a 2-hour slice where a spike might exist
    sample_start = df_final.index[0]
    sample_end = sample_start + pd.Timedelta(hours=4)
    
    raw_slice = df[sample_start:sample_end]
    clean_slice = df_final[sample_start:sample_end]

    plt.figure(figsize=(10, 5))
    plt.plot(raw_slice.index, raw_slice['pm25'], label='Raw (Noisy)', color='red', alpha=0.5)
    plt.plot(clean_slice.index, clean_slice['pm25'], label='Cleaned', color='green')
    plt.title("Cleaning Check: PM2.5 (First 4 Hours)")
    plt.legend()
    plt.ylabel("PM 2.5")
    plt.show()
    print("displayed plot check.")
except Exception as e:
    print("Could not generate plot (requires graphical environment).")