from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_moment import Moment

# 创建app
app = Flask('lovewall')
bootstrap = Bootstrap(app)
moment = Moment(app)
# 加载配置文件
app.config.from_pyfile('setting.py')
# 去掉jinja2语句占据的空行
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

db = SQLAlchemy(app)

from lovewall import errors, views, commands
