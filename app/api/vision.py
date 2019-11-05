import io
import os
# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
from flask import Flask, render_template, request
from flask_uploads import UploadSet, configure_uploads, IMAGES
from google.oauth2 import service_account

# Change this to your local directory
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="../travelvive-2a4639cbd834.json"

# app = Flask(__name__)

photos = UploadSet('photos', IMAGES)

app.config['UPLOADED_PHOTOS_DEST'] = 'static/img'
configure_uploads(app, photos)
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
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'photo' in request.files:

        filename = photos.save(request.files['photo'])
        full_path = os.path.join(app.config['UPLOADED_PHOTOS_DEST'], filename)

        labels = detect_labels(full_path)
        #print(labels)
        predictions = []

        for label in labels:
                predictions.append(label.description)  #make a list as print would only show up in terminal

        prediction_text = ", ".join(predictions)  #make it a little more pretty with ','
    else:
        prediction_text = "nothing to predict.."
    
    return prediction_text
    # return render_template('upload.html', prediction_text=prediction_text)

