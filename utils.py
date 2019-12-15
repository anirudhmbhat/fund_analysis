import quandl
import pandas as pd
from config import *
import numpy as np

def replace_empty_values_drop_na(df):
    df.replace('', np.nan, inplace=True)
    df.dropna(inplace=True)
    return df

def string_strip(in_, character=' '):
    return in_.strip(character)

def get_fund_list(path):
    return pd.read_csv(path)

def get_data_from_csv(backup_data_path):
    fund_list = get_fund_list(fund_list_path)
    fund_names = list(map(string_strip, fund_list['fund_name'].to_string(
        header=False,
        index=False).split('\n')))
    print(fund_names)
    fund_names.append('Date')
    data = pd.read_csv(backup_data_path,
                       usecols=fund_names,
                       parse_dates=True)
    return data

def get_data_from_quandl():
    #get the list of funds I want data for from the file
    fund_list = get_fund_list(fund_list_path)
    #Separate the fund names and their identifiers
    fund_names = list(map(string_strip, fund_list['fund_name'].to_string(
        header=False,
        index=False).split('\n')))
    identifiers = list(map(string_strip, fund_list['fund_identifier'].to_string(
        header=False,
        index=False).split('\n')))
    identifiers = ['{}.1'.format(i.strip()) for i in identifiers]
    #Print the fund identifiers
    print('Fund identifiers: {}'.format(identifiers))
    pd.set_option('max_colwidth', 255)
    data = get_navs(identifiers,
                    fund_names,
                    auth_token,
                    date_to_fetch_data_from)
    #Take a backup since there are limited number of free api calls per account per time period
    data = replace_empty_values_drop_na(data)
    write_data_to_csv(data, backup_data_path)
    fund_names.append('Date')
    data = pd.read_csv(backup_data_path,
                       usecols=fund_names,
                       parse_dates=True)
    return data


def get_navs(fund_identifiers,
             fund_names,
             auth_token,
             start_date="2016-01-01"):
    try:
        #get fund returns with identifiers as col name
        fund = quandl.get(fund_identifiers,
                          authtoken=auth_token,
                          start_date=start_date)
        #Change col name to the appropriate fund name
        fund.columns = fund_names
        return fund
    except Exception as e:
        print(str(e))


# Write data to file to avoid hitting the api repeatedly
def write_data_to_csv(data_frame, path):
    data_frame.to_csv(path)
