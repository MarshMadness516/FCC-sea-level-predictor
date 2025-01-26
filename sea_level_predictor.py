import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.scatter(data=df, x='Year', y='CSIRO Adjusted Sea Level', marker='.')
    
    # Create first line of best fit
    slope_all, intercept_all, _, _, _ = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    x_all = pd.Series([i for i in range(1880, 2051)])
    ax.plot(x_all, (slope_all * x_all + intercept_all), 'orange', label='Projection Using All Data')

    # Create second line of best fit
    df_after2k = df[df['Year'] >= 2000].copy(deep=True)
    slope_2k, intercept_2k, _, _, _ = linregress(x=df_after2k['Year'], y=df_after2k['CSIRO Adjusted Sea Level'])
    x_2k = pd.Series([i for i in range(2000, 2051)])
    ax.plot(x_2k, (slope_2k * x_2k + intercept_2k), 'red', label='Projection Using Data After 2000')

    # Add axis labels, plot title, and legend
    ax.set_title('Rise in Sea Level')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_xlabel('Year')
    ax.legend()
    
    # Save plot and return data for testing
    plt.savefig('sea_level_plot.png')
    return plt.gca()