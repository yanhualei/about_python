from bs4 import BeautifulSoup
import bs4
import requests
# 获取目标html文本
def gethtmltext(url):
    try:
        r = requests.get(url)
        # print(r.text)
        r.raise_for_status() # 抛出除200以外的所有异常
        r.encoding = r.apparent_encoding  # 使用apparent_encoding可以获得真实编码
        # encode = requests.utils.get_encodings_from_content(r.text)  # 从网页的中抽取
        return r.text
    except:
        return  "......"
# 获取目标内容
def fill_university_list(ulist,html):
    # 创建BeautifulSoup对象，html为获取的html文本内容
    soup = BeautifulSoup(html,"html.parser")
    for tr in soup.find("tbody").children:
        if isinstance(tr,bs4.element.Tag):
            tds = tr("td")
            ulist.append([tds[0].string,tds[1].string,tds[2].string,
                          tds[3].string])
    # print(ulist)

# 打印目标内容（或者保存目标内容）
def print_university_list(ulist,num):
    tplt = "{0:^10}\t{1:{4}^8}\t{2:6}\t{3:10}"  # {1：{4}^8什么意思}
    print(tplt.format("排名","学校名称","城市","总分",chr(12288))) # chr(12288)表示utf-8的中文空格
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0],u[1],u[2],u[3],chr(12288)))

def main():
    ulist = []
    url = "http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html"
    html_text = gethtmltext(url)
    fill_university_list(ulist,html_text)
    print_university_list(ulist,10) #  打印ulist中的20行

if __name__ == '__main__':
    main()