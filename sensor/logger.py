import logging 
import os 
import sys
from datetime import datetime 

LOG_FILE= f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

logs_path= os.path.join(os.getcwd(),"logs")

os.makedirs(logs_path, exist_ok=True)
LOG_FILE_PATH=os.path.join(logs_path, LOG_FILE)



logging.basicConfig(
    filename= LOG_FILE_PATH, #log messages will be written here 
    format= "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
                            #defines how each message will look like 
    level= logging.INFO, #sets the mininmum severity level for logging 
                         #debug->info->warning->error->critical
                         #in this case ignores debug and logs all others
)