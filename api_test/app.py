import os

# 主文件位置
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# token
TOKEN = ""

# url地址
url = "https://jzk80vaqs7.execute-api.ap-northeast-1.amazonaws.com/dev_v2"

# 请求头数据
header_data ={
    "Content-Type": "application/json",
    "Authorization": TOKEN
}