import requests
from proxypool.setting import TEST_URL


proxy = '117.41.0.34:8080'

proxies = {
    'http': 'http://' + proxy,
    'https': 'https://' + proxy,
}
headers ={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36"}

print(TEST_URL)
requests.packages.urllib3.disable_warnings()  # 防止报verify强制验证警报
response = requests.get(TEST_URL, proxies=proxies,headers=headers,verify=False)  # TEST_URL：爬取的目标网站，verify：ssl证书验证
if response.status_code == 200:
    print('Successfully')
    # print(response.text)