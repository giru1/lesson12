from flask import Flask, render_template
import logging
from logging.config import dictConfig



app = Flask(__name__)

import views

