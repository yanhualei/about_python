import requests
url = "https://www.baidu.com/"
headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36"}
cookie_dict = {"name":"nadlkhfaefnadful_aef","pwd":"1h2i23hj3hudfjasdlfadhafialufha"}

respons = requests.get(url,headers=headers,cookies=cookie_dict)
print(respons)