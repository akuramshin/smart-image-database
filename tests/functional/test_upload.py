from project.models import Image

"""
This file contains the functional tests for the 'upload' blueprint.

These tests use GETs and POSTs to different URLs to check for the proper behavior.
"""

def test_home_page(test_client):
    """
    GIVEN a testing client
    WHEN the '/' (home) page is accessed with GET request
    THEN check that we are directed to the upload page
    """
    response = test_client.get('/')
    assert response.status_code == 200
    assert b"Upload Images" in response.data

def test_upload_image(test_client, init_database):
    """
    GIVEN a testing client
    WHEN the '/api/uploadImages' page recieves a POST request
    THEN check that we recieve a valid response and the database is updated
    """
    files = dict(file=open('tests/functional/dog2.jpg', 'rb'))
    response = test_client.post('/api/uploadImages',data=files,follow_redirects=True)

    assert response.status_code == 200
    assert Image.query.filter(Image.file_name =='dog2.jpg').first() is not None





