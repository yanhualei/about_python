import urllib.request
from gevent import monkey
import re
import gevent

monkey.patch_all()  # 打补丁，让所有的延时任务被认为是gevent的空闲时间


def download(img_name,img_url):
    # 通过图片链接地址，获取图片内容
    req = urllib.request.urlopen(img_url)  # 此时获取的只是图片页面的成功请求状态
    # 读取页面内容
    img_content = req.read()
    # 下载图片：读取图片内容，写在本地
    with open(r"./image_download/"+img_name, "wb") as f:
        f.write(img_content)


def main():
    # 正则匹配图片地址
    # https://rpic.douyucdn.cn/live-cover/appCovers/2018/06/26/5221558_20180626104204_big.jpg
    with open("./pic", "rb") as f:
        content = f.read()
    img_list = re.findall(r"https://.*?\.jpg",content.decode("utf-8"))
    pic_list = []
    m = 0
    for img_url in img_list:
        m += 1
        img_name = str(m) + ".jpg"
        pic_list.append(gevent.spawn(download, img_name, img_url))  # 先将所有下载任务准备好
    gevent.joinall(pic_list)  # 然后全部加入gevent任务


if __name__ == '__main__':
    main()

