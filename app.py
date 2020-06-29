import numpy as np
from flask import Flask, request, jsonify, render_template
import ktrain

                                     
app = Flask(__name__)
model = ktrain.load_predictor(fpath=F"ubuntu/model")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [(x) for x in request.form.values()]
    prediction = model.predict(int_features)

    return render_template('index.html', prediction_text='The ticket belong to category  {}'.format(prediction))


#if __name__ == "__main__":
  #  app.run(debug=True)
    
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)