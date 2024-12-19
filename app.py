import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load the dataset
url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
data = pd.read_csv(url)

# Clean and preprocess the data
data = data.drop(columns=['Province/State', 'Lat', 'Long'])
data = data.groupby('Country/Region').sum()

# Calculate total cases
total_cases = data.sum(axis=1)

# Plot the total cases by country
plt.figure(figsize=(12, 6))
total_cases.sort_values(ascending=False).head(10).plot(kind='bar')
plt.title('Top 10 Countries by Total COVID-19 Cases')
plt.xlabel('Country')
plt.ylabel('Total Cases')
plt.show()

# Time series analysis (for a specific country)
country_data = data.loc['India']  # Change 'India' to any country of choice
country_data.plot(figsize=(12, 6))
plt.title('COVID-19 Confirmed Cases in India Over Time')
plt.xlabel('Date')
plt.ylabel('Confirmed Cases')
plt.show()

# Interactive visualization using Plotly
fig = px.line(data_frame=data.transpose(), title='Global COVID-19 Confirmed Cases Over Time')
fig.show()
