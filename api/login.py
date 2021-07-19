# 导包
import requests
import app


# 创建接口类
class LoginApi:
    # 初始化
    def __init__(self):
        self.url = app.url + "/sign_in/v2"

    # 定义接口调用方法
    def login(self, login_data):
        return requests.post(url=self.url, json=login_data)
