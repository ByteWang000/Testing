from api.login import loginAPI

from api.coures import courseAPI
from api.contract import ContractAPI
# 创建测试类
class TestContractBusiness:
    # 初始化
    token = None
    # 前置处理
    def setup(self):
        # 实例化
        self.login_api=loginAPI()
        self.course_api=courseAPI()
        self.contract_api=ContractAPI()
    # 后置处理
    def tesrdown(self):
        pass

    # 登录成功
    def test01_login_success(self):
        # 获取验证码
        res_v = self.login_api.get_verify_code()
        print(res_v.status_code)
        print(res_v.json())
        uuid = res_v.json().get("uuid")

        # 登录
        login_data = {
            "username": "admin",
            "password": "HM_2023_test",
            "code": "2",
            "uuid": uuid
        }
        res_l = self.login_api.login(test_data=login_data)
        print(res_l.status_code)
        print(res_l.json())
        # 提取登录后的token
        TestContractBusiness.token=res_l.json().get("token")
    # 新增课程成功
    def test0_add_course(self):
        add_data={ "name": "测试开发提升课01", "subject": "6","price": 899,"applicablePerson": "2", "info": "测试开发提升课01"}
        response = self.course_api.url_add_course(test_data=add_data,token=TestContractBusiness.token)
        print(response.json())


    # 上传合同成功
    def test03_upload_contract(self):
        file = open("C:/Users/ByteWang/Downloads/03_资料/data/test.pdf","rb")
        response = self.contract_api.upload_contract(test_data=file,token=self.token)
        print(response.json())

    # 新增合同
    def test04_add_contract(self):
        add_data={ "name": "测试888", "phone": "13612345678",
                   "contractNo": "HT12312323", "subject": "6",
                   "courseId": " 99", "channel": "0",
                   "activityId": 77, "fileName": "xxx"}
        response = self.contract_api.add_contract(test_data=add_data,token=self.token)
