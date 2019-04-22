from interfaces.login import *
import requests
from utils.decorator import url

'''
把url和headers封装好，作为一个接口调用方法，testcase传入时，只关注传入的data/json
'''


@url(get_api("create-orde"))
def create_orde(url=None, data=None, json=None, **kwargs):
    '''转运入库订单生成'''
    r = requests.post(url, json=json, headers=headers)
    return r


@url(get_api("chargeback"))
def chargeback(url=None, data=None, json=None, **kwargs):
    '''取消转运订单'''
    r = requests.post(url, json=json, headers=headers)
    return r


@url(get_api("update-logistics"))
def update_logistics(url=None, data=None, json=None, **kwargs):
    '''修改物流信息'''
    r = requests.post(url, json=json, headers=headers)
    return r


@url(get_api("batch-update-logistics"))
def batch_update_logistics(url=None, data=None, json=None, **kwargs):
    '''批量修改物流信息'''
    r = requests.post(url, json=json, headers=headers)
    return r


@url(get_api("query-goods-cat-list"))
def query_goods_cat_list(url=None, data=None, json=None, **kwargs):
    '''查询所有转运商品分类'''
    r = requests.post(url, json=json, headers=headers)
    return r
