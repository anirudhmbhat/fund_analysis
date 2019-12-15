import pandas as pd
from config import *
from utils import *
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

#plt.style.use('fivethirtyeight')

pd.set_option('max_colwidth', 255)

def process_log_returns(data):
    data = data[data.columns.difference(['Date'])]
    returns = data.pct_change()
    #log_returns = np.log(1+returns)
    # return log_returns
    return returns

def analyze_fund_variance_by_graph(fund_info):
    fund_info.plot(kind='bar',stacked=False,y = fund_info.columns.difference(['Date']))
    plt.show()

if __name__ == '__main__':
    data = get_data_from_csv(backup_data_path)
    tmp = data['Date'].copy(deep=True)
    data['Date'] = pd.to_datetime(data['Date'])
    data = data.loc[(data['Date'] >= (datetime.now() - timedelta(days = 365)))]
    log_returns = process_log_returns(data)
    log_returns = log_returns.join(tmp)
    log_returns = replace_empty_values_drop_na(log_returns)
    write_data_to_csv(log_returns,backup_log_data_path)
    log_data = get_data_from_csv(backup_log_data_path)

    # timeline = pd.DatetimeIndex(start=str(log_data['Date'].min()), freq='D', periods=len(log_data.index))
    # # print(timeline)
    # # log_data['Date'] = timeline
    log_data.set_index('Date', inplace=True)
    # print(log_data.head())
    analyze_fund_variance_by_graph(log_data)
