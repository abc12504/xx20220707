import requests
import pytest

s = requests.session()
print(s.headers)
print(s.cookies)

url = 'http://localhost:81/dev-api/login'
paload = {"username": "admin", "password": "admin123"}
h1 = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37",
    "isToken": "false",
    "Content-Type": "application/json;charset=UTF-8"
}


def test_1():
    res = s.post(url=url, headers=h1, json=paload)
    print(res.json())
    token = res.json()["token"]
    h2 = {
        "Authorization": "Bearer " + token
    }
    s.headers.update(h2)
    print(s.headers)
    assert res.json()['code'] == 200
    assert res.json()['msg'] == "操作成功"


url2 = 'http://localhost:81/dev-api/getInfo'
# res2 = s.get(url2)
# print(res2.json())

def test_2():
    res2 = s.get(url2)
    print(res2.json())
    assert res2.json()['code'] == 500
    assert res2.json()['msg'] == "操作成功"