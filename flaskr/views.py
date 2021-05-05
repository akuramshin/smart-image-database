from flask import render_template, request

from models import Image
from app import app

upload_page = Blueprint('upload_page', __name__, template_folder='templates')


# @app.route('/add', methods=['GET', 'POST'])
# def add():

#     if request.method == 'GET':
#         return render_template('add.html')

#     # Because we 'returned' for a 'GET', if we get to this next bit, we must
#     # have received a POST

#     # Get the incoming data from the request.form dictionary.
#     # The values on the right, inside get(), correspond to the 'name'
#     # values in the HTML form that was submitted.

#     dessert_name = request.form.get('name_field')
#     dessert_price = request.form.get('price_field')
#     dessert_cals = request.form.get('cals_field')

#     dessert = create_dessert(dessert_name, dessert_price, dessert_cals)
#     return render_template('add.html', dessert=dessert)

@upload_page.route('/')
def index():
    return render_template('index.html')


@upload_page.route('/api/uploadImages', methods=['POST'])
def upload_files():
    file = request.files['file']

    # Check filename extension to be valid
    filename = file.filename
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['EXTENSIONS']:
            abort(400)

    # Analyze image


    add_image(file.read(), "primary", "secondary")

    print("Saved {} to the database!".format(filename))
    return redirect(url_for('index'))