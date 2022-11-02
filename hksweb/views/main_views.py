from flask import Blueprint, url_for, render_template
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    return redirect(url_for('farminfo._list'))

#@bp.route('/index')
#def index():
#   return render_template('index.html')

@bp.route('/layout')
def layout():
   return render_template('layout.html')   

@bp.route('/citruswork')
def citruswork():
   return render_template('citruswork.html')   

@bp.route('/pesticide')
def pesticide():
   return render_template('pesticide.html')   

@bp.route('/cymbidiumdisease')
def cymbidiumdisease():
   return render_template('cymbidiumdisease.html')      