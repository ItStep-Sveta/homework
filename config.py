from flask import Flask
from pymongo import MongoClient


app = Flask(__name__)
app.config['SECRET_KEY'] = '125689'
app.config['TEMPLATES_AUTO_RELOAD'] = True
url = "mongodb+srv://sveta123:sveta12345678@cluster1.afxjy.mongodb.net/homework_db?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.homework_db