# from app import ma, app, db
from .models import db
from flask_marshmallow import Marshmallow
from flask import jsonify, Blueprint, request
from .models import Keep


ma = Marshmallow()


main_api = Blueprint(
    'main_api',
    __name__
)


class KeepSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'body')


keep_schema = KeepSchema()
keeps_schema = KeepSchema(many=True)


def get_keep_for_id(id):
    return Keep.query.filter(Keep.id == id).first()

# Create a keep
@main_api.route('/', methods=['POST'])
def add_keep():
    print(request.json)
    title = request.json['title']
    body = request.json['body']

    new_keep = Keep(title=title, body=body)

    db.session.add(new_keep)
    db.session.commit()

    return keep_schema.jsonify(new_keep)

# Get all keeps
@main_api.route('/', methods=['GET'])
def get_keeps():
    all_keeps = Keep.query.all()
    result = keeps_schema.dump(all_keeps)
    return jsonify(result)

# Get single keep
@main_api.route('/<id>', methods=['GET'])
def get_keep(id):
    keep = get_keep_for_id(id)
    return keep_schema.jsonify(keep)

# Update keep
@main_api.route('/<id>', methods=['PUT'])
def update_keep(id):
    keep = get_keep_for_id(id)

    title = request.json['title']
    body = request.json['body']

    keep.title = title
    keep.body = body

    db.session.commit()

    return keep_schema.jsonify(keep)

# Delete keep
@main_api.route('/<id>', methods=['DELETE'])
def delete_keep(id):
    # keep = get_keep_for_id(id)
    keep = Keep.query.filter(Keep.id == id).first()
    db.session.delete(keep)
    db.session.commit()

    return keep_schema.jsonify(keep)
