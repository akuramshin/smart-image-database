"""
This file contains the functional tests for the 'search' blueprint.

These tests use GETs and POSTs to different URLs to check for the proper behavior.
"""


def test_text_search(test_client, init_database):
     """
    GIVEN a testing client
    WHEN the '/api/search-text' page is accessed with POST request
    THEN check that we are shown correct search result
    """
     search = dict(search='cat')
     response = test_client.post('/api/search-text', data=search, follow_redirects=True)

     assert response.status_code == 200
     assert b'cat' in response.data

     search = dict(search='duck')
     response = test_client.post('/api/search-text', data=search, follow_redirects=True)

     assert response.status_code == 200
     assert b'No images found that match your search' in response.data

     search = dict(search='all')
     response = test_client.post('/api/search-text', data=search, follow_redirects=True)

     assert response.status_code == 200
     assert b'dog' in response.data
     assert b'cat' in response.data


def test_image_search(test_client, init_database):
     """
    GIVEN a testing client
    WHEN the '/api/search-image' page is accessed with POST request
    THEN check that we are shown correct search result
    """
     files = dict(file=open('tests/functional/dog2.jpg', 'rb'))
     response = test_client.post('/api/search-image', data=files, follow_redirects=True)

     assert response.status_code == 200
     assert b'dog' in response.data

     files = dict(file=open('tests/functional/teddy.jpg', 'rb'))
     response = test_client.post('/api/search-image', data=files, follow_redirects=True)

     assert response.status_code == 200
     assert b'No images found that match your search' in response.data

