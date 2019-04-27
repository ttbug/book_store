from flask import Blueprint

# 或者也可以把这句放到单独的文件中
web = Blueprint('web', __name__)

# 导入相应的模块，注意位置

from app.webviews import web