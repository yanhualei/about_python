import re

import requests
from requests.exceptions import ConnectionError

base_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7'
}


def get_page(url, options={}):
    """
    抓取代理
    :param url:
    :param options:
    :return:
    """
    headers = dict(base_headers, **options)
    print('正在抓取', url)
    try:
        response = requests.get(url, headers=headers)
        print('抓取成功', url, response.status_code)
        if response.status_code == 200:
            # print(response.text)
            return response.text
    except ConnectionError:
        print('抓取失败', url)
        return None


def crawl_data5u():
    start_url = 'http://www.data5u.com'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'JSESSIONID=72B2A17CE717602D8964F633FC2A1871',
        'Host': 'www.data5u.com',
        'Referer': 'http://www.data5u.com/free/index.shtml',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
    }
    html = get_page(start_url, options=headers)
    if html:
        # re_ip_address = re.findall(r"\d+\.\d+\.\d+\.\d+",html)
        # ip_address = re.compile('<span><li>.*?</li><span></span><span style="width: 100px;"><li class="port GEAGE">(\d+)</li></span>', html)
        # re_ip_address = ip_address.findall(html)
        ip_address = re.compile("<span><li>(.*?)</li></span>\s+<span .*?><li .*?>(\d+)</li></span>", re.M)
        re_ip_address = ip_address.findall(html)
        print(re_ip_address)
        for address, port in re_ip_address:
            result = address + ':' + port
            print(result.replace(' ', ''))

if __name__ == '__main__':
    crawl_data5u()