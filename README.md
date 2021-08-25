# Smart Image Database
Image database that automatically labels uploaded images using a machine learning model for keyword image search.

## Get started
In order to run the API locally, you need the Python 3.x.x with the following dependencies installed:
* flask
* SQLAlchemy
* tensorflow
* OpenCV
* Keras
* imageAI
* pytest

You can use the package manager [pip](https://pip.pypa.io/en/stable/) to install the dependencies:

```bash
pip install Flask
pip install Flask-SQLAlchemy
pip install tensorflow
pip install opencv-python
pip install keras
pip install imageAI
pip install pytest
```

I was interested in implementing image search myself so I developed it from scratch. The library [**flask_image_search**](https://pypi.org/project/flask-image-search/) is an already made solution that works with flask. It is smarter to use already existing libraries if they match your use case.

## Usage

While in the main directory (`smart-image-search`), run the command `flask run` to start the flask application. It might take a bit for the application to start as it is creating the database and loading in the object detection model (ignore the warnings if you don't have a GPU set up on your machine).

Once the application is running, you can head over to the webpage [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

There are two main functionalities: **upload** and **search**. 

For [upload](http://127.0.0.1:5000/upload), you can drag and drop your image(s) into the drop-zone for them to be uploaded. The backend runs object detection to categorize each image with two tags (highest probability objects detected). The image files are saved in the file system along with a corresponding entry in the database.

For [search](http://127.0.0.1:5000/search), there are two options, search using text or an image:
* Text search is looking for tag keywords such as "person" or "car". If you want to list all images, enter "all" into the text search.
* Image search looks for semantically similar images by comparing the query image tags with tags of images in the database.

For each image in the search result, its tags are listed and you can click on each image to get a closer look.

## Testing
I decided to use the `pytest` tool for testing. Pytest's fixtures make it easier to create multiple tests that require the same initial state.

I have split my tests into the unit and functional categories. Each test is accompanied by a description following the Given-When-Then style.

While in the main directory (`smart-image-search`), enter the command `python -m pytest` to run the tests.


## Security 
Data submitted by users should never be trusted, so there are several checks we should perform.
1. A file with a virus or other malicious software might be uploaded where we expect an image.
2. directory traversal attacks via filenames.
3. A file size attack might cause our application to overload or fail. 

Although I have included checks for (2) and (3) there are great security libraries like [**Werkzeug**](https://pypi.org/project/Werkzeug/) that can further check filenames. For (1) we can create a check that makes sure that the files we are receiving indeed image files via checking the file header.

## Further Improvement
Some things I would implement for a more polished version of this project.

* **Problem**: Currently files are saved on the server using the filename of the uploaded image. If an image is uploaded with the same filename as an existing image, it will not be saved.
    * **Solution**: Ignore client-provided filenames and generate 
      our own filenames when saving images. This can be done if we 
      have some user system.
* Currently search via image works through image tags; semantic similarity. Another approach is to look at literal similarity by comparing pixel values
