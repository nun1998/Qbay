# 导包
import requests
import app


# 创建接口类
class AddressAPI:
    # 初始化
    def __init__(self):
        # 添加收货地址
        self.url_add_address = app.url + "/add_customer_address/v2"
        # 查询所有收货地址
        self.url_get_address = app.url + "/get_customer_address_list/v2"

        # 删除收货地址
        self.url_delete_address = app.url + "/delete_customer_address/v2"

    # 添加收货地址
    def add_address(self, add_address_data):
        return requests.post(url=self.url_add_address, json=add_address_data, headers=app.header_data)

    # 查询收货地址
    def find_address(self, params):
        return requests.get(url=self.url_get_address, params=params, headers=app.header_data)

    # 删除收货地址
    def delete_address(self, address_id):
        return requests.post(url=self.url_delete_address, json=address_id, headers=app.header_data)
