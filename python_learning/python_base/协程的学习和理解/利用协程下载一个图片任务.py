# 协程：依赖于线程，线程结束，协程相应结束
import urllib.request
import gevent
from gevent import monkey

monkey.patch_all()  # 打补丁，让所有消耗时间的操作，都被认为是gevent延时，当然下面的下载任务也是耗时任务
# 爬取熊猫泛娱乐主播封面图片

def download(image_name,image_url):
	# 先获取图片网页请求
	req = urllib.request.urlopen(image_url)
	# 读取图片内容
	img_content = req.read()
	with open(image_name,"wb") as f:
		f.write(img_content) 


def main():
	gevent.joinall([
		gevent.spawn(download, "C:/Users/xieolei/Desktop/meinv1.jpeg", "https://image.xingyan.panda.tv/e0c94579c14d61b592301ac5ac139887_w338_h190.jpeg"),
		gevent.spawn(download, "C:/Users/xieolei/Desktop/meinv2.jpeg", "https://image.xingyan.panda.tv/f567532a8389196f5a483980237c64f1_w338_h190.jpeg")
		])


if __name__ =="__main__":
	main()





