import os
from flask import Flask
from app.config import DevelopmentConfig, ProductionConfig


def create_app():
    app = Flask(__name__)
    # for local use DevelopmentConfig instead of Production
    app.config.from_object(ProductionConfig)
    os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

    from app.routes import main
    app.register_blueprint(main)

    return app