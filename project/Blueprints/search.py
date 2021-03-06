from flask import render_template, request, Blueprint, redirect, url_for, abort
from ..shared.utils import tag_search, analyze_image
from ..models import Image

search_blueprint = Blueprint('search_blueprint', __name__, template_folder='templates')


@search_blueprint.route('/search')
def search():
    return render_template('search.html')


# Check if the POSTed text query matches any of the images in our database
@search_blueprint.route('/api/search-text', methods=['POST'])
def api_search_text():
    search = request.form['search'].lower()

    images = tag_search(search)
    
    if images:
        return render_template('search.html', results=images)
    else:
        return redirect(url_for('search_blueprint.search'))


# Detect the tags of the query image and check if they match any of the images in our database
@search_blueprint.route('/api/search-image', methods=['POST'])
def api_search_image():
    file = request.files['file']

    tags = analyze_image(file)
    if tags:
        images = tag_search(tags[0], tags[1])

    if images:
        return render_template('search.html', results=images)
    else:
        return redirect(url_for('search_blueprint.search'))


# Given the unique id of the image in our database, display that image with full resolution
@search_blueprint.route('/view/<image_id>')
def view_image(image_id):
    image = Image.query.filter(Image.id == image_id).first()

    return render_template('view.html', image=image)
    


