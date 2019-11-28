import random

# UserAgen池
class UserAgentMiddleware(object):
    
    def process_request(self, request, spider):  # 用于构造requset然后交给下载器
        first_num = random.randint(55, 62)
        third_num = random.randint(0, 3200)
        fourth_num = random.randint(0, 140)
        os_type = [
            '(Windows NT 6.1; WOW64)', '(Windows NT 10.0; WOW64)', '(X11; Linux x86_64)',
            '(Macintosh; Intel Mac OS X 10_12_6)'
        ]
        chrome_version = 'Chrome/{}.0.{}.{}'.format(first_num, third_num, fourth_num)
    
        user_agent= ' '.join(['Mozilla/5.0', random.choice(os_type), 'AppleWebKit/537.36',
                       '(KHTML, like Gecko)', chrome_version, 'Safari/537.36']
                      )
        print(user_agent)
        request.headers['User-Agent'] = user_agent

    def process_response(self,request,response,spider):  # 用于过滤response然后交给爬虫
        return response

# ip代理池
class ProxyMiddleware(object):
    # def process_request(self, request, spider):
    #     proxy = random.choice(proxies)
    #     request.meta['proxy'] = proxy
    pass


# cookie池
class CookieMiddleware(object):
    """利用selenium模拟登陆目标网站，然后获取cookie保存到redis备用"""
    pass

