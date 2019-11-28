from flask import Flask, g

from .db import RedisClient

__all__ = ['app']

app = Flask(__name__)


def get_conn():
    if not hasattr(g, 'redis'):
        g.redis = RedisClient()
    return g.redis


# @app.route('/')
# def index():
#     return '<h2>Welcome to Proxy Pool System</h2>'


@app.route('/useful')
def get_useful():
    """
    Get a proxy
    :return: 随机代理
    """
    conn = get_conn()
    proxies,count = conn.useful()
    show_text =  "有用代理数{}".format(count)
    return show_text

@app.route('/random')
def get_proxy():
    """
    Get a proxy
    :return: 随机代理
    """
    conn = get_conn()
    return conn.random()


@app.route('/count')
def get_counts():
    """
    Get the count of proxies
    :return: 代理池总量
    """
    conn = get_conn()
    return str (conn.count())


if __name__ == '__main__':
    app.run()
