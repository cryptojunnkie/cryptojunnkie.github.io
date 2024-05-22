import numpy as np
import matplotlib.pyplot as plt
import yahoo_fin.stock_info as si
import matplotlib.dates as mdates
from datetime import date
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio

# Set the Plotly template to use the "plotly_white" theme
pio.templates.default = "plotly_white"

# Retrieve historical BTC price data up to the current date
btc_data = si.get_data("BTC-USD", start_date="04/19/2015", end_date=date.today(), index_as_date=True, interval="1d")

# Extract date and price data
x = btc_data.index
y = btc_data['close'].values

# Perform polynomial regression fit with increased degree for smoothing
polynomial_degree = 13  # Set the polynomial degree for regression
p = np.polyfit(mdates.date2num(x), y, polynomial_degree)
y_fit = np.polyval(p, mdates.date2num(x))

# Calculate the distances from the polynomial regression curve based on historical price levels
price_high = np.max(y_fit)
price_low = np.min(y_fit)

# Create the Plotly traces
trace1 = go.Scatter(x=x, y=y, mode='lines', name='BTC Price', line={'color': 'black', 'width': 0.75})
trace2 = go.Scatter(x=x, y=y_fit, mode='lines', name='Smoothed Polynomial Regression Curve', line={'color': 'red', 'width': 2})

# Create the additional channels
additional_traces = []
channel_distance = 5000  # $5,000 distance between channels

# Lower channel and upper channel color palettes
lower_channel_colors = ['#F1C40F', '#2ECC71', '#3498DB', '#9B59B6']
upper_channel_colors = ['#F39C12', '#16A085', '#8E44AD', '#E74C3C']

# Add annotations for each level
annotations = []
for i in range(4):
    lower_channel = y_fit - (i + 1) * channel_distance
    upper_channel = y_fit + (i + 1) * channel_distance
    additional_traces.append(go.Scatter(x=x, y=lower_channel, mode='lines', name=f'Buy Area {i+1}',
                                       line={'color': lower_channel_colors[i], 'width': 2, 'dash': 'solid'}))
    additional_traces.append(go.Scatter(x=x, y=upper_channel, mode='lines', name=f'TP {i+1}',
                                       line={'color': upper_channel_colors[i], 'width': 2, 'dash': 'solid'}))

    # Add annotations for lower channel levels
    annotations.append(
        go.layout.Annotation(
            x=x[-1],
            y=lower_channel,
            text=f"Buy Area {i+1}",
            showarrow=False,
            font=dict(color=lower_channel_colors[i], size=12)
        )
    )

    # Add annotations for upper channel levels
    annotations.append(
        go.layout.Annotation(
            x=x[-1],
            y=upper_channel,
            text=f"TP  {i+1}",
            showarrow=False,
            font=dict(color=upper_channel_colors[i], size=12)
        )
    )

# Create the layout
layout = go.Layout(
    title='Bitcoin HISTORICAL BUY & TAKE PROFIT LEVELS',
    xaxis_title='Date',
    yaxis_title='Price (USD)',
    yaxis_tickformat='${:,.2f}',
    xaxis_type='date',
    xaxis_rangeslider_visible=False,
    xaxis_zerolinewidth=1,
    yaxis_zerolinewidth=1,
    xaxis_showgrid=True,
    yaxis_showgrid=True,
    xaxis_gridwidth=1,
    yaxis_gridwidth=1,
    xaxis_gridcolor='lightgray',
    yaxis_gridcolor='lightgray',
    legend=dict(
        bgcolor='rgba(255, 255, 255, 0.5)',
        bordercolor='grey',
        borderwidth=1,
        x=0.01,
        y=0.99,
        orientation="v",
        font=dict(
            size=12
        ),
        traceorder="normal"
    ),
    margin=dict(l=50, r=50, t=50, b=50),
    dragmode='zoom',  # Set the dragmode to 'zoom'
    xaxis_fixedrange=False,
    yaxis_fixedrange=False,
    annotations=annotations
)

# Create the figure and save it as an HTML file
fig = go.Figure(data=[trace1, trace2, *additional_traces], layout=layout)

# Add the trend line
fig.add_trace(
    go.Scatter(
        x=x,
        y=y_fit,
        mode='lines',
        name='Trend Line',
        line={'color': 'blue', 'width': 2, 'dash': 'dash'}
    )
)

fig.update_layout(
    title_font_size=20,
    xaxis_title_font_size=16,
    yaxis_title_font_size=16,
    dragmode='zoom',  # Set the dragmode to 'zoom'
    xaxis_rangeslider_visible=False
)

fig.write_html('price_chart.html')
