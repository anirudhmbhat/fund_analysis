import pandas as pd
from utils import *
import matplotlib.pyplot as plt
from config import *

pd.set_option('max_colwidth', 255)

# Fetch all the data into one dataframe and store in a file

#if run is true, hit quandl api and fetch data to store in csv for further runs,
#else read from csv and return data
def fetch_data(run):
    if run is True:
        data = get_data_from_quandl()
    elif run is False:
        data = get_data_from_csv()
    else:
        raise Exception(
            'Please set the fetch_data_flag to either True or False')
    return data

# Plot a graph of all the instruments to compare them
def compare_navs_by_graph(fund_info):
    # gca stands for 'get current axis'
    ax = plt.gca()
    ax.set_ylabel("Net asset value(NAV) in rupees")
    for column in fund_info.columns:
        if column != x_axis_col_name:
            fund_info.plot(kind='line',
                           x=x_axis_col_name,
                           y=column,
                           ax=ax,
                           title='Analysis of NAVs of Mutual Fund(s)')
    plt.show()

if __name__ == '__main__':
    data = fetch_data(fetch_data_flag)
    compare_navs_by_graph(data)
    exit(0)
