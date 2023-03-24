import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SC = os.urandom(30).hex()
    SECRET_KEY = SC
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql+psycopg2://steamup:Ytu0lzq_2022@127.0.0.1:5432/steamup'
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    THREADS_PER_PAGE = 8
    WTF_CSRF_ENABLED = True
    WTF_CSRF_SECRET_KEY = SC
    UPLOAD_FILES = '/opt/env/steamup'
    ALLOWED_EXTENSIONS = {'csv', 'txt'}
    MAX_CONTENT_LENGTH = 2 * 1024 * 1024
    UPLOAD_EXTENSIONS = ['.txt']

