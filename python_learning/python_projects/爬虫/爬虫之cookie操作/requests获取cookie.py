
import requests
url = "https://www.baidu.com/"
headers = {
"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}

response = requests.get(url,headers=headers)
print(response.cookies)
cookies = requests.utils.dict_from_cookiejar(response.cookies)  # dict_from_cookiejar将cookies转化为字典模式
print(cookies)