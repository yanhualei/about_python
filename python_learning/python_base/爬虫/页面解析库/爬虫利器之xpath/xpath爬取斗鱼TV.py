import time
from lxml import etree

import requests
def douyu_spider():
    """斗鱼直播
    1.直播类别：和平精英
    2.房间id
    3.主播名
    4.直播间链接
    5.热度
    """
    url = "https://www.douyu.com/g_hpjy"
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36"}
    response = requests.get(url,headers=headers)
    # print(response.content.decode())
    response_text = response.content.decode()
    html = etree.HTML(response_text)
    li_list = html.xpath("//ul[@class='layout-Cover-list']/li")
    content_list = []
    for li in li_list:
        item = {}
        item["room_type"] = li.xpath('.//span[@class="DyListCover-zone"]/text()')[0]  # .//表示当前节点下所有【class="DyListCover-zone】的span
        # item["room_type"] = i.xpath('./span[@class="DyListCover-zone"]/text()') # ./表示当前节点的下一个节点，由于当前节点的下一个节点不是span，所以定位不到
        item['room_id'] = li.xpath('.//a[@class="DyListCover-wrap"]/@href')[0][1:]
        item['anchor_name'] =li.xpath('.//div[@class="DyListCover-info"]/h2/text()')[0].strip()
        item['room_link'] = "https://www.douyu.com"+li.xpath('.//a[@class="DyListCover-wrap"]/@href')[0]
        item['hot'] = li.xpath('.//div[@class="DyListCover-info"]/span/text()')[1]
        content_list.append(item)
    return content_list
def save(datas):
    with open('DyTV_hpjy.text','w+') as f:
        for data in datas:
            f.write(str(data))
            f.write("\n")
if __name__ == '__main__':
    datas = douyu_spider()
    time.sleep(0.5)
    save(datas)



"""
今天写这段代码的目的：再次回顾xpath库的应用
"""