from flask import Flask, request, json

from utils import allowed_file
from gcp import get_text

app = Flask(__name__)


@app.route('/image', methods=['POST'])
def receive_img():

    if 'file' not in request.files:
        response = app.response_class(
            response='No image found',
            status=400,
            mimetype='application/json'
        )
        return response

    file = request.files['file']

    if file.filename == '':
        response = app.response_class(
            response='No image found',
            status=400,
            mimetype='application/json'
        )
        return response

    if file and allowed_file(file.filename):
        fileData = file.read()
        return get_text(fileData)

    return app.response_class(
            response='UnkwonError',
            status=500,
            mimetype='application/json'
        )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
