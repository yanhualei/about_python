import json
from flask import render_template
from sqlalchemy import and_,func
from info import constants
from info.modules.news import news_blu
from info.models import News, Category


@news_blu.route("/news_one")
def news_one():
    """
    查询所有新闻消息
    :return:
    """
    news_query = News.query.filter_by(id=1)
    news_list = []
    for news in news_query:
        news_list.append(news.to_basic_dict())
    print(news_list)
    # data = json.dumps(news_list)
    data = news_list
    return render_template('news_list.html',data = data)


@news_blu.route("/news_all")
def news_all():
    """
    查询所有新闻消息
    :return:
    """
    news_query = News.query.all()
    news_list = []
    for news in news_query:
        news_list.append(news.to_basic_dict())
    print(news_list)
    # data = json.dumps(news_list)
    data = news_list
    return render_template('news_list.html',data = data)

@news_blu.route("/news_limit")
def news_limit():
    """
    查询指定区域范围内的数据
    :return:
    """
    news_query = News.query.offset(3).limit(6)
    news_list = []
    for news in news_query:
        news_list.append(news.to_basic_dict())
    return render_template("news_list.html",data=news_list)

@news_blu.route("/news_order")
def news_order():
    """
    查询指定区域范围内的数据
    :return:
    """
    # 这条sql语句相当于:select * from info_news order_by clicks limit 1,3
    news_query = News.query.order_by(News.clicks.desc()).offset(1).limit(3)
    news_list = []
    for news in news_query:
        news_list.append(news.to_basic_dict())
    return render_template("news_list.html",data=news_list)

@news_blu.route("/news_filter")
def news_filter():
    """
    查询指定区列的数据
    :return:
    """
    # 查询点击量大于100并且小于200的新闻id和标题
    # with_entities查询指定的列,返回的是元组列表
    # select id,title from info_news where click>=200 and click<=300

    news_query = News.query.with_entities(News.id,News.title).filter(and_(News.clicks>=200,News.clicks<=300)).all()
    # print(news_query)
    # news_list = []
    # for news in news_query:
    #     print(news)
    #     news_list.append(news)
    return render_template("news_list.html",data=news_query)

 #  左链接查询
@news_blu.route("/news_outerjoin")
def news_outerjoin():
    """
    多表联合查询
    :return:
    """
   #查询点击量大于200并且小于300的新闻id,title,clicks,所属类别,类别id
    #select n.id,n.category_id,n.clicks,ic.name,n.title from info_news n
    # left join  info_category ic on n.category_id = ic.id
    # group by n.id
    # having n.clicks>=200 and n.clicks<=300
    news_query = News.query.with_entities(News.id,
                                          News.category_id,
                                          News.clicks,
                                          News.title,
                                          Category.name).\
        outerjoin(Category,News.category_id == Category.id).\
        group_by(News.id).filter(and_(News.clicks>=200,News.clicks<=300)).all()
    # print(news_query)
    # news_list = []
    # for news in news_query:
    #     print(news)
    #     news_list.append(news)
    for id,category_id,clicks,title,name in news_query:
        print([id,category_id,clicks,title,name])
    return render_template("news_list.html",data=news_query)


@news_blu.route("/news_func")
def news_func():
    """
    多表联合查询
    :return:
    """
   #查询info_news的总点击量
    # select count(clicks) from news
    news_query = News.query.with_entities(func.sum(News.clicks)).all()
    # print(news_query)
    # news_list = []
    # for news in news_query:
    #     print(news)
    #     news_list.append(news)
    count = news_query[0][0]
    print(count)


    return render_template("news_list.html",data=count)


