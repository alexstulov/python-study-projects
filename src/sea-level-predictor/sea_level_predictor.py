import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def generate_data(start_year, end_year, slope, intercept):
    data = {
        'x': [],
        'y': []
    }
    for year in range(start_year, end_year+1):
        data['x'] = [year for year in range(start_year, end_year+1)]
        data['y'] = [slope * year + intercept for year in range(start_year, end_year+1)]
    return data

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Create first line of best fit
    all_data_regression = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    data = generate_data(df['Year'].min(), 2050, all_data_regression.slope, all_data_regression.intercept)
    plt.plot(data['x'], data['y'], 'r')

    # # Create second line of best fit
    start_year = 2000
    end_year = 2050
    data_regression_2000_plus = linregress(df.loc[df['Year'] >= start_year]['Year'], df.loc[df['Year'] >= start_year]['CSIRO Adjusted Sea Level'])
    data = generate_data(start_year, end_year, data_regression_2000_plus.slope, data_regression_2000_plus.intercept)
    plt.plot(data['x'], data['y'], 'g')
    
    # # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
