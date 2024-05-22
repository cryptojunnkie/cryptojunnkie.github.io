# Your existing code (with both upper and lower bands)
import numpy as np
import matplotlib.pyplot as plt
import yahoo_fin.stock_info as si
import matplotlib.dates as mdates
from matplotlib.ticker import MultipleLocator
from datetime import date

# Retrieve historical BTC price data up to the current date
btc_data = si.get_data("BTC-USD", start_date="04/19/2015", end_date=date.today(), index_as_date=True, interval="1d")

# Extract date and price data
x = btc_data.index
y = btc_data['close'].values

# Perform polynomial regression fit with increased degree for smoothing
polynomial_degree = 13
p = np.polyfit(mdates.date2num(x), y, polynomial_degree)
y_fit = np.polyval(p, mdates.date2num(x))

# Calculate the distances from the polynomial regression curve based on historical price levels
price_high = np.max(y_fit)
price_low = np.min(y_fit)

# Define distinct color palettes for the lines using RGB colors
colors = [(0.6, 0.3, 0.8), (0.1, 0.5, 0.9), (0.4, 0.6, 0.2), (0.9, 0.7, 0.1),
          (0.7, 0.2, 0.5), (0.3, 0.8, 0.6), (0.8, 0.5, 0.1), (0.2, 0.4, 0.7)]

# Plot the original BTC price data, polynomial regression curve, and the bands
fig, ax = plt.subplots(figsize=(12, 6))

# Plot lines below and above the polynomial regression curve
for i in range(4):
    distance_below = 0.07 * (price_high - price_low) * (i + 1)
    distance_above = 0.07 * (price_high - price_low) * (i + 1)
    lower_band_line = ax.plot(x, y_fit - distance_below, alpha=0.8, linestyle='-', color=colors[i], linewidth=2, zorder=1)
    upper_band_line = ax.plot(x, y_fit + distance_above, alpha=0.8, linestyle='-', color=colors[i + 4], linewidth=2, zorder=1)

# Plot the original BTC price data with reduced line width
price_plot, = ax.plot(x, y, label='BTC Price', color='black', zorder=2, linewidth=0.75)

# Plot the polynomial regression curve behind the price line
regression_plot = ax.plot(x, y_fit, color='red', linestyle='-', linewidth=2, label='Smoothed Polynomial Regression Curve', zorder=1)

# Format y-axis tick labels based on the magnitude of the value
if price_high > 0.01:
    ax.yaxis.set_major_formatter('${x:,.2f}')  # Use whole value number and 2 decimal places to the left of the decimal
    ax.yaxis.set_major_locator(MultipleLocator(5000))  # Set y-axis price interval to the nearest 500
else:
    ax.yaxis.set_major_formatter('${x:,.2f}')  # Use all place values to the right of the decimal for price

plt.title('Bitcoin HISTORICAL BUY & TAKE PROFIT LEVELS', fontsize=12, fontweight='bold', ha='center')
plt.xlabel('Date')
plt.ylabel('Price (USD)')

# Move the legend to the upper left corner
ax.legend(loc='upper left')

# Customize the x-axis to display dates
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.xticks(rotation=45)

# Enable freehand drawing with LassoSelector
lasso = LassoSelector(ax, onselect=None)

# Function to handle drawing selection
def onselect(verts):
    print(f"Selected vertices: {verts}")  # Process the selected vertices as needed

# Connect the freehand drawing function
lasso.onselect = onselect

# Function to tether the comment container to the price line (with dollar sign added)
mplcursors.cursor(price_plot, hover=True).connect("add", lambda sel: sel.annotation.set_text(
    f'Price: ${sel.target[1]:.10f}\nDate: {mdates.num2date(sel.target[0]).strftime("%Y-%m-%d")}'))

# Display the plot
plt.grid(True)
plt.tight_layout()
plt.show()


# Save the plot as an HTML file
fig.write_html('index.html')

# Display a message indicating successful file creation
print("HTML file 'index.html' has been created.")
