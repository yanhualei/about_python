import re
import requests
from fontTools.ttLib import TTFont

url = 'https://maoyan.com/'
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36",
           }
base_font  = TTFont("base.woff")
base_font_list = base_font.getGlyphOrder()[2:]
base_font_dict ={"uniE187":"7","uniF651":"1","uniF878":"3","uniE8CD":"4","uniEA40":"2",
            "uniF871":"0","uniEB3E":"8","uniE20E":"6","uniEAE3":"5","uniF17E":"9"}

response = requests.get(url, headers=headers).content.decode()
font_file_eot = re.findall(r'vfile\.meituan\.net\/colorstone\/(\w+\.eot)', response)[0]
font_file_woff = re.findall(r'vfile\.meituan\.net\/colorstone\/(\w+\.woff)', response)[0]
font_file_list =[font_file_eot,font_file_woff]
print(font_file_list)
font_url_list = []
for i in font_file_list:
    font_url = 'http://vfile.meituan.net/colorstone/' + i
    new_file = requests.get(font_url,headers=headers)
    with open('{}'.format(i), 'wb') as f:
        f.write(new_file.content)

new_font = TTFont(font_file_woff)
new_list = new_font.getGlyphOrder()[2:]
print(new_list)
new_dict = {}
for new_name in new_list:
    obj2 = new_font['glyf'][new_name]
    for base_name in base_font:
        obj1 = base_font['glyf'][base_name]
        if obj1 == obj2:
            new_dict[new_name] = base_font[base_name]
print(new_dict)




