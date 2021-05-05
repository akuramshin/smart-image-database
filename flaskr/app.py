from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from .Blueprints.upload_blueprint import upload_blueprint
from .db import db

app = Flask(__name__)

# Set up the SQLAlchemy Database to be a local file 'desserts.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///images.db'
# Accepted file extensions
app.config['EXTENSIONS'] = ['.jpg', '.png']
# 2 MB files 
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 * 2
app.config['UPLOAD_PATH'] = 'input'

db.init_app(app)
app.register_blueprint(upload_blueprint)

if __name__ == "__main__":
    app.run(debug=True)