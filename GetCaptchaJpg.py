import requests
import time

def DownImage(i):
    sess = requests.Session()
    '''headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36",
        "Connection": "keep-alive"}'''
    url = "http://csujwc.its.csu.edu.cn/verifycode.servlet"
    image = sess.get(url).content
    with open("image" + str(i) + ".jpg", "wb") as f:
        f.write(image)


if __name__ == "__main__":
    # 获取10000张图片
    for i in range(10000):
        time.sleep(0.1) #防止对教务系统访问过于密集
        DownImage(i)