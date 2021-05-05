# Shopify Developer Challenge

## Get started
In order to run the API locally, you need the Python 3.x.x with the following dependencies installed:
* flask
* SQLAlchemy
* tensorflow
* OpenCV
* Keras
* imageAI

You can use the package manager [pip](https://pip.pypa.io/en/stable/) to install the dependencies:

```bash
pip install Flask
pip install Flask-SQLAlchemy
pip install tensorflow
pip install opencv-python
pip install keras
pip install imageAI
```

## Usage


## Security 
Data submitted by users should never be trusted, so there are several checks we should perform.
1. A file with a virus or other malicious software might be uploaded where we expect an image.
2. directory traversal attacks via filenames.
3. A file size attack might cause our application to overload or fail. 

Although I have included checks for 2. and 3. there are great security libraries like **Werkzeug** that can further check filenames. For 1. we can create a check that makes sure that the files we are receiving indeed image files via checking the file header.
