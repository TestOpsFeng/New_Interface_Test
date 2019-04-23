import requests
from utils.yaml_utils import get_api

login_url = get_api("login_url")
print("login_url: " + login_url)
data = {
    "appCode": "0000001952683880",
    "appSecret": "b9486ca7a8e84a8f863b3dfbd9e8c074",
    "currentTime": 1554199785083,
    "sign": "14a6f90464468c74363a08b7f050028e"
}

response = requests.post(login_url, json=data)
token = response.json()['data']['token']
print('token:',token)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Content-Type": "application/json;charset=UTF-8",
    "Authorization": token
}