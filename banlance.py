import json
import requests
import time
import threading

ADDRESS_LIST = {
    "",

}
UUID = ""


class MonitorAddress:
    URL = "https://api-worker.noscription.org/indexer/balance?npub="

    # initialize initial balance
    def __init__(self, address, uuid):
        self.address = address
        self.uuid = uuid
        self.url = self.URL + self.address
        self.data = self.getBalance()
        self.result = None
        if self.data is not None:
            print("[Initial response]", self.address[-8:] + ":" + self.data)
        else:
            print("Init false" + self.address[-8:])
            exit()

        self.time_check()  # 持续检查

    # Get_balance
    def getBalance(self):
        i = 10
        while i > 0:
            i -= 1
            try:
                response = requests.get(self.url)
                if response.status_code == 200:
                    data = response.text
                    return data
            except requests.RequestException as e:
                print(self.address[-8:] + "[Request]error:", e)
                time.sleep(1)
        return None

    # check the change of balance
    def checkChange(self):
        self.result = self.getBalance()
        if self.result is None:
            print("Getting balance have encounter error.", self.result)
            exit()

        if self.result == self.data:
            print(self.address[-8:] + "：Nothing have updated")
        else:
            text = self.address[-8:] + "【Monitoring change】The latest balance:", self.result
            self.data = self.result
            print(text)
            self.Notify(text)

    def Notify(self, text):
        url = "https://wxpusher.zjiecode.com/api/send/message/?appToken=AT_IqL2BKbwJ3VBP3UkIdah8pesiA3CwUGj&content={}&uid={}".format(
            text, self.uuid)

        # 发送 GET 请求
        response = requests.get(url)
        # 检查响应
        if response.status_code == 200:
            print(self.address[-8:] + "消息发送成功！")
        else:
            print(self.address[-8:] + "消息发送失败，状态码：", response.status_code)

    def time_check(self):
        while 1:
            self.checkChange()
            time.sleep(5)


if __name__ == '__main__':
    threads = []
    for _ in ADDRESS_LIST:
        thread = threading.Thread(target=MonitorAddress, args=(_, UUID))
        threads.append(thread)
        thread.start()

    # 主线程等待所有线程结束
    for thread in threads:
        thread.join()
