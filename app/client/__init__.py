""" Client App """

import os
from flask import Blueprint, render_template

client_bp = Blueprint('client_app', __name__,
                      url_prefix='',
                      static_url_path='',
                      static_folder='./vue_app/dist',
                      template_folder='./vue_app/dist',
                      )

@client_bp.route('/')
def index():
    return render_template('index.html')
