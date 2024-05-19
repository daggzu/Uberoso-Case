import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
base_dir = 'C:/Users/Diego/Documents/github/Uberoso-Case'
data_path = f'{base_dir}/uberoso.csv'
season_path = f'{base_dir}/season.csv'
weather_path = f'{base_dir}/weather.csv'

data = pd.read_csv(data_path)
season = pd.read_csv(season_path)
weather = pd.read_csv(weather_path)

# Merge data
data = pd.merge(data, season, left_on='Season ID', right_on='Season ID', how='left')
data.rename(columns={'Season': 'Season Name'}, inplace=True)
data = pd.merge(data, weather, left_on='Weather ID', right_on='Weather ID', how='left')
data.rename(columns={'Weather': 'Weather Description'}, inplace=True)
data.drop(columns=['Season ID', 'Weather ID'], inplace=True)

# Data transformation
data[['Date', 'Time']] = data['Time Bucket'].str.split(' ', expand=True)
data.drop(columns=['Time Bucket'], inplace=True)
data['Date'] = pd.to_datetime(data['Date'])
data['Total Trips'] = data['App Trips'] + data['Outside App Trips']

# EDA and Analysis
print(data.describe())

# Distribution of Trips
plt.figure(figsize=(12, 6))
sns.histplot(data['App Trips'], bins=30, kde=True, color='blue', label='App Trips')
sns.histplot(data['Outside App Trips'], bins=30, kde=True, color='orange', label='Outside App Trips')
plt.legend()
plt.title('Distribution of App Trips and Outside App Trips')
plt.show()

# Total trips by date
plt.figure(figsize=(14, 7))
data.groupby('Date')['Total Trips'].sum().plot()
plt.title('Total Trips by Date')
plt.xlabel('Date')
plt.ylabel('Number of Trips')
plt.show()

# Trips on holidays vs non-holidays
plt.figure(figsize=(12, 6))
sns.boxplot(x='holiday', y='Total Trips', data=data)
plt.title('Total Trips on Holidays vs Non-Holidays')
plt.xlabel('Holiday')
plt.ylabel('Total Trips')
plt.show()

# Trips on working days vs non-working days
plt.figure(figsize=(12, 6))
sns.boxplot(x='workingday', y='Total Trips', data=data)
plt.title('Total Trips on Working Days vs Non-Working Days')
plt.xlabel('Working Day')
plt.ylabel('Total Trips')
plt.show()

# Trips by season
plt.figure(figsize=(12, 6))
sns.boxplot(x='Season Name', y='Total Trips', data=data)
plt.title('Total Trips by Season')
plt.xlabel('Season')
plt.ylabel('Total Trips')
plt.show()

# Trips by weather
plt.figure(figsize=(12, 6))
sns.boxplot(x='Weather Description', y='Total Trips', data=data)
plt.title('Total Trips by Weather')
plt.xlabel('Weather')
plt.ylabel('Total Trips')
plt.xticks(rotation=45)
plt.show()
