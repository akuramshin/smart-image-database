import pytest
from project import create_app, db
from project.models import Image


@pytest.fixture(scope='module')
def new_image():
    image = Image('dog.jpg', 'dog', 'cat')
    return image

@pytest.fixture(scope='module')
def test_client():
    app = create_app()

    with app.test_client() as testing_client:
        with app.app_context():
            yield testing_client  

@pytest.fixture(scope='module')
def init_database(test_client):
    db.create_all()

    image1 = Image('dog.jpg', 'dog', 'car')
    image2 = Image('cat.jpg', 'cat', 'None')
    db.session.add(image1)
    db.session.add(image2)

    db.session.commit()

    yield

    db.drop_all()

