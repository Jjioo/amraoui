from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/data', methods=['POST'])

def get_data():
    a ="PCDA3ONEEZILT3CN"
    stock_name = request.form['stock_name']
    api_key = os.getenv(a)
    ts = TimeSeries(key=api_key, output_format='pandas')
    data, meta_data = ts.get_daily(symbol=stock_name, outputsize='full')
    data.reset_index(inplace=True)
    data.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
    data['Date'] = pd.to_datetime(data['Date']).dt.date
    return render_template('data.html', stock_name=stock_name, data=data)


if __name__ == '__main__':
    app.run()
