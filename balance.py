import json
import requests
import time
import threading

ADDRESS_LIST = [
    {
        "name": "钱包1",
        "address": "1"
    },
    {
        "name": "钱包1",
        "address": "2"
    }
]

UUID = ""


class MonitorAddress:
    URL = "https://api-worker.noscription.org/indexer/balance?npub="

    # initialize initial balance
    def __init__(self, address, uuid):
        self.address = address.get("address")
        self.name = address.get("name")
        self.uuid = uuid
        # self.url = self.URL + self.address
        self.url = "http://127.0.0.1:1000/HTML/1.html"
        self.data = self.getBalance()
        self.result = None
        if self.data is not None:
            print("[Initial response]", self.name + ":" + self.data)
        else:
            print("Init false" + self.name)
            exit()

        self.time_check()  # 持续检查

    # Get_balance
    def getBalance(self):
        i = 64
        while i > 0:
            i -= 1
            try:
                response = requests.get(self.url)
                if response.status_code == 200:
                    data = response.text
                    return data
            except requests.RequestException as e:
                print(self.name + "[Request]error:", e)
                time.sleep(4)
        return None

    # check the change of balance
    def checkChange(self):
        self.result = self.getBalance()
        if self.result is None:
            print("Getting balance have encounter error.", self.result)
            exit()

        if self.result == self.data:
            print(self.name + "：Nothing have updated")
        else:
            text = self.name + "：", self.result + "{},{},{}".format(self.address, self.uuid, get_public_ip())
            self.data = self.result
            print(text)
            self.Notify(text)

    def Notify(self, text):
        url = "https://wxpusher.zjiecode.com/api/send/message/?appToken=AT_q354HXyreyvPfh1rTldQmQRAYKgG2fQs&content={}&uid={}".format(
            text, self.uuid)

        # 发送 GET 请求
        response = requests.get(url)
        # 检查响应
        if response.status_code == 200:
            print(self.name + "消息发送成功！")
        else:
            print(self.name + "消息发送失败，状态码：", response.status_code)

    def time_check(self):
        while 1:
            self.checkChange()
            time.sleep(5)


def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        if response.status_code == 200:
            public_ip = response.json()['ip']
            return public_ip
        else:
            return "None"
    except requests.RequestException:
        pass


if __name__ == '__main__':
    threads = []

    for _ in ADDRESS_LIST:
        thread = threading.Thread(target=MonitorAddress, args=(_, UUID))
        threads.append(thread)
        thread.start()

    # 主线程等待所有线程结束
    for thread in threads:
        thread.join()
