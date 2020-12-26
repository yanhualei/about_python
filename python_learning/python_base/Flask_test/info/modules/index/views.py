from flask import render_template

from . import index_blu


@index_blu.route('/')
def index():
    data = "hello world"
    return render_template("index.html",data=data)





