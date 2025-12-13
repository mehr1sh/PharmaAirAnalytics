import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import calplot # You might need to install this: pip install calplot
# If calplot isn't available, we will build a heatmap manually using seaborn

# ==========================================
# 1. LOAD DATA
# ==========================================
df = pd.read_csv('./datasets/final_dataset.csv')
df['timestamp'] = pd.to_datetime(df['timestamp'])
df = df.set_index('timestamp')

# Resample to Daily Average for the Calendar
daily_df = df['pm25'].resample('D').mean()

# ==========================================
# 2. ANALYSIS A: CALENDAR HEATMAP (Manual Seaborn Build)
# ==========================================
# We build a grid: Weeks on Y-axis, Days on X-axis
print("Generating Calendar Heatmap...")

# Create helper columns
daily_data = pd.DataFrame(daily_df)
daily_data['weekday'] = daily_data.index.day_name()
daily_data['week'] = daily_data.index.isocalendar().week
daily_data['day_num'] = daily_data.index.day

# Pivot for Heatmap
# Note: This pivot depends on your specific month's data. 
# It creates a matrix where rows=Week Number, cols=Day Name
calendar_matrix = daily_data.pivot_table(index='week', columns='weekday', values='pm25')

# Reorder columns to be Mon-Sun
days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
calendar_matrix = calendar_matrix.reindex(columns=days_order)

plt.figure(figsize=(12, 5))
sns.heatmap(calendar_matrix, cmap='RdYlGn_r', annot=True, fmt=".0f", linewidths=1, linecolor='white')
plt.title('Calendar Heatmap: Average Daily PM2.5 (Red = High Pollution)', fontsize=14)
plt.xlabel('')
plt.ylabel('Week Number')
plt.tight_layout()
plt.show()