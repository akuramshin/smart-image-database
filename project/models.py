from project import db


class Image(db.Model):
    __tablename__ = 'images'

    id = db.Column(db.Integer,primary_key=True)
    file_name = db.Column(db.Text)
    item_primary = db.Column(db.String(100))
    item_secondary = db.Column(db.String(100))

    def __init__(self, file_name, primary, secondary):
        self.file_name = file_name
        self.item_primary = primary
        self.item_secondary = secondary


def add_image(file_name, primary, secondary):
    image = Image(file_name, primary, secondary)

    db.session.add(image)
    db.session.commit()