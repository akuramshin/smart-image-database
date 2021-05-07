from flask import render_template, request, Blueprint, redirect, url_for, abort
from ..shared.utils import analyze_image, get_filename
from ..models import Image, add_image

upload_blueprint = Blueprint('upload_blueprint', __name__, template_folder='templates')


@upload_blueprint.route('/')
@upload_blueprint.route('/upload')
def upload():
    return render_template('upload.html')


# Given a POSTed image:
# 1. Check if the file is safe
# 2. Save the image in the file system
# 3. Add an entry into the database with the filename and tags
@upload_blueprint.route('/api/uploadImages', methods=['POST'])
def api_upload():
    file = request.files['file']
    filename = get_filename(file)

    tags = analyze_image(file)
    if not tags:
        abort(400)
    else:
        add_image(filename, tags[0], tags[1])

    return redirect(url_for('upload_blueprint.upload'))