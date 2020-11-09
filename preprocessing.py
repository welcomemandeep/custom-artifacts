import pandas as pd
import logging
import json

def run(data, configurations={},):
    #===========================================================================
    # This function is responsible to contain the preprocessing steps.
    # configurations :- Are a set of key value pair that the customer might want
    # to pass in the service. These configuration will be maintained at the 
    # metadata in service
    #===========================================================================
    logging.info(configurations)
    df = pd.DataFrame.from_dict(json.loads(data))
    df = df.fillna(0)
    return df