from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_wtf import CSRFProtect


from dotenv import load_dotenv

load_dotenv()
import os


app = Flask(__name__)
csrf = CSRFProtect(app)

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db = SQLAlchemy(app)

from flaskrecipes import routes