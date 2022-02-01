from flask import render_template, request
from config import app
from models.category import Category

class HomeViews(object):

    @staticmethod
    @app.route('/')
    def index():
        return render_template('home/index.html', context={
            'page_title': 'Главная',
            'passwords_list': Category.get_all_passwords()


        })