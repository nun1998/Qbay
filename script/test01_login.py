# 导包
import app
import unittest
from api.login import LoginApi


# 构造数据
def build_data():
    sql = "select * from login"


class TestLogin(unittest.TestCase):

    # 前置处理
    def setUp(self):
        self.login_api = LoginApi()

    # 后置处理
    def tearDown(self):
        pass

    def test01_case001(self):
        # 调用登录接口
        response = self.login_api.login({"phone": "18725778441", "password":"f300fb7c100ad9792073f28da38423d8", 'grant_type': 'password'})
        # 断言
        self.assertEqual(200, response.status_code)

        # 获取token
        if response.status_code == 200:
            app.TOKEN = "Bearer " + response.json().get("access_token")
            app.header_data["Authorization"] = app.TOKEN