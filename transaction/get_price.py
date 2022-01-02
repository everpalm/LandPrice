import requests
import pandas as pd
from datetime import datetime
import json
import sys
import codecs
from time import sleep
import matplotlib.pyplot as plt

import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class EvaluateHouse:
    def __init__(self, str_district, str_date):
        self.str_district = str_district
        self.str_date = str_date

    #def get_address(self):
    #    return self.str_address

    #def get_date(self):
    #    return self.str_date

    def import_data(self):
        df = pd.read_csv('transaction/f_lvr_land_a.csv',encoding='utf-8')            
        logger.debug(f'df = {df}' )
        
        return df
        ''' Refactor format of year, month and day '''
        #year_start = date_start[0:4]
        #month_start = date_start[4:6]
        #day_start = date_start[6:8]
        #year_end = date_end[0:4]
        #month_end = date_end[4:6]
        #day_end = date_end[6:8]