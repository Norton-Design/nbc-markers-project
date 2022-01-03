import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.http import HTTP_STATUS_CODES
from werkzeug.datastructures import ImmutableMultiDict

app = Flask(__name__)
CORS(app, expose_headers='Authorization')

@app.route('/upload', methods=["POST"])
def file_upload():
    file = request.files.get('file')
    # call the validate_markers_file function here
    if file:
        print('is the file true?')
        print(file.filename)
    return bad_request('testing things')

def bad_request(message):
    return error_response(400, message)

def error_response(code, message=None):
    payload = {
        'error': HTTP_STATUS_CODES.get(code, "Unknown error")
    }
    if message:
        payload['message'] = message
    response = jsonify(payload)
    response.status_code = code
    return response