from sensor.exception import SensorException
import os 
import sys 
from sensor.pipeline.training_pipeline import TrainPipeline
from sensor.logger import logging 
from sensor.utils2 import dump_csv_file_to_mongodb_collection


# def test_exception(): 
#     try: 
#         #logging.info("testing for logging - will get an error")
#         a=1/0
#     except Exception as e: 
#         logging.info("we entered the exception block for DivisionbyZero")
#         raise SensorException(e, sys)   #passing sys module as a tool to then extract info regarding exceptions

# if __name__ == "__main__": 
#     try: 
#         test_exception()
#     except Exception as e: 
#         print(e)"


if __name__=="__main__":
    #file_path=r"C:\Users\khans\Desktop\ML00\aps_failure_training_set1.csv"
    #database_name="mlproj"
    #collection_name="sensor"
    #dump_csv_file_to_mongodb_collection(file_path,database_name,collection_name)

    training_pipeline = TrainPipeline()
    training_pipeline.run_pipeline()
