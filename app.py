import os

# 主文件位置
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)
# token
TOKEN = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJkYXRhIjp7ImlkIjoxMSwidXNlcl90eXBlIjoiY3VzdG9tZXIifSwidG9rZW5fdHlwZSI6ImFjY2VzcyIsImlhdCI6MTYyNjY2Njc4OSwiZXhwIjoxNjI2NzUzMTg5fQ.CtHQ8P8pKL8P5qEjfN7ibWz0XLbOZhbezTUOyCR4fyU"

# url地址
url = "https://jzk80vaqs7.execute-api.ap-northeast-1.amazonaws.com/dev_v2"

# 请求头数据
header_data ={
    "Content-Type": "application/json",
    "Authorization": TOKEN
}

PEPPER = "qbaytek2021"