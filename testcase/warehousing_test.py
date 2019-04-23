from testcase.base_setup import BaseSetup
from interfaces.warehousing import *
import ddt
from utils.json_utils import get_json
from utils.decorator import desc
import unittest
'''
desc装饰起仅调用runner可用
如果想通过unittest运行，不能使用desc
解释：
    1. unittest默认会把__doc__赋值_testMethodDoc
    2. 通过unittest会比装饰器更早初始化
    3. _testMethodDoc的值不能在初始化前修改
    4. 在初始化后修改_testMethodDoc会导致崩毁（unitetest有验证）
'''
create_orde_data = get_json("ware_housing.json")["create_orde_data"]

@ddt.ddt
class warehousing_test(BaseSetup):

    @desc
    @ddt.data(*create_orde_data)
    def test_create_orde1(self,data):
        '''测试转运入库订单生成'''
        create_orde(json=data['data'])

    def test_chargeback1(self):
        '''取消转运订单：'''
        pass

    def test_update_logistics1(self):
        '''修改物流信息：'''
        pass

    def test_batch_update_logistics1(self):
        '''批量修改物流信息：'''
        pass

    def test_query_goods_cat_list1(self):
        '''查询所有转运商品分类：'''
        pass
