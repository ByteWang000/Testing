# 登录等返回信息

import requests


# 类
class loginAPI:
    # 初始化
    def __init__(self):
        self.url_verify="http://kdtx-test.itheima.net/api/captchaImage"
        self.url_login="http://kdtx-test.itheima.net/api/login"
    # 验证码
    def get_verify_code(self):
        return  requests.get(url=self.url_verify)
    # 登录
    def login(self,test_data):
        return requests.post(self.url_login,test_data)