#!/usr/bin/python3
"""
Regression on a continuous dataset (stocks in this example)
y = m*x + b
"""
import pandas as pd
import quandl

# Features (attributes/continuous data) and labels
# Features are the attributes that make up the label
# Label is the prediction


# Don't worry - this is a junk key
data_frame = quandl.get('WIKI/GOOGL', authtoken="TMkJ5_yDWs5AwGje44vc")  # Ticker for stock on quandl.com

# Features for this dataset include: open, high, low, close, volume, etc.
#print(data_frame.head())

# Meaningful features are essential to machine learning
# Adjusted prices in this example are to account for stock splits
# Useless features will cause trouble for machine learning classifiers

# Grabbing features
data_frame = data_frame[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]

# Margin of High and Low shows stocks volatility
# Creating a new column for the percent volatility
data_frame['HL_PCT'] = (data_frame['Adj. High'] - data_frame['Adj. Low'])/data_frame['Adj. Close'] * 100.0
data_frame['PCT_CHG'] = (data_frame['Adj. Close'] - data_frame['Adj. Open'])/data_frame['Adj. Open'] * 100.0

# Defining a new dataframe
data_frame = data_frame[['Adj. Close', 'HL_PCT', 'PCT_CHG', 'Adj. Volume']]
print(data_frame.head())
