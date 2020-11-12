from flask import Flask

# instantiate new object
app = Flask(__name__)

# Look into current directory and import file
from .import routes