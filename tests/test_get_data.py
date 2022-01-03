
#import pytest
from transaction.get_data import EvaluateHouse as EH
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class TestEvaluateHouse:
    def test_get_price(self): 
        MyPrice = EH('土城區','學成路１１９號九樓','2021', 'Q3').get_price()
        #logger.debug(f'MyHouse = {MyHouse}')
        print(f'MyPrice = {MyPrice}')
        #print(type(MyPrice))
        #assert MyPrice['總價元'] == '2368000'
        #print(MyHouse['屋齡'])
        #print(MyHouse['建物移轉面積平方公尺'])
        #print(MyHouse['建築完成日期'])
        #print(MyHouse['總層數'])
        #print(MyHouse['建物分層'])