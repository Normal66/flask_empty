from flask import Flask
from flask.json import JSONEncoder
from flask_migrate import Migrate
from sqlalchemy.ext.declarative import DeclarativeMeta
import logging.config
from config import Config
from .database import db


_log_format = f"%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'file': {
            'format': _log_format
        }
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'file',
            'encoding': 'utf-8',
            'filename': 'flasky.log',
            'mode': 'a'
        }
    },
    'loggers': {
        '': {
            'level': 'DEBUG',
            'handlers': ['file'],
            'propagate': True
        },
    }
}


class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            return obj.to_dict()
        return super(CustomJSONEncoder, self).default(obj)


def create_app():
    logging.config.dictConfig(LOGGING)
    logging.getLogger("requests").setLevel(logging.CRITICAL)
    logging.getLogger("urllib3").setLevel(logging.CRITICAL)
    logger = logging.getLogger(__name__)

    app = Flask(__name__)

    app.config.from_object(Config)
    app.json_encoder = CustomJSONEncoder

    from app.main.views import main_bp
    app.register_blueprint(main_bp)
    db.init_app(app)
    migrate = Migrate(app, db)
    return app
