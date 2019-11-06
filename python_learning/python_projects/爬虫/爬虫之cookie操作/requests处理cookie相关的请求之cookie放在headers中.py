# requests处理cookie相关的请求之cookie放在headers中

# headers中的cookie：
# 使用分号(;)隔开
# 分号两边的类似a=b形式的表示一条cookie
# a=b中，a表示键（name），b表示值（value）
# 在headers中仅仅使用了cookie的name和value
import requests
url = "https://www.baidu.com/"
headers = {
"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
"Cookie":" Pycharm-26c2d973=dbb9b300-2483-478f-9f5a-16ca4580177e; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1512607763; Pycharm-26c2d974=f645329f-338e-486c-82c2-29e2a0205c74; _xsrf=2|d1a3d8ea|c5b07851cbce048bd5453846445de19d|1522379036"}

requests.get(url,headers=headers)