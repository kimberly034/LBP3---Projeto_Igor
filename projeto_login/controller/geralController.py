# controllers/geralController.py
from flask import Blueprint, render_template

geral_bp = Blueprint('geral', __name__)

@geral_bp.route('/')
def index():
    return render_template('index.html')

@geral_bp.route('/admin')
def admin():
    return render_template('admin.html')
