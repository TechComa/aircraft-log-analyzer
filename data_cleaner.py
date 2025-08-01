import pandas as pd

#Load raw dataset
df = pd.read_csv(r'C:\Users\junie\Aircraft_Engine_Maintenance_final.csv')


print("Initial Preview:")
print(df.head())
print(df.info())
print(df.describe())


#Checking for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Drop unnecessary columns
columns_to_drop = ['Company', 'Model', 'ROC (One)', 'Slo', 'Sl', 'THR']
df.drop(columns=columns_to_drop, inplace=True)

# Standardize column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
df['multi_engine'].fillna('Unknown', inplace=True) # Keeping Column NaN makes up 55% of Data, Need for Analysis
df['hmax_one'].fillna('Unknown', inplace=True) # Keeping Column NaN makes up 57% of Data, Need for Analysis
print("Updated Column names:")
print(df.columns.tolist())


# Preview Cleaned data
print("\n Preview of Cleaned Data:")
print(df.head())

# Save Cleaned Data
df.to_csv('data/cleaned_aircraft_maintenance.csv', index=False)
print("\n 'Cleaned data saved to data/cleaned_aircraft_maintenance.csv'")





