import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load cleaned data
df = pd.read_csv('data/cleaned_aircraft_maintenance.csv')

# Information
print("\n Data Info:")
print(df.info())

# Preview Rows
print("\n First 5 Rows:")
print(df.head())

# Descriptive Statistics
print("\n Descriptive Statistics:")
print(df.describe(include='all'))

# Visualizations Folder
os.makedirs("outputs/visualizations", exist_ok=True)

# Distrubution of Engine Type
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='engine_type')
plt.title("Engine Type Distribution")
plt.savefig("outputs/visualizations/engine_type_distribution.png")
plt.close()

# Correlation Heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(df.select_dtypes(include='number').corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.savefig("outputs/visualizations/correlation_heatmap.png")
plt.close()

# Box Plot: Cruise Speed by Engine Type
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='engine_type', y='vcruise')
plt.title('Box Plot of Cruise Speed by Engine Type')
plt.xlabel('Engine Type')
plt.ylabel('Cruise Speed')
plt.tight_layout()
plt.savefig('outputs/visualizations/boxplot_cruise_speed.png')
plt.close()

# Histogram: Maximum Altitude
plt.figure(figsize=(10, 6))
sns.histplot(df['hmax'], kde=True, bins=20, color='skyblue')
plt.title('Histogram of Maximum Altitude')
plt.xlabel('Max Altitude')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('outputs/visualizations/histogram_max_altitude.png')
plt.close()

# Box Plot: Max Altitude by Engine Type
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='engine_type', y='hmax')
plt.title('Maximum Altitude by Engine Type')
plt.xlabel('Engine Type')
plt.ylabel('Max Altitude')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('outputs/visualizations/boxplot_by_engine_type.png')
plt.show()

# Histogram: Maximum Speed Distribution
plt.figure(figsize=(8, 5))
sns.histplot(df['vmax'].dropna(), bins=20, kde=True, color='skyblue')
plt.title('Distribution of Maximum Speed')
plt.xlabel('Maximum Speed')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('outputs/visualizations/histogram_max_speed_distribution.png')
plt.show()

print("\n EDA Completed. Plots saved to outputs/visualizations/")
