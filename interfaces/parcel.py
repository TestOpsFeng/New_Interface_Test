from interfaces.login import *
import requests
from utils.decorator import url

'''
把url和headers封装好，作为一个接口调用方法，testcase传入时，只关注传入的data/json
'''


@url(get_api("parcel_delivery_list"))
def parcel_delivery_list(url=None, data=None, json=None, **kwargs):
    '''提交包裹可用线路查询'''
    r = requests.post(url, json=json, headers=headers)
    return r


@url(get_api("query_packages"))
def query_packages(url=None, data=None, json=None, **kwargs):
    '''物流订单列表-分页'''
    r = requests.post(url, json=json, headers=headers)
    return r


@url(get_api("parcel_create"))
def parcel_create(url=None, data=None, json=None, **kwargs):
    '''提交物流订单'''
    r = requests.post(url, json=json, headers=headers)
    return r


@url(get_api("calculate_item_volume_weight"))
def calculate_item_volume_weight(url=None, data=None, json=None, **kwargs):
    '''包裹估算重量'''
    r = requests.post(url, json=json, headers=headers)
    return r


@url(get_api("calculate_delivery_cost"))
def calculate_delivery_cost(url=None, data=None, json=None, **kwargs):
    '''包裹估算运费'''
    r = requests.post(url, json=json, headers=headers)
    return r


@url(get_api("parcel_trace"))
def parcel_trace(url=None, data=None, json=None, **kwargs):
    '''包裹轨迹查询'''
    r = requests.post(url, json=json, headers=headers)
    return r


@url(get_api("parcel_detail"))
def parcel_detail(url=None, data=None, json=None, **kwargs):
    '''包裹详情查询'''
    r = requests.post(url, json=json, headers=headers)
    return r
