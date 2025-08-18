import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import io
import json
import time
import joblib
import logging
import threading
import pandas as pd
import threading
from collections import OrderedDict

from app import Config
from app.sensors.cod import prediction_cod, prediction_cod_multiline
from app.sensors.bod import prediction_bod
from app.utils import (data_cleaning,
                       load_model, 
                       send_result_prediction, 
                       convert_to_dataframe,
                       load_and_convert,
                       merge_data,
                       process_data,) 

# Initial configuration
config = Config()

# Constants
FEATURE_NAME = "data_meter"
QUEUE_NAME_COD = "cod_data_prediction"
QUEUE_NAME_BOD = "bod_data_prediction"

# RabbitMQ configuration
RABBITMQ_URL = config.RABBITMQ_URL

# Example data
json_data_1 = '''
{
    "data_meter":
    [
        {
            "timestamp": "2024-01-02 02:00:00",
            "TSS": 6000,
            "do": 1,
            "pH": 7
        }
    ] 
} 
'''

json_data_2 = '''
{
    "data_meter":
    [
        {
            "Timestamp": "2024-01-02 02:00:00",
            "TSS": 700,
            "Flow": 300,
            "pH": 6
        }
    ] 
}
'''   


def prediction_cod_main():
    try:
        # data = data_meter()
        data_dict = json.loads(json_data_1)
        data = data_dict
        if FEATURE_NAME in data:
            try:
                df = convert_to_dataframe(data, FEATURE_NAME)
                df = data_cleaning(df)
                df.columns = df.columns.str.lower()
                
                # Load model and scalers
                model_path_cod = config.get_model_path("cod")
                model, scaler_X, scaler_y = load_model(model_path_cod)
                
                # Prediction
                result = prediction_cod(model, scaler_X, scaler_y, df)
                if result is None:
                    logging.error("Prediction failed, skipping result processing.")
                    return
                predictions, log_prediction = result
                logging.info(f"Prediction COD: \n{log_prediction}")
                
                # Send results
                # send_result_prediction(QUEUE_NAME_COD, predictions, RABBITMQ_URL)
            except Exception as e:
                logging.error("An error occurred during prediction: %s", e)
        else:
            logging.warning(f"'{FEATURE_NAME}' key not found in the fetched data.")
                
    except KeyboardInterrupt:
        print("App stopped by user.")
        
    except Exception as e:
        logging.error("An error occurred during run app: %s", e)
    
        
    
def run_prediction_cod_multiline():
    try:
        # data = data_meter()
        
        df = process_data(json_data_1, json_data_2)
        df.columns = df.columns.str.lower()
        
        # Load model and scalers
        model_path_cod = config.get_model_path("cod_multiline")
        model, scaler_X, scaler_y = load_model(model_path_cod)
        
        # Prediction
        result = prediction_cod(model, scaler_X, scaler_y, df) 
        if result is None:
            logging.error("Prediction failed, skipping result processing.")
            return
        predictions, log_prediction = result
        logging.info(f"Prediction COD: \n{log_prediction}")
        
        # Send results
        # send_result_prediction(QUEUE_NAME_COD, predictions, RABBITMQ_URL)
                
    except KeyboardInterrupt:
        print("App stopped by user.")
        
    except Exception as e:
        logging.error("An error occurred during run app: %s", e)
           
def prediction_cod_multiline_v2():
    try:
        # data = data_meter()
        data_dict = json.loads(json_data_1)
        data = data_dict
        if FEATURE_NAME in data:
            try:
                df = convert_to_dataframe(data, FEATURE_NAME)
                df = data_cleaning(df)
                df.columns = df.columns.str.lower()
                
                # Load model and scalers
                model_path_cod = config.get_model_path("cod_multiline")
                model, scaler_X, scaler_y = load_model(model_path_cod)
                
                # Prediction
                result = prediction_cod(model, scaler_X, scaler_y, df)
                if result is None:
                    logging.error("Prediction failed, skipping result processing.")
                    return
                predictions, log_prediction = result
                logging.info(f"Prediction COD: \n{log_prediction}")
                
                # Send results
                # send_result_prediction(QUEUE_NAME_COD, predictions, RABBITMQ_URL)
            except Exception as e:
                logging.error("An error occurred during prediction: %s", e)
        else:
            logging.warning(f"'{FEATURE_NAME}' key not found in the fetched data.")
                
    except KeyboardInterrupt:
        print("App stopped by user.")
        
    except Exception as e:
        logging.error("An error occurred during run app: %s", e)

if __name__ == "__main__":
    prediction_cod_main()
    # run_prediction_cod_multiline()
    # prediction_cod_multiline_v2()