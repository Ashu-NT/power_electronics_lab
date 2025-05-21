
import re
import pandas as pd
from typing import Tuple

def extract_channeldata_value(filename:str, pattern = None)-> Tuple[str, int]:
    """ Function returns the value which measurement was made and channel
    """
    if pattern is None:
        pattern = re.compile(r'.*?(CH\d+)_(\d+).csv$')
        
    match = pattern.search(filename)
    if not match:
        return None
    
    channel, value = match.group(1), int(match.group(2))
    return channel, value

# Function to process multiple files
def get_data_from_dataframe(df:pd.DataFrame,channel_name:str):
    
    time_data = df['TIME'].values
    voltage_data = df[channel_name].values

    return time_data,voltage_data