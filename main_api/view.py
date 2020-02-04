from app import ma, app
from flask import jsonify, Blueprint
from models import Keep


main_api = Blueprint(
    'main_api',
    __name__
)


class KeepSchema(ma.Schema):
    fields = ('id', 'title', 'slug', 'body')


keep_schema = KeepSchema()
keeps_schema = KeepSchema(many=True)

# Get all keeps
@app.route('/', methods=['GET'])
def get_keeps():
    all_keeps = Keep.query.all()
    result = keeps_schema.dump(all_keeps)
    return jsonify(result.data)
