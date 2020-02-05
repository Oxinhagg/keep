from app import ma, app, db
from flask import jsonify, Blueprint, request
from models import Keep


main_api = Blueprint(
    'main_api',
    __name__
)


class KeepSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'slug', 'body')


keep_schema = KeepSchema()
keeps_schema = KeepSchema(many=True)


def get_keep_for_slug(slug):
    return Keep.query.filter(Keep.slug == slug).first()

# Create a keep
@app.route('/', methods=['POST'])
def add_keep():
    title = request.json['title']
    body = request.json['body']

    new_keep = Keep(title=title, body=body)

    db.session.add(new_keep)
    db.session.commit()

    return keep_schema.jsonify(new_keep)

# Get all keeps
@app.route('/', methods=['GET'])
def get_keeps():
    all_keeps = Keep.query.all()
    result = keeps_schema.dump(all_keeps)
    return jsonify(result)

# Get single keep
@app.route('/<slug>', methods=['GET'])
def get_keep(slug):
    keep = get_keep_for_slug(slug)
    return keep_schema.jsonify(keep)

# Update keep
@app.route('/<slug>', methods=['PUT'])
def update_keep(slug):
    keep = get_keep_for_slug(slug)

    title = request.json['title']
    body = request.json['body']

    keep.title = title
    keep.body = body

    db.session.commit()

    return keep_schema.jsonify(keep)

# Delete keep
@app.route('/<slug>', methods=['DELETE'])
def delete_keep(slug):
    keep = get_keep_for_slug(slug)
    db.session.delete(keep)
    db.session.commit()

    return keep_schema.jsonify(keep)
