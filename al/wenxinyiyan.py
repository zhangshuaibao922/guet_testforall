"""
@FileName：wenxinyiyan.py\n
@Description：\n
@Author：Mr.Dc\n
@Time：2023/9/25 17:35\n
@Department：研发部\n
@Website：www.xxx.com\n
@Copyright：©2002-2023 guet_test有限公司
"""
import requests
import json

import traceback
def get_access_token():
    """
    使用 API Key，Secret Key 获取access_token，替换下列示例中的应用API Key、应用Secret Key
    """

    url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=80bu03KBNz0XeWYOQIUzfW2k&client_secret=XIfESQz6HqsYjvuut3wcAEZKzpMZre8x"

    payload = json.dumps("")
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json().get("access_token")


def answer(question: str) -> str:
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions?access_token=" + get_access_token()

    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": question

            }
        ]
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    # print(response.text)
    # print(type(response.text))
    return response.text


def main():
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions?access_token=" + get_access_token()

    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": "北京在哪"

            }
        ]
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    # print(response.text)
    # print(type(response.text))


if __name__ == '__main__':
    # 基于文心一言的错误处理推荐报告
    s=""
    try:
        a = 1 / 0
    except Exception as e:
        s=traceback.format_exc()
        print(traceback.format_exc())
    finally:
        z=answer(s)
        l = z.split(',')
        print(l[3])
    # while True:
    #     qs=input("输入问题：")
    #     s = answer(qs)
    #     l = s.split(',')
    #     # print(type(l))
    #     print(l[3])

    # print(type(s))
    # print(s)
