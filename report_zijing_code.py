import http.cookiejar as HC
import json
import os
import random
import re
import requests

temperature = str(36.0 + (random.randint(0, 4) / 10))  # change this as you wish


def load_info():
    with open("conf.ini") as rf:
        line = rf.readlines()
        user_name_ = line[0].strip().split("=")[1].strip()
        user_pass_ = line[1].strip().split("=")[1].strip()
    return user_name_, user_pass_


if os.getenv("USER_NAME") and os.getenv("USER_PASS"):
    print("User info found in env")
    user_name = os.getenv("USER_NAME")
    user_pass = os.getenv("USER_PASS")
else:
    user_name, user_pass = load_info()

session = requests.session()
session.cookies = HC.LWPCookieJar(filename="cookies")
try:
    session.cookies.load(ignore_discard=True)
except:
    pass

r = session.post("https://zijing.tsinghua.edu.cn/tp_jp/getToken")
if r.url != "https://zijing.tsinghua.edu.cn/tp_jp/getToken":
    r = session.post(f"https://id.tsinghua.edu.cn/do/off/ui/auth/login/check",
                     data={"i_user": user_name, "i_pass": user_pass, "i_captcha": ""})
    r = session.post(re.findall(r'(?<=window.location.replace\(").*(?="\);)', r.text)[0])
    r = session.post("https://zijing.tsinghua.edu.cn/tp_jp/getToken")
    print("Login succeeded!")
data = {"tw": temperature, "token": r.text}
headers = {"Content-Type": "application/json;charset=UTF-8"}
r = session.post("https://zijing.tsinghua.edu.cn/tp_jp/jp/temporary/confirmTw", headers=headers, data=json.dumps(data))

if r.ok:
    print(f"Report succeeded! ({temperature})")
else:
    print(f"Report failed with code {r.status_code}.")
