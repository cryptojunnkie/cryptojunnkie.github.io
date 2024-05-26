# update_data.py
import numpy as np
import yahoo_fin.stock_info as si
import matplotlib.dates as mdates
from datetime import date
import plotly.graph_objects as go
import plotly.io as pio

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

# Save the updated data (optional)
# You can save it to a file or a database for future reference

print("Data updated successfully!")
