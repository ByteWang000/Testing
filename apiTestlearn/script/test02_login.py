import requests

url = "http://kdtx-test.itheima.net/api/login"
header_data = {
    "Content-Type": "application/json"
}
login_data = {
    "username": "admin",
    "password": "HM_2023_test",
    "code": "2",
    "uuid": "5efe7d741d674350a9da9451f20deb9c"
}
response = requests.post(url=url, headers=header_data, json=login_data)

print(response.status_code)
print(response.text)
