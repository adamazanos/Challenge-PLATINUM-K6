import re

from flask import Flask, jsonify

app = Flask(__name__)

from flask import request
from flasgger import Swagger, LazyString, LazyJSONEncoder
from flasgger import swag_from

app.json_encoder = LazyJSONEncoder
swagger_template = dict(
    info = {
        'title': LazyString(lambda: 'API Documentation for Data Processing and Modeling Binar Challenge 1 platinum'),
        'version': LazyString(lambda: '1.0.0'),
        'description': LazyString(lambda: 'Dokumentasi API untuk Data Processing dan Modeling Binar Challenge 1 platinum')
    },
    host = LazyString(lambda: request.host)
)
swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'docs',
            "route": '/docs.json'
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/docs/"
}
swagger = Swagger(app, template=swagger_template,config=swagger_config)

@swag_from("docs/hello_world.yml", methods=['GET'])
@app.route('/', methods=['GET'])
def hello_world():
    json_response = {
        'status_code': 200,
        'description': "Test Hello World",
        'data': "Hello World"
    }

    response_data = jsonify(json_response)
    return response_data

@swag_from("docs/text.yml", methods=['GET'])
@app.route('/text', methods=['GET'])
def text():
    json_response = {
        'status_code': 200,
        'description': "Original Teks",
        'data': "Halo, apa kabar semua?"
    }

    response_data = jsonify(json_response)
    return response_data

@swag_from("docs/text_processing.yml", methods=['POST'])
@app.route("/text/", methods=['POST'])
def text_processing():
    text = request.form.get('text')
    text_clean= cleansing.data_prepocessing(text)
    response_data = jsonify(text_clean)
    return response_data

@swag_from("docs/file_processing.yml", methods=['POST'])
@app.route("/file/", methods=['POST'])
def file_processing():
    file = request.files['file']
    df = pd.read_csv(file, encoding=('ISO-8859-1'))
    cleansing.data_prepocessing(df)
    return jsonify(df)


if __name__ == '__main__':
    app.run()
