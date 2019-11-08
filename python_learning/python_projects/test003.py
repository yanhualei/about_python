import re

from lxml import etree
import requests
from fontTools.ttLib import TTFont
import reprlib

# base_font = TTFont('/home/oldeleven/PycharmProjects/base.woff')
# base_font.saveXML('base.xml')


url = 'https://maoyan.com/'
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36",
           }
response = requests.get(url, headers=headers)
font_file = re.findall(r'vfile\.meituan\.net\/colorstone\/(\w+\.woff)', response)[0]
font_url = 'http://vfile.meituan.net/colorstone/' + font_file

new_file = requests.get(font_url,headers=headers)
with open('./fonts/' + font_file, 'wb') as f:
    f.write(new_file.content)

base_font_dict ={"uniE187":"7","uniF651":"1","uniF878":"3","uniE8CD":"4","uniEA40":"2",
            "uniF871":"0","uniEB3E":"8","uniE20E":"6","uniEAE3":"5","uniF17E":"9"}

print("正常访问中...",response)
html = etree.HTML(response.content.decode())
li_list = html.xpath('//ul[@class="ranking-wrapper ranking-box"]/li')
content_list = []
n = 0
for li in li_list:
    item = {}
    if n ==0:
        item["电影名字"] = li.xpath('.//span//text()')[0].strip()
        item["票房"] = li.xpath('.//span//text()')[1].strip()
    else:
        item["电影名字"] = li.xpath('.//span[@class="ranking-movie-name"]/text()')[0].strip()
        item["票房"] = li.xpath('.//span[@class="stonefont"]/text()')[0].strip()
    n += 1
    print(item)
    content_list.append(item)



