from flask import render_template
from flask import request
from flask import Blueprint


from models import Keep

main_blueprint = Blueprint(
    'main_blueprint',
    __name__,
    template_folder='templates'
)

@main_blueprint.route('/')
def index():

    q = request.args.get('q')

    if q:
        keeps = Keep.query.filter(
            Keep.title.contains(q) | Keep.body.contains(q)).all()
    else:
        keeps = Keep.query.all()

    return render_template('index.html', keeps=keeps)


@main_blueprint.route('/<slug>')
def keep_detail(slug):
    keep = Keep.query.filter(Keep.slug == slug).first()
    return render_template('keep_detail.html', keep=keep)
