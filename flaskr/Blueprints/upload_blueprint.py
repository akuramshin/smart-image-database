from flask import render_template, request, Blueprint, redirect, url_for, abort, current_app

from ..models import Image, add_image
import os
from ..detector import detect

upload_blueprint = Blueprint('upload_blueprint', __name__, template_folder='templates')

@upload_blueprint.route('/')
def index():
    return render_template('index.html')


@upload_blueprint.route('/api/uploadImages', methods=['POST'])
def upload_files():
    file = request.files['file']

    # Check filename extension to be valid
    filename = file.filename
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in current_app.config['EXTENSIONS']:
            abort(400)

    # Analyze image
    file.save(os.path.join(current_app.config['UPLOAD_PATH'], filename))
    objects = detect(os.path.join(current_app.config['UPLOAD_PATH'], filename))

    add_image(filename, objects[0], objects[1])

    print("Saved {} to the database!".format(filename))
    return redirect(url_for('upload_blueprint.index'))