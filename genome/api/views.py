"""
Backend Template

Use this to display server debugging info during development

"""
from flask import render_template
from genome.api import api_bp


@api_bp.route('/')
def api():
    return render_template('api.html', msg='API Blueprint View')
