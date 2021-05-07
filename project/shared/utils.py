from ..models import Image
from flask import current_app
import os
from project import dt
import ntpath

# Extract the filename in the case that the uploaded filename is in file path form (e.g. '/a/b/c/dog.jpg)
def get_filename(file):
    return ntpath.basename(file.filename)


# Given search tags, query our database to see if any images match
def tag_search(primary, secondary=None):
    images = None
    if primary == "all":
        images = Image.query.all()
    elif primary == "None":
        return images
    else:
        if secondary is None or secondary == "None":
            images = Image.query.filter((Image.item_primary == primary) | (Image.item_secondary == primary)).all()
        else:
            images = Image.query.filter((Image.item_primary == primary) | (Image.item_secondary == primary) |
                                        (Image.item_primary == secondary) | (Image.item_secondary == secondary)).all()
    
    return images


def analyze_image(file):
    filename = get_filename(file)

    # Check filename extension to be valid
    if filename != '':
        extension = os.path.splitext(filename)[1]
        if extension not in current_app.config['EXTENSIONS']:
            return False

    # Save the image to the file system and run object detection
    file.save(os.path.join(current_app.config['UPLOAD_PATH'], filename))
    objects = dt.detect(os.path.join(current_app.config['UPLOAD_PATH'], filename))

    return [objects[0], objects[1]]