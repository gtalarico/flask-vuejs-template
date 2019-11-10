import io
import os
# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
from flask import Flask, render_template, request,jsonify
from flask_uploads import UploadSet, configure_uploads, IMAGES
from google.oauth2 import service_account
from flask_restplus import Resource
import requests
import json
from io import BytesIO
# import firebase_admin
# from firebase_admin import db,credentials

from google.cloud import vision_v1
from google.cloud.vision_v1 import enums,types
import six

import urllib.request
from PIL import Image

from .security import require_auth
from . import api_rest



# cred = credentials.Certificate("/Users/shahnawaz/Documents/ml/ML Course/Week10/tripive/keys/tripive-firebase-adminsdk-zoa3q-3aac541827.json")
# cred = credentials.Certificate(os.getenv('FIREBASE_ADMIN_CRED'))
# firebase_admin.initialize_app(cred,options={
#     'databaseURL': 'https://tripvive.firebaseio.com'
# })

# https://cloud.google.com/vision/docs/batch
# https://googleapis.dev/python/google-api-core/latest/auth.html
# https://googleapis.dev/python/vision/latest/index.html
# 


# client = Client.from_service_account_json(os.getenv('FIREBASE_ADMIN_CRED'))
# credentials = service_account.Credentials.from_service_account_file(os.getenv('FIREBASE_ADMIN_CRED'))

class SecureResource(Resource):
    """ Calls require_auth decorator on all requests """
    method_decorators = [require_auth]

# Change this to your local directory
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="../travelvive-2a4639cbd834.json"

# app = Flask(__name__)

# photos = UploadSet('photos', IMAGES)

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
    credentials = service_account.Credentials.from_service_account_file(os.getenv('FIREBASE_ADMIN_CRED'))
    client = vision_v1.ImageAnnotatorClient()

    #client = vision_v1.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = client.label_detection(image=image)
    #response = client.web_detection(image=image)
    #print(response)
    return response.label_detection
    print('Labels:')

    for label in labels:
       print(label.description)

@api_rest.route('/upload/<string:resource_id>', methods=['GET', 'POST'])
class SecureVision(Resource):
        def post(self, resource_id):
                # Instantiates a client
                client = vision_v1.ImageAnnotatorClient()

                # The name of the image file to annotate
                file_name = os.path.abspath('files/taj.jpg')
                # Loads the image into memory
                with io.open(file_name, 'rb') as image_file:
                    content = image_file.read()

                image = types.Image(content=content)

                #Performs label detection on the image file
                response = client.label_detection(image=image)
                labels = response.label_annotations
                data = {}
                predictions = []
                for label in labels:
                    # data.update({
                    #     'label' : label.description,
                    #     'score' : label.score
                    # })
                    predictions.append({label.description,label.score})  #make a list as print would only show up in terminal
                    
                    # predictions.append(data)
                print(predictions)
                # data.update({tuple(predictions)})
                # prediction_text = ", ".join(predictions)  #make it a little more pretty with ','
                return {'prediction' : 'Success'}
                # return json.dumps(predictions, cls=SetEncoder)
    
################################# Old Code by Shyam ################################                
        # if request.method == 'POST':# and 'photo' in request.files:

                # filename = photos.save(request.files['photo'])
                # full_path = os.path.join(app.config[os.getenv('UPLOADED_PHOTOS_DEST')], filename)
                # print(full_path)
                # full_path = os.path.join('/static/img', filename)

                # labels = detect_labels('/Users/shahnawaz/Documents/ml/ML Course/Week10/tripive/files/taj.jpg')
                # print(labels)
                # predictions = []

                # for label in labels:
                #         predictions.append(label.description)  #make a list as print would only show up in terminal

                # # prediction_text = ", ".join(predictions)  #make it a little more pretty with ','
                # prediction_text = "Holy molly"
                # # else:
                # prediction_text = label

            # return {'timestamp': timestamp}
################################# Old Code by Shyam ################################            
                
            # return render_template('upload.html', prediction_text=prediction_text)

        def get(self, resource_id):
                return {'prediction' : 'Returning list of prediction'}  

@api_rest.route('/upload/object/<string:resource_id>')
class SecureVision(Resource):
        def post(self, resource_id):
                # Instantiates a client
                client = vision_v1.ImageAnnotatorClient()

                # The name of the image file to annotate
                file_name = os.path.abspath('files/yos.jpg')

                # Loads the image into memory
                with io.open(file_name, 'rb') as image_file:
                    content = image_file.read()

                image = types.Image(content=content)

                image = vision_v1.types.Image(content=content)
                data = {} 
                bounding_polygon_vertices = []   
                vertexcol = {}
                objects = client.object_localization(
                    image=image).localized_object_annotations

                print('Number of objects found: {}'.format(len(objects)))
                data.update({
                    'objects' : len(objects)
                })
                i = 1
                for object_ in objects:
                    data.update({
                        'objecttype' : object_.name, 
                        'confidence' : object_.score
                    })
                    print('\n{} (confidence: {})'.format(object_.name, object_.score))
                    print('Normalized bounding polygon vertices: ')
                    for vertex in object_.bounding_poly.normalized_vertices:
                        vertexcol.update({
                                 'vertex.x' : vertex.x,
                                 'vertex.y' : vertex.y
                        })
                        # i = i +1 
                        print(' - ({}, {})'.format(vertex.x, vertex.y))
                        bounding_polygon_vertices.append(vertexcol)
                        # data.update(bounding_polygon_vertices.copy())
                
                data.update({
                    'bounding_polygons' : bounding_polygon_vertices
                })
                return {'objects' : data}

        def get(self, resource_id):
                return {'prediction' : 'Returning list of prediction'}  

def sample_async_batch_annotate_images(input_image_uri, output_uri):
        """Perform async batch image annotation"""

        client = vision_v1.ImageAnnotatorClient()

        # input_image_uri = 'gs://cloud-samples-data/vision/label/wakeupcat.jpg'
        # output_uri = 'gs://your-bucket/prefix/'

        if isinstance(input_image_uri, six.binary_type):
            input_image_uri = input_image_uri.decode('utf-8')
        if isinstance(output_uri, six.binary_type):
            output_uri = output_uri.decode('utf-8')
        source = {'image_uri': input_image_uri}
        image = {'source': source}
        type_ = enums.Feature.Type.LABEL_DETECTION
        features_element = {'type': type_}
        type_2 = enums.Feature.Type.IMAGE_PROPERTIES
        features_element_2 = {'type': type_2}
        features = [features_element, features_element_2]
        requests_element = {'image': image, 'features': features}
        requests = [requests_element]
        gcs_destination = {'uri': output_uri}

        # The max number of responses to output in each JSON file
        batch_size = 2
        output_config = {'gcs_destination': gcs_destination, 'batch_size': batch_size}

        operation = client.async_batch_annotate_images(requests, output_config)

        print('Waiting for operation to complete...')
        response = operation.result()
        print(response)
        # The output is written to GCS with the provided output_uri as prefix
        # gcs_output_uri = response.output_config.gcs_destination.uri
        # print('Output written to GCS with prefix: {}'.format(gcs_output_uri))


@api_rest.route('/upload/batch/<string:resource_id>')           #Not working due to api auth issues
class SecureVision(Resource):
        def post(self, resource_id):
            input_image_uri = 'gs://tripive.appspot.com/images/taj.jpg'
            output_uri = 'gs://tripive.appspot.com/batch/'
            text = sample_async_batch_annotate_images(input_image_uri,output_uri)          
            return {'prediction' : 'prediction_text'}

        def get(self, resource_id):
                return {'prediction' : 'Returning list of prediction'}  

def detect_landmarks(path):
    """Detects landmarks in the file."""
    from google.cloud import vision
    import io
    client = vision_v1.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision_v1.types.Image(content=content)

    response = client.landmark_detection(image=image)
    landmarks = response.landmark_annotations
    print('Landmarks:')
    return landmarks

@api_rest.route('/upload/landmark/<string:resource_id>')           
class SecureVision(Resource):
        def post(self, resource_id):
            data = {}
            file_name = os.path.abspath('files/yos.jpg')
            
            # url = 'https://cdn.britannica.com/86/170586-050-AB7FEFAE/Taj-Mahal-Agra-India.jpg'
            # # image = Image.open(urllib.request.urlopen(url))
            # input_image_uri = 'gs://tripive.appspot.com/images/taj.jpg'
            # response = requests.get(url)
            # img = Image.open(BytesIO(response.content))
            # if isinstance(input_image_uri, six.binary_type):
            #     input_image_uri = input_image_uri.decode('utf-8')

            detected_landmk = detect_landmarks(file_name)   

            for landmark in detected_landmk:
                # print(landmark.description)
                data.update({
                    'landmark' : landmark.description
                })
                for location in landmark.locations:
                    lat_lng = location.lat_lng
                    data.update({
                        'Latitude' : lat_lng.latitude,
                        'Longitude': lat_lng.longitude
                    })
                    print('Latitude {}'.format(lat_lng.latitude))
                    print('Longitude {}'.format(lat_lng.longitude))
            # print(data)
            return {'landmarkdesc' : data}

        def get(self, resource_id):
                return {'prediction' : 'Returning list of prediction'}                                  

def detect_faces(path):
    """Detects faces in an image."""
    from google.cloud import vision
    import io
    client = vision_v1.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision_v1.types.Image(content=content)

    response = client.face_detection(image=image)
    faces = response.face_annotations

    # Names of likelihood from google.cloud.vision_v1.enums
    likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                       'LIKELY', 'VERY_LIKELY')
    print('Faces:')

    for face in faces:
        print('anger: {}'.format(likelihood_name[face.anger_likelihood]))
        print('joy: {}'.format(likelihood_name[face.joy_likelihood]))
        print('surprise: {}'.format(likelihood_name[face.surprise_likelihood]))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in face.bounding_poly.vertices])

        print('face bounds: {}'.format(','.join(vertices)))

@api_rest.route('/upload/faces/<string:resource_id>')          
class SecureVision(Resource):
        def post(self, resource_id):
            file_name = os.path.abspath('files/taj.jpg')
            detected_landmk = detect_faces(file_name)   
            return {'prediction' : 'prediction_text'}

        def get(self, resource_id):
                return {'prediction' : 'Returning list of prediction'}             

@api_rest.route('/upload/test/<string:resource_id>')          
class SecureVision(Resource):
        def post(self, resource_id):
            data = {}
            client = vision.ImageAnnotatorClient()
            response = client.annotate_image({
            'image': {'source': {'image_uri': 'gs://tripive.appspot.com/images/taj.jpg'}},
            'features': [{'type': vision.enums.Feature.Type.LABEL_DETECTION}], #Supported types see here https://cloud.google.com/vision/docs/batch#currently_supported_feature_types
            }) 
            # data.update({response.annotations})
            print(response)
            # return {'prediction' : data}

        def get(self, resource_id):
                return {'prediction' : 'Returning list of prediction'}    