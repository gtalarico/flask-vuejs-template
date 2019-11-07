import io
import os
# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
from flask import Flask, render_template, request
from flask_uploads import UploadSet, configure_uploads, IMAGES
from google.oauth2 import service_account
from flask_restplus import Resource
# import firebase_admin
# from firebase_admin import db,credentials

from .security import require_auth
from . import api_rest

# cred = credentials.Certificate("/Users/shahnawaz/Documents/ml/ML Course/Week10/tripive/keys/tripive-firebase-adminsdk-zoa3q-3aac541827.json")
# firebase_admin.initialize_app(cred,options={
#     'databaseURL': 'https://tripvive.firebaseio.com'
# })

class SecureResource(Resource):
    """ Calls require_auth decorator on all requests """
    method_decorators = [require_auth]

# Change this to your local directory
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="../travelvive-2a4639cbd834.json"

# app = Flask(__name__)

photos = UploadSet('photos', IMAGES)

# firebase_admin.initialize_app(options={
#     'databaseURL': 'https://tripvive.firebaseio.com'
# })
# SUPERHEROES = db.reference('tripive')

# app.config['UPLOADED_PHOTOS_DEST'] = 'static/img'
# configure_uploads(app, photos)
# def model(filename):
#     #google.io stuff
#     return answer
def detect_labels(path):
    """Detects labels in the file."""
    #credentials = service_account.Credentials.from_service_account_file('D:\\mmwl\\final_project\\flask_app_image_classifier_google_vision\\travelvive-2a4639cbd834.json')
    client = vision.ImageAnnotatorClient()

    #client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = client.label_detection(image=image)
    #response = client.web_detection(image=image)
    #print(response)
    return response.label_detection
    #print('Labels:')

    #for label in labels:
    #    print(label.description)
# @api_rest.route('/upload/<string:resource_id>', methods=['GET', 'POST'])
# def upload():
#     if request.method == 'POST' and 'photo' in request.files:

#         filename = photos.save(request.files['photo'])
#         # full_path = os.path.join(app.config['UPLOADED_PHOTOS_DEST'], filename)
#         full_path = os.path.join('/static/img', filename)

#         labels = detect_labels(full_path)
#         #print(labels)
#         predictions = []

#         for label in labels:
#                 predictions.append(label.description)  #make a list as print would only show up in terminal

#         prediction_text = ", ".join(predictions)  #make it a little more pretty with ','
#     else:
#         prediction_text = "nothing to predict.."

#     # return {'timestamp': timestamp}
#     return {'prediction' : prediction_text}
#     # return render_template('upload.html', prediction_text=prediction_text)

# Sample Test Call
@api_rest.route('/test/<string:resource_id>')
class SecureResourceTwo(Resource):
    """ Unsecure Resource Class: Inherit from Resource """

    def get(self,resource_id):
        # timestamp = datetime.utcnow().isoformat()
        return {'timestamp': 'Hello World'}       

