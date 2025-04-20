📦 1. Import and Load Data 
python CopyEdit 
import pandas as pd 
 
# Load CSV file 
df = pd.read_csv("csv.csv") 
 
# Convert to datetime 
df['Datetime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'], dayfirst=True) 
df.set_index('Datetime', inplace=True) 
 
 
python CopyEdit 
import matplotlib.pyplot as plt 
 
# Attacks per day 
attacks_per_day = df.resample('D').size() 
 
plt.figure(figsize=(10, 5)) attacks_per_day.plot(marker='o') plt.title('Number of Attacks Per Day') plt.xlabel('Date') plt.ylabel('Attack Count') plt.grid(True) plt.tight_layout() plt.show() 
 
 
python CopyEdit 
attacks_per_hour = df.resample('H').size() 
 
plt.figure(figsize=(10, 5)) attacks_per_hour.plot(color='green') plt.title('Number of Attacks Per Hour') plt.xlabel('Datetime') plt.ylabel('Attack Count') plt.grid(True) plt.tight_layout() plt.show() 
 
 
python 
CopyEdit 
attack_type_counts = df['Attack Type'].value_counts() 
 
plt.figure(figsize=(8, 8)) 
attack_type_counts.plot.pie(autopct='%1.1f%%', startangle=140) plt.title('Attack Type Distribution') plt.ylabel('') plt.tight_layout() plt.show() 
  
python CopyEdit 
country_counts = df['Country'].value_counts() 
 
plt.figure(figsize=(10, 6)) 
country_counts.plot(kind='bar', color='tomato') plt.title('Top Attacking Countries') plt.xlabel('Country') plt.ylabel('Attack Count') plt.xticks(rotation=45) plt.tight_layout() plt.show() 
 
🌍 Optional – World Map of Attacking Countries (if you want fancier plots) 
python CopyEdit 
import plotly.express as px 
 
# Prepare data 
country_counts_df = df['Country'].value_counts().reset_index() country_counts_df.columns = ['Country', 'Attacks'] 
 
# Choropleth map fig = px.choropleth(     country_counts_df,     locations='Country',     locationmode='country names',     color='Attacks',     color_continuous_scale='Reds',     title='Global Attack Sources' 
) fig.show() 
 
