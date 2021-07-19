# 导包
import app
import unittest
from api.address import AddressAPI


# 创建测试类
class TestAddress(unittest.TestCase):

    address_id = None

    # 前置处理
    def setUp(self):
        self.address_api = AddressAPI()

    # 后置处理
    def tearDown(self):
        pass

    # 定义测试类
    def test01_add_address(self):
        add_address_data = {
            "name": "nun",
            "phone_region": "86",
            "shipping_address": "成都",
            "shipping_phone": "12345678900",
            "latitude": "30",
            "longitude": "120"
        }

        response = self.address_api.add_address(add_address_data)
        # 断言
        self.assertEqual(200, response.status_code)
        # 提取员工信息
        TestAddress.address_id = response.json().get("id")

    # test02
    def test02_find_address(self):
        params = {
            "limit": 10,
            "offset": 1
        }
        response = self.address_api.find_address(params)
        self.assertEqual(200, response.status_code)

    def test03_delete_address(self):
        if TestAddress.address_id:
            address_data ={
                "shipping_address_id": TestAddress.address_id
            }
            response = self.address_api.delete_address(address_data)
            self.assertEqual(200, response.status_code)
