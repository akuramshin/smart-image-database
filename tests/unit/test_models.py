from project.models import Image

"""
This file (models.py) contains the unit tests for the data models.

"""


def test_new_user(new_image):
    """
    GIVEN a Image model
    WHEN a new Image is uploaded
    THEN check that the filename and the tag fields are defined correctly
    """
    assert new_image.file_name == 'dog.jpg'
    assert new_image.item_primary == 'dog'
    assert new_image.item_secondary == 'cat'