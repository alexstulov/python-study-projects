import matplotlib.pyplot as plt
import locale
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'])
df = df.set_index('date')

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

def draw_line_plot():
    df_line = df.copy()
    # Draw line plot
    fig, ax = plt.subplots(figsize=(32,10), dpi=100)
    sns.lineplot(data=df_line,legend=False)
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.strftime('%B')
    df_bar = pd.DataFrame(df_bar.groupby(['year', 'month'])['value'].mean().round().astype('int'))
    
    # Draw bar plot
    months_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    bar = sns.catplot(
        data=df_bar,
        kind='bar',
        x='year',
        y='value',
        hue='month',
        hue_order=months_order,
        palette='tab10',
        legend_out=False, 
        facet_kws={"despine": False}
    )
    bar.set_axis_labels('Years','Average Page Views')
    fig = bar.fig

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # fix months amount not fit months order 'cause filled with local month names
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    fig, axes = plt.subplots(1,2, figsize=(32,10))
    
    # Draw box plots (using Seaborn)
    sns.boxplot(
        ax=axes[0],
        data=df_box,
        x='year',
        y='value',
        fliersize=1
    )
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')
    months_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    box = sns.boxplot(data=df_box,
        ax=axes[1],
        x='month',
        y='value',
        fliersize=1,
        order=months_order
    )
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')
    
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
