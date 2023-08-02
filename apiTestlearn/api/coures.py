# 课程模块接口封装：

# 接口信息：
# URL：http://kdtx-test.itheima.net/api/clues/course
# 方法：Post
# 请求数据：
# 请求头：{ "Content-Type ": "application/json ", "Authorization": "xxx " }
# 请求体：{ "name": "测试开发提升课01", "subject": "6","price": 899,"applicablePerson": "2", "info": "测试开发提升课01"}
import requests


class courseAPI:
    # 初始化
    def __init__(self):
        self.url_add_course = "http://kdtx-test.itheima.net/api/clues/course"

    # 课程添加
    def add_course(self, test_data, token):
        return requests.post(self.url_add_course, json=test_data, headers={"Authorization": token})
