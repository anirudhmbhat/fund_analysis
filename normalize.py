import pandas as pd
from utils import *
import matplotlib.pyplot as plt

pd.set_option('max_colwidth', 255)
#plt.style.use('fivethirtyeight')

# Plot a graph of all the instruments to compare them
def analyze_fund_variance_by_graph(fund_info):
    fund_info.plot(kind='line', colormap='Paired',x = 'Date',y = fund_info.columns.difference(['Date']))
    plt.show()

def normalize_data(data):
    for column in data.columns:
        if column != 'Date':
            data[column] = (data[column]-data[column].mean())/data[column].std()
    return data

if __name__ == '__main__':
    data = get_data_from_csv(backup_data_path)
    data = normalize_data(data)
    analyze_fund_variance_by_graph(data)
