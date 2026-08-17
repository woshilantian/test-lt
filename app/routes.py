from flask import Blueprint, render_template, jsonify

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return jsonify({"message": "Welcome to test-lt"})

@bp.route('/login')
def login():
    return render_template('login.html')
