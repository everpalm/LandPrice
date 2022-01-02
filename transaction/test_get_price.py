
#import pytest
from transaction.get_price import EvaluateHouse as EH
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class TestEvaluateHouse:
    def test_import_data(self): 
        MyHouse = EH('address','date').import_data()
        logger.debug(f'MyHouse = {MyHouse}')
        #print(f'Myhouse = {MyHouse}')
        print(MyHouse['編號'])
        print(MyHouse['屋齡'])
        print(MyHouse['建物移轉面積平方公尺'])
        print(MyHouse['建築完成日期'])
        print(MyHouse['總層數'])
        print(MyHouse['建物分層'])