import re
import requests
from fontTools.ttLib import TTFont
from lxml import etree

"""
爬取猫眼电影数据
主要解决css字体web-font
爬取原理：通过观察发现，每个字体对应的编码无论如何变化，对应的glyf坐标相同或者相似
所以坐标差在一定范围就几乎可以认为是相同数字
缺点：爬取的结果不够精确，存在误差
"""

class Maoyan(object):
    def __init__(self):
        self.url = 'https://maoyan.com/board/1'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
        }


    def get_html(self, url):
        response = requests.get(url, headers=self.headers)
        return response


    def replace_font(self, response):

        base_font = TTFont('base.woff')
        # base_font.saveXML('base_font.xml')
        base_dict = {"uniE187": "7", "uniF651": "1", "uniF878": "3", "uniE8CD": "4", "uniEA40": "2",
                     "uniF871": "0", "uniEB3E": "8", "uniE20E": "6", "uniEAE3": "5", "uniF17E": "9"}
        base_list = base_font.getGlyphOrder()[2:]
        print(base_list)

        font_file = re.findall(r'vfile\.meituan\.net\/colorstone\/(\w+\.woff)', response)[0]
        font_url = 'http://vfile.meituan.net/colorstone/' + font_file
        new_file = self.get_html(font_url)
        with open(font_file, 'wb') as f:
            f.write(new_file.content)
        new_font = TTFont(font_file)
        # new_font.saveXML('new_font.xml')
        new_list = new_font.getGlyphOrder()[2:]


        coordinate_list1 = []
        for uniname1 in base_list:
            # 获取字体对象的横纵坐标信息
            coordinate = base_font['glyf'][uniname1].coordinates
            coordinate_list1.append(list(coordinate))

        coordinate_list2 = []
        for uniname2 in new_list:
            coordinate = new_font['glyf'][uniname2].coordinates
            coordinate_list2.append(list(coordinate))

        index2 = -1
        new_dict = {}
        for name2 in coordinate_list2:
            index2 += 1
            index1 = -1
            for name1 in coordinate_list1:
                index1 += 1
                if self.compare(name1, name2):
                    new_dict[new_list[index2]] = base_dict[base_list[index1]]

        # new_dict = {}
        # for name2 in new_list:
        #     obj2 = new_font['glyf'][name2]
        #     for name1 in base_list:
        #         obj1 = base_font['glyf'][name1]
        #         if obj1 == obj2:
        #             new_dict[name2] = base_dict[name1]


        for i in new_list:
            pattern = i.replace('uni', '&#x').lower() + ';'
            response = response.replace(pattern, new_dict[i])
        return response


    def compare(self, c1, c2):
        """
        输入：某俩个对象字体的坐标列表
        输出：bool类型，True则可视为是同一个字
        """
        # if len(c1) != len(c2):
        #     return False
        # else:
        # for i in range(len(c1)):
        for i in range(5):
            if abs(c1[i][0] - c2[i][0]) < 70 and abs(c1[i][1] - c2[i][1]) < 70:
                pass
            else:
                return False
        return True

    def parse_info(self, response):
        tree = etree.HTML(response)
        items = []
        for node in tree.xpath('//dd//div[@class="board-item-content"]'):
            item ={}

            item['电影名'] = node.xpath('./div[@class="movie-item-info"]//a/text()')[0]

            item['今日票房'] = node.xpath('.//p[@class="realtime"]/span/span/text()')[0] + node.xpath(
                './/p[@class="realtime"]//text()[2]')[0].replace('\n', '')

            item['总票房'] = node.xpath('.//p[@class="total-boxoffice"]/span/span/text()')[0] + node.xpath(
                './/p[@class="total-boxoffice"]//text()[2]')[0].replace('\n', '')

            items.append(item)
        return items


    def start_crawl(self):

        response = self.get_html(self.url).text
        response = self.replace_font(response)
        results = self.parse_info(response)

        for i in results:
            print(i)


if __name__ == '__main__':
    maoyan = Maoyan()
    maoyan.start_crawl()