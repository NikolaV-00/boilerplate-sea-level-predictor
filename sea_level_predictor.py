import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
  # Read data from file
  df = pd.read_csv('epa-sea-level.csv')

  # Create scatter plot
  x = df['Year']
  y = df['CSIRO Adjusted Sea Level']
  fig, ax = plt.subplots(figsize=(6,6))
  ax = plt.scatter(x, y)

  
  # Create first line of best fit
  print(df['CSIRO Adjusted Sea Level'].min())
  slope, intercept, r_value, p_value, stderr = linregress(x, y)
  x_pred = pd.Series([i for i in range(1880, 2051)])
  y_pred = slope*x_pred + intercept
  plt.plot(x_pred, y_pred, 'r')


  # Create second line of best fit
  new_df = df.loc[df['Year'] >= 2000]
  new_x = new_df['Year']
  new_y = new_df['CSIRO Adjusted Sea Level']
  slope, intercept, r_value, p_value, stderr = linregress(new_x, new_y)
  x_pred2 = pd.Series([i for i in range(2000, 2051)])
  y_pred2 = slope*x_pred2 + intercept
  plt.plot(x_pred2, y_pred2, 'g')

  # Add labels and title
  plt.xlabel('Year')
  plt.ylabel('Sea Level (inches)')
  plt.title('Rise in Sea Level')
    
  # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()