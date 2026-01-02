from sensor.exception import SensorException
import os 
import sys 
from sensor.pipeline.training_pipeline import TrainPipeline
from sensor.logger import logging 
from sensor.utils2 import dump_csv_file_to_mongodb_collection

from  fastapi import FastAPI
from sensor.constant.application import APP_HOST, APP_PORT
from starlette.responses import RedirectResponse
from uvicorn import run 
from fastapi.responses import Response
from sensor.ml.model.estimator import ModelResolver,TargetValueMapping
from sensor.utils.main_utils import load_object
from fastapi.middleware.cors import CORSMiddleware
import os
from fastapi import FastAPI, File, UploadFile, Response
import pandas as pd
from sensor.constant.training_pipeline import SAVED_MODEL_DIR
import uvicorn

app = FastAPI()



origins = ["*"]
#Cross-Origin Resource Sharing (CORS) 
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/",tags=["authentication"])
async def  index():
    return RedirectResponse(url="/docs")





@app.get("/train")
async def train():
    try:

        training_pipeline = TrainPipeline()

        if training_pipeline.is_pipeline_running:
            return Response("Training pipeline is already running.")
        
        training_pipeline.run_pipeline()
        return Response("Training successfully completed!")
    except Exception as e:
        return Response(f"Error Occurred! {e}")
        




@app.get("/predict")
async def predict():
    try:

    # get data and from the csv file 
    # covert it into dataframe 

        df =None

        Model_resolver = ModelResolver(model_dir=SAVED_MODEL_DIR)
        if not Model_resolver.does_model_exist():
            return Response("Model is not available")
        
        best_model_path = Model_resolver.get_best_model_path()
        model= load_object(file_path=best_model_path)
        y_pred=model.predict(df)
        df['predicted_column'] = y_pred
        df['predicted_column'].replace(TargetValueMapping().reverse_mapping,inplace=True)


        # get the prediction output as you want 


    except  Exception as e:
        raise  SensorException(e,sys)



def main():
    try:
            
        training_pipeline = TrainPipeline()
        training_pipeline.run_pipeline()
    except Exception as e:
        print(e)
        logging.exception(e)



if __name__ == "__main__":

    uvicorn.run(app, host=APP_HOST,port=APP_PORT)





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


# if __name__=="__main__":
#     #file_path=r"C:\Users\khans\Desktop\ML00\aps_failure_training_set1.csv"
#     #database_name="mlproj"
#     #collection_name="sensor"
#     #dump_csv_file_to_mongodb_collection(file_path,database_name,collection_name)

#     training_pipeline = TrainPipeline()
#     training_pipeline.run_pipeline()
