#import package dan konfigurasi swagger

import re, pickle
import pandas as pd

from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

from flask import request
from flasgger import Swagger, LazyString, LazyJSONEncoder
from flasgger import swag_from
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from keras.models import load_model

import numpy as np


app.json_encoder = LazyJSONEncoder
swagger_template = dict(
    info = {
        'title': LazyString(lambda: 'Platinum Challange API Documentation'),
        'version': LazyString(lambda: '1.0.0'),
        'description': LazyString(lambda: 'Dokumentasi API Sentiment Analysist dengan Model LSTM dan Neural Network')
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

#mendefinisikan function untuk cleansing
import cleansing
sentiment = ['negative', 'neutral', 'positive']

def get_sent(sent):
    if sent==0:
        sent='negative'
    elif sent==1:
        sent='neutral'
    else: sent='positive'
    return sent

file_tokenizer = open('tokenizer.pickle', 'rb')
# max_features = 100000
# tokenizer = Tokenizer(num_words=max_features, split=' ', lower=True)
file_sequencer = open('x_pad_sequences.pickle', 'rb')

#load file
load_tokenizer = pickle.load(file_tokenizer)
load_sequencer = pickle.load(file_sequencer)
file_sequencer.close()
model_lstm = load_model('model_lstm.h5')
model_nn = load_model('model_nn.h5')

#lstm route (text input)
@swag_from("docs/lstm.yml", methods=['POST'])
@app.route('/lstm', methods=['POST'])
def lstm():

    string = request.form.get('text')
    clean_string = cleansing.data_prepocessing(string)

    # feature = tokenizer.texts_to_sequences(clean_string)
    feature = load_tokenizer.texts_to_sequences(clean_string)
    feature = pad_sequences(feature, maxlen=load_sequencer.shape[1])

    prediction = model_lstm.predict(feature)
    get_sentiment = sentiment[np.argmax(prediction[0])]

    json_response = {
        'status_code': 200,
        'text_clean': clean_string,
        'sentiment': get_sentiment
    }

    response_data = jsonify(json_response)
    return response_data

#lstm route (file upload)
@swag_from("docs/lstm_upload.yml", methods=['POST'])
@app.route('/lstm_upload', methods=['POST'])
def lstm_upload():

    df= pd.read_csv(request.files.get('file'), encoding=('ISO-8859-1'))
    tweet= df['Tweet']
    data_processed= []
    for text in tweet:
        text = cleansing.data_prepocessing(text)
        data_processed.append(text)

    # feature = tokenizer.texts_to_sequences(clean_string)
    feature = load_tokenizer.texts_to_sequences(data_processed)
    feature = pad_sequences(feature, maxlen=load_sequencer.shape[1])

    prediction = model_lstm.predict(feature)
    get_sentiment = np.argmax(prediction, axis=1)
    get_sentiment = get_sentiment.reshape(-1,1)
    
    get= []
    for text in get_sentiment:
        sent= get_sent(text)
        get.append(sent)
        
    json_response = {
        'text_clean': data_processed,
        'sentiment': get,
        'status_code': 200
    }

    response_data = jsonify(json_response)
    return response_data

#neural network route (text input)
@swag_from("docs/nn.yml", methods=['POST'])
@app.route('/nn', methods=['POST'])
def nn():

    string = request.form.get('text')
    clean_string = cleansing.data_prepocessing(string)

    # feature = tokenizer.texts_to_sequences(clean_string)
    feature = load_tokenizer.texts_to_sequences(clean_string)
    feature = pad_sequences(feature, maxlen=load_sequencer.shape[1])

    prediction = model_nn.predict(feature)
    get_sentiment = sentiment[np.argmax(prediction[0])]
    
    json_response = {
        'status_code': 200,
        'text_clean': clean_string,
        'sentiment': get_sentiment
    }

    response_data = jsonify(json_response)
    return response_data

#nn route (file upload)
@swag_from("docs/nn_upload.yml", methods=['POST'])
@app.route('/nn_upload', methods=['POST'])
def nn_upload():

    df= pd.read_csv(request.files.get('file'), encoding=('ISO-8859-1'))
    tweet= df['Tweet']
    data_processed= []
    for text in tweet:
        text = cleansing.data_prepocessing(text)
        data_processed.append(text)

    # feature = tokenizer.texts_to_sequences(clean_string)
    feature = load_tokenizer.texts_to_sequences(data_processed)
    feature = pad_sequences(feature, maxlen=load_sequencer.shape[1])

    prediction = model_nn.predict(feature)
    get_sentiment = np.argmax(prediction, axis=1)
    get_sentiment = get_sentiment.reshape(-1,1)
    
    get= []
    for text in get_sentiment:
        sent= get_sent(text)
        get.append(sent)
        
    json_response = {
        'text_clean': data_processed,
        'sentiment': get,
        'status_code': 200
    }

    response_data = jsonify(json_response)
    return response_data

if __name__ == '__main__':
    app.run(debug=True)