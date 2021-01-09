from flask import render_template, request, Blueprint
from app import db

main_bp = Blueprint('main_bp', __name__)

@main_bp.route("/")
@main_bp.route("/home")
def home():
    return render_template('home.html', title='Home')

@main_bp.route("/about")
def about():
    return render_template('about.html', title='About')
