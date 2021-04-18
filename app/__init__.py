import os
from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

from config import config

csrf = CSRFProtect()
db = SQLAlchemy()
config = config[os.getenv("APP_CONFIG", "default")]
login_manager = LoginManager()
moment = Moment()


def create_app():
    app = Flask(__name__)

    config.init_app(app)

    csrf.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.session_protection = "strong"
    login_manager.login_view = "auth.login"
    Migrate(app, db)
    moment.init_app(app)

    if not app.debug and not app.testing:
        try:
            from flask.ext.sslify import SSLify

            sslify = SSLify(app)
            app.logger.info("SSL enabled")
        except:
            pass

    from app.blueprints.main import main as main_blueprint

    app.register_blueprint(main_blueprint)

    from app.blueprints.auth import auth as auth_blueprint
    from app.blueprints.crypto import crypto as crypto_blueprint
    from app.blueprints.forex import forex as forex_blueprint
    from app.blueprints.portfolio import portfolio as portfolio_blueprint
    from app.blueprints.stocks import stocks as stocks_blueprint

    app.register_blueprint(auth_blueprint, url_prefix="/auth")
    app.register_blueprint(crypto_blueprint, url_prefix="/crypto")
    app.register_blueprint(portfolio_blueprint, url_prefix="/portfolio")
    app.register_blueprint(forex_blueprint, url_prefix="/forex")
    app.register_blueprint(stocks_blueprint, url_prefix="/stocks")

    # Add additional blueprints here...
    # example:
    # from app.blueprints.myblueprint import myblueprint as myblueprint_blueprint
    # app.register_blueprint(myblueprint_blueprint, url_prefix='/myblueprint')

    return app
