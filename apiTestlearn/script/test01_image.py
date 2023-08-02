import requests as rq

# 发送请求
response = rq.get(url="http://kdtx-test.itheima.net/api/captchaImage")

print(response.status_code)
print("响应文本：",response.text)