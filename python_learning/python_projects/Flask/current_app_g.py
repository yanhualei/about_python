from flask import Flask
from flask_script import Manager

app = Flask(__name__)
# 把 Manager 类和应用程序实例进行关联
manager = Manager(app)

@app.route('/')
def index():
    return "Flask 测试"

if __name__ == "__main__":
    # app.run()
    manager.run()