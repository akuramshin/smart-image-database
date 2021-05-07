from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .shared.detector import Detector



db = SQLAlchemy()
dt = Detector("project/models/yolo-tiny.h5")


# Application factory
def create_app():
    app = Flask(__name__)

    # Project configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///images.db'
    app.config['EXTENSIONS'] = ['.jpg', '.png']            # Accepted image file extensions
    app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 * 2     # Accept image files of max size 2 MB
    app.config['UPLOAD_PATH'] = 'project/static/input'             # Path to folder where images are saved
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
   
    from project.Blueprints.search import search_blueprint
    from project.Blueprints.upload import upload_blueprint

    app.register_blueprint(upload_blueprint)
    app.register_blueprint(search_blueprint)

    return app
