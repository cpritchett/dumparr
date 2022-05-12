import arrapi
import sqlite3
from flask import Flask

__author__ = "Chad Pritchett"
__credits__ = "cpritchett"
__package_name__ = "dumparr"
__project_name__ = "dumparr"
__description__ = "Database backups for arr apps:"
__url__ = "https://github.com/cpritchett/dumparr"
__email__ = 'chad@chadpritchett.com'
__license__ = 'GPL 3.0'


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


