from config import app

from views.home import HomeViews

if __name__ == '__main__':

    views1 = HomeViews()
    app.run(debug=True)