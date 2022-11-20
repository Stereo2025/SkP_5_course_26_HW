from flask import Flask

from config import DB_NAME, DB_HOST, DB_USER, DB_PASSWORD
from db import db
from views import main_bp


def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    app.register_blueprint(main_bp)
    return app


app = create_app()

if __name__ == '__main__':
    app.run(port=80)
