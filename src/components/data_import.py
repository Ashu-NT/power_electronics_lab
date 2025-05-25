
import pandas as pd
from typing import Tuple, Dict
from collections import defaultdict
import os
from IPython.display import display

from utils import extract_channeldata_value
from logger import logging
# Functions below are used to import data
# Please to verify the data and change the "skiprows" values accordingly

def import_simulation_data(file_path, skiprows=0) -> pd.DataFrame:
    """
    Import data from simulation software (e.g., LTSpice)
    """
    try:
        # Adjust column names and separator based on your file format
        data = pd.read_csv(file_path, sep='\t', skiprows=skiprows)
        logging.info(f"Successfully imported simulation data from {file_path}")
        display(data.head())
        return data
    except Exception as e:
        logging.info(f"Error importing simulation data: {e}")
        return None

def import_measurement_data(file_path, skiprows=20) -> pd.DataFrame:
    """
    Import data from measurement equipment (e.g., oscilloscope)
    """
    try:
        # Adjust column names and separator based on your file format
        data = pd.read_csv(file_path, sep=',', skiprows=skiprows)
        logging.info(f"Successfully imported measurement data from {file_path}")
        display(data.head())
        return data
    except Exception as e:
        logging.info(f"Error importing measurement data: {e}")
        return None
    
def get_multiple_oscilloscope_data_files(folder_path:str, pattern=None) ->  Tuple[ Dict[int,Dict[str,str]], int]: 
    """Functions get path of each .csv file from the oscilloscope
        Returnns Tuple : CH1 files path and CH2 files path 
    """
    data = defaultdict(dict)
    
    try:
        for root,_,files in os.walk(folder_path):
            for filename in files:
                if filename.endswith(".csv"):
                    file_path = os.path.join(root,filename)
                    
                    result = extract_channeldata_value(filename,pattern)
                    if result:
                        channel , value = result
                        data[value][channel] = file_path
        
        # Sort Dictionary                
        index = sorted(data.keys(),key=lambda x:int(x))
        
        return data, index
    except Exception as e:
        logging.info(f"Error Processing Multiple files: {e}")
        return None