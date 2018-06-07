from flask import Blueprint, request, render_template, g, redirect, url_for, make_response, abort
from flask import session as flask_session
from flask import send_from_directory
from app import app

pageView = Blueprint('pageView', __name__, template_folder="templates")

@pageView.route('/static/<path:filename>')
def static(filename):
    return send_from_directory(app.config['STATIC_FOLDER'], filename, as_attachment=False)

@pageView.route('/', methods=['GET'])
def index():
    return render_template('pages/index.html')
