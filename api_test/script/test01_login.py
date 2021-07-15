# 导包
import unittest
from api.login import LoginApi


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.login_api =LoginApi.login()


    def tearDown(self):
        pass

    def test01_case001(self):
        pass