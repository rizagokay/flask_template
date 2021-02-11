import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from logging.config import dictConfig
from config import ProductionConfig, DevelopmentConfig

db = SQLAlchemy()
migrate = Migrate()

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {
        'file.handler': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'app.log',
            'maxBytes': 10000000,
            'backupCount': 5,
            'level': 'DEBUG',
        },
        'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default'
        }
    },
    'loggers': {
        'werkzeug': {
            'level': 'DEBUG',
            'handlers': ['file.handler', 'wsgi'],
        },
    }
    
})


def create_app(test_config=None):
    
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
     
    app.config.from_object(DevelopmentConfig())

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Ping pong route
    @app.route('/ping')
    def hello():
        return 'Pong!'
    
    db.init_app(app)
    migrate.init_app(app, db)

    # Uncomment for model imports
    # from .models import *
    
    with app.app_context():
        
        from .routes import auth, index
        from .api import api
        
        app.register_blueprint(auth.bp)
        app.register_blueprint(index.bp)
        app.register_blueprint(api.bp)
        app.add_url_rule('/', endpoint='index')
        
        import error_handlers
                
        return app