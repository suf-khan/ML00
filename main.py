from sensor.exception import SensorException
import os 
import sys 

from sensor.logger import logging 

def test_exception(): 
    try: 
        #logging.info("testing for logging - will get an error")
        a=1/0
    except Exception as e: 
        logging.info("we entered the exception block for DivisionbyZero")
        raise SensorException(e, sys)   #passing sys module as a tool to then extract info regarding exceptions

if __name__ == "__main__": 
    try: 
        test_exception()
    except Exception as e: 
        print(e)