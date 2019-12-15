import subprocess
from config import *

def call_subprocess(list_of_commands):
    #list of commands will be like ['ls','-lrt']
    return subprocess.call(list_of_commands)

if fetch_data_flag:
    call_subprocess(['python','get_fund_data.py'])
if normalize_data_flag:
    call_subprocess(['python','normalize.py'])
