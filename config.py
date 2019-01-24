import os

basedir=os.path.abspath(os.path.dirname(__file__))

class config:
    DB_USERNAME = os.environ.get('DB_USERNAME')
    DB_PASSWORD = os.environ.get('DB_PASSWORD')

    @staticmethod
    def init_app(app):
        pass