import click
from flask.cli import with_appcontext
from flask import Blueprint
from app import db
from app.auth.models import User

cmd_bp = Blueprint('cmd', __name__)

# Use this command to access
# flask cmd create_tables

@cmd_bp.cli.command('create_tables')
def create_tables():
    db.create_all()
