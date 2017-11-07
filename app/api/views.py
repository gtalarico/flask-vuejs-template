"""
Backend Template

Use this to display server debugging info during development

"""
from flask import render_template
from app.api import api_bp


@api_bp.route('/')
def api():
    return render_template('api.html', msg='API Blueprint View')


from flask import session, jsonify

@api_bp.route('/test')
def test():
    session['test_cookie'] = 'xxx'
    return jsonify({'test': True})

@api_bp.route('/testcookie')
def testcookie():
    return jsonify({'msg': 'Here is  cookie is {}'.format(session)})
