import urllib.request
import gevent
import re
from gevent import monkey

# 打补丁
monkey.patch_all()


def download(img_name, img_url):
    # 读取图片内容并记录             网址
    req = urllib.request.urlopen(img_url)
    data = req.read()
    # 写入记录的图片内容信息
    with open(img_name, "wb") as f:
        f.write(data)


def main():
    # 打开文件
    with open("新建文本文档.txt", "rb") as f:
        # 读取文件
        http = f.read().decode("utf-8")
    # 筛选文件
    download_list = re.findall(r'https://.*?\.jpg', http)  # \.如果不加斜杠转义，那么程序会把点当做正则中的点
    swp_list = []
    i = 0
    # 遍历列表
    for c in download_list:
        i += 1
        img_name = "%d.jpg" % i
        swp_list.append(gevent.spawn(download, img_name, c))
    # 等待所有乱执行结束
    gevent.joinall(swp_list)


if __name__ == '__main__':
    main()
