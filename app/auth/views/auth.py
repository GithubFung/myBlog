from flask import Blueprint, render_template

bp = Blueprint('auth', __name__, url_prefix='/auth', static_folder='../static', template_folder='../templates')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')
