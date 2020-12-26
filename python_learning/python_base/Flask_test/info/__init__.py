import redis
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from werkzeug.routing import BaseConverter

from configs.config import Config,config


# 数据库
db = SQLAlchemy()
redis_store = None


# 自定义正则转换器
class RegexConverter(BaseConverter):
    def __init__(self, url_map, *args):
        super(RegexConverter, self).__init__(url_map)
        # 将接受的第1个参数当作匹配规则进行保存
        self.regex = args[0]

def create_app(config_name):
    """通过传入不同的配置名字，初始化其对应配置的应用实例"""

    app = Flask(__name__,template_folder='templates')
    # 将自定义转换器添加到转换器字典中，并指定转换器使用时名字为: re
    app.url_map.converters['re'] = RegexConverter
    # 配置
    app.config.from_object(config[config_name])
    # 配置数据库
    db.init_app(app)
    # 配置redis
    global redis_store  # 为什么这里要申明global???
    redis_store = redis.StrictRedis(host=config[config_name].REDIS_HOST, port=config[config_name].REDIS_PORT)
    # 开启csrf保护
    CSRFProtect(app)
    # 设置session保存位置
    Session(app)

    # 注册蓝图
    from info.modules.index import index_blu
    app.register_blueprint(index_blu)
    from info.modules.news import news_blu
    app.register_blueprint(news_blu)

    return app