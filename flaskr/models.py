from .db import db


class Image(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    file_name = db.Column(db.String(100))
    item_primary = db.Column(db.String(100))
    item_secondary = db.Column(db.String(100))

    def __init__(self, data, primary, secondary):
        self.data = data
        self.item_primary = primary
        self.item_secondary = secondary


def add_image(file_name, primary, secondary):
    image = Image(file_name, primary, secondary)

    db.session.add(image)
    db.session.commit()



if __name__ == "__main__":

    # Run this file directly to create the database tables.
    print ("Creating database tables...")
    db.create_all()
    print ("Done!")