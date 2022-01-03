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
    def __init__(self, str_district, str_address, str_year, str_quarter):
        self.str_district = str_district
        self.str_address = str_address
        self.str_year = str_year
        self.str_quarter = str_quarter
        self.df = pd.read_csv(f'transaction/f_lvr_land_a' + f'_{self.str_year}'+ f'{self.str_quarter}.csv',encoding='utf-8')

    def get_address(self):
        return self.str_address

    def get_district(self):
        return self.str_district

    def get_price(self):
        print(f'Fiscal Year = {self.str_year}{self.str_quarter}')
        target_df = self.df[(self.df['鄉鎮市區'] == self.str_district) & (self.df['土地位置建物門牌'].str.contains(self.str_address))]
        #df = pd.read_csv('transaction/f_lvr_land_a.csv',encoding='utf-8')
        #logger.debug(f'df = {df}' )
        print(target_df['土地位置建物門牌'])
        return target_df['總價元']
        ''' Refactor format of year, month and day '''
        #year_start = date_start[0:4]
        #month_start = date_start[4:6]
        #day_start = date_start[6:8]
        #year_end = date_end[0:4]
        #month_end = date_end[4:6]
        #day_end = date_end[6:8]