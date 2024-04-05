import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(12, 6))
    plt.scatter(x=df["Year"], y=df["CSIRO Adjusted Sea Level"], s=10)

    # Create first line of best fit
    slope1, intercept1, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    plt.plot(list(range(df["Year"].iloc[0], 2051)), [slope1 * x + intercept1 for x in range(df["Year"].iloc[0], 2051)], '--', color='red', label='Line of Best Fit (All Data)')
    
    # Create second line of best fit
    slope2, intercept2, _, _, _ = linregress(df['Year'][df['Year'] >= 2000], df['CSIRO Adjusted Sea Level'][df['Year'] >= 2000])
    plt.plot(list(range(2000, 2051)), [slope2 * x + intercept2 for x in range(2000, 2051)], '--', color='green', label='Line of Best Fit (Since 2000)')

    # Add labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")

    #plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()