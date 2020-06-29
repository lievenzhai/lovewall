import os
from lovewall import app

# 定义开发数据库URL(os.path.join拼接路径，os.path.dirname获取上一级路径，root_path获取app路径)
# 得到的url应该时：sqlite://lovewall/data.db
dev_db = 'sqlite:///' + os.path.join(os.path.dirname(app.root_path), 'data.db')

# 设置密钥(os.getenv获取环境变量，第二个参数'secret string'时默认值)
SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')
# 关闭追踪数据库的修改
SQLALCHEMY_TRACK_MODIFICATIONS = False
# 设置数据库URI
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db)