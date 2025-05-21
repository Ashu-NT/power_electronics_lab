import pandas as pd
from typing import Dict


from logger import logging
from utils import get_data_from_dataframe
from components.data_import import import_measurement_data


#Function to process single data
def process_sim_data(data:pd.DataFrame) -> pd.DataFrame:
    """Process data according to tasks demands
        returns clean data 
    """
    return data


#Function to process single data
def process_single_csv(data:pd.DataFrame) -> pd.DataFrame:
    """Process data according to tasks demands
        returns clean data 
    """
    return data



def process_multiple_csv(data:dict,value:list) -> Dict[int,Dict[str,str]]:
    
    output = {}
    try:
        for index in value:
            if 'CH1' in data[index] and 'CH2' in data[index]:
                
                # Get file path from dictionary
                ch1_file_path = data[index]['CH1'] 
                ch2_file_path = data[index]['CH2'
                                            ]
                # Read file data
                ch1_data = import_measurement_data(ch1_file_path)
                ch2_data = import_measurement_data(ch2_file_path)
                
                # get values from dataframe
                ch1_col_1, ch1_col_2 = get_data_from_dataframe(ch1_data,"CH1")
                ch2_col_1, ch2_col_2 = get_data_from_dataframe(ch2_data,"CH2")
                
                output[index] = {
                'ch1_col_1': ch1_col_1,
                'ch1_col_2': ch1_col_2,  
                'ch2_col_1': ch2_col_1,
                'ch2_col_2': ch2_col_2   
            }
                    
    except Exception as e:
        logging.info(f"Error processing multiple csv data: {str(e)}")
        
    if not output:
        return None
    
    return output