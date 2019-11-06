import re
from pymysql import connect

URL_FUNC_DICT = dict()

"""装饰器什么时候运行：在web_server.py文件运行的时候
装饰器就映射到对应的函数了"""
def route(url):
    def set_func(func):
        URL_FUNC_DICT[url] = func
        def call_func(*args,**kwargs):
            return func(*args,**kwargs)
        return call_func
    return set_func
"""带参数的装饰器：
1.route("/center")调用route(url)
2.route("/center")的返回值当做装饰器对center进行装饰
3.此时参数就传到普通装饰其中了"""
@route(r"/center.html")
def center(ret):
    with open("./templates/center.html",encoding='utf-8') as f:
        content =  f.read()
    # stock_info = "这是从数据库查询出来的模块center"
    # content = re.sub(r"\{%content%\}", stock_info, content)
    # 把content中的{%content%}替换成stock_info
    conn = connect(host='localhost', port=3306, database='stock_db', user='root', password='root', charset='utf8')
    cs = conn.cursor()
    cs.execute("select i.code,i.short,i.chg,i.turnover,i.price,i.highs,f.note_info "
                +"from info as i inner join focus as f on i.id = f.info_id;")
    stock_info = cs.fetchall()
    cs.close()
    conn.close()
    tr_template="""
    <tr>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>
            <a type="button" class="btn btn-default btn-xs" href="/update/300268.html">
            <span class="glyphicon glyphicon-star" aria-hidden="true"></span>修改
        </a></td>
        <td>
            <input type="button" value="删除" id="toDel" name="toDel" systemidvalue="300268">
        </td>
        
    </tr>
    
    """
    html = ''
    for line_info in stock_info:
        html += tr_template%(line_info[0],line_info[1],line_info[2],line_info[3],
                             line_info[4],line_info[5],line_info[6])
    content =re.sub(r"\{%content%\}",html,content)
    return content
@route(r"/index.html")
def index(ret):
    with open("./templates/index.html",encoding='utf-8') as f:
       content = f.read()
    conn = connect(host='localhost', port=3306, database='stock_db', user='root', password='root', charset='utf8')
    cs = conn.cursor()
    cs.execute("select * from info;")
    stock_info = cs.fetchall()
    cs.close()
    conn.close()
    tr_template = '''<tr>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td><input type="button" value="添加" name="toAdd" systemIdValue="%s" >
                </td>
            </tr>
            '''
    html = ''
    for line_info in stock_info:
        html += tr_template % (line_info[0], line_info[1], line_info[2], line_info[3],
                               line_info[4], line_info[5], line_info[6], line_info[7],line_info[1])
    content =re.sub(r"\{%content%\}",html,content)
    # 把content中的{%content%}替换成stock_info
    return content


@route(r"/add/(\d+)\.html")
def add_focus(ret):
    # 1.获取股票代码
    stock_code = ret.group(1)
    conn = connect(host='localhost', port=3306, database='stock_db', user='root', password='root', charset='utf8')
    cs = conn.cursor()
    sql = "select * from info where code = %s;"
    cs.execute(sql,(stock_code,))  # 防注入
    # 2. 如果没有从info表中查询到信息，则认为是非法请求
    if not cs.fetchone():
        cs.close()
        conn.close()
        return  "没有这只股票......"
    sql = """select * from info as i inner join focus as f on i.id= f.info_id where i.code = %s;"""
    # 如果只图简单，可以直接去focus中查询；为了安全，保证用户关注的股票信息要在股票表格中，所以进行一下内连接
    # 3.判断是否已经关注过
    cs.execute(sql,(stock_code,))
    if cs.fetchone():
        cs.close()
        conn.close()
        return "已经关注过了，请勿重复关注......"
    # 添加关注
    sql ="""insert into focus (info_id) select id from info where code = %s;"""
    cs.execute(sql,(stock_code,))
    cs.close()
    conn.close()

    return "关注成功......"

# URL_FUNC_DICT = {
#     "/index.py":index,
#     "/center.py":center
# }
def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    file_name = env['PATH_INFO']

    """有可能用户访问的数据资源不存在
    如果不存在，找不到对应的资源，程序就会报错"""
    try:
        # func = URL_FUNC_DICT[file_name]
        # return func()
        """上面两行代码的简写"""
        # return URL_FUNC_DICT[file_name]()
        for url,func in URL_FUNC_DICT.items():
            ret = re.match(url,file_name)
            if  ret:
                return  func(ret)
    except Exception as e:
        return "找不到对应的资源...%s"%str(e)