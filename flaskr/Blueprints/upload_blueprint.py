from flask import render_template, request, Blueprint, redirect, url_for, abort
from ..shared.utils import analyze_image
from ..models import Image, add_image

upload_blueprint = Blueprint('upload_blueprint', __name__, template_folder='templates')

@upload_blueprint.route('/upload')
def upload():
    return render_template('upload.html')


@upload_blueprint.route('/api/uploadImages', methods=['POST'])
def api_upload():
    file = request.files['file']
    filename = file.filename

    tags = analyze_image(file)
    if not tags:
        abort(400)
    else:
        add_image(filename, tags[0], tags[1])

    print("Saved {} to the database!".format(filename))
    return redirect(url_for('upload_blueprint.upload'))