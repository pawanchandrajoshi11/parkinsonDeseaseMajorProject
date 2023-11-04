
import numpy as np
from flask import Flask, request, render_template
import pickle
import pandas as pd


app = Flask(__name__)


model = pickle.load(open('static/model.pkl', 'rb'))
maxi = [1.00000000e+00, 9.07660000e-01, 8.52640000e-01, 8.71230000e-01,
       9.07000000e+02, 9.05000000e+02, 1.29655760e-02, 3.48253600e-03,
       2.77500000e-02, 2.56480000e-04, 1.10500000e-02, 1.83200000e-02,
       3.31500000e-02, 8.39083485e+01, 8.63161759e+01, 9.99382000e-01,
       7.61696000e-01]

mini = [0.00000000e+00, 4.15510000e-02, 5.43500000e-01, 1.54300000e-01,
       2.00000000e+00, 1.00000000e+00, 2.10708900e-03, 1.06000000e-05,
       2.10000000e-04, 6.86000000e-07, 2.00000000e-05, 5.00000000e-05,
       5.00000000e-05, 2.86515288e+01, 4.41334920e+01, 5.89609000e-01,
       6.18000000e-04]

#use the route() decorator to tell Flask what URL should trigger our function.
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    int_features = [x for x in request.form.values()] 
    print(int_features)
    int_features = [float(x.strip()) for x in int_features]
    int_features = [(x-mini[i])/(maxi[i]-mini[i]) for i,x in enumerate(int_features)]

    features = [np.array(int_features)]  #Convert to the form [[a, b]] for input to the model
    prediction = model.predict(features)  # features Must be in the form [[a, b]]
    print(prediction)
    if prediction[0] == 0:
        result = 'No Disease'
    else:
        result = 'Parkinson Disease'

    return render_template('index.html', prediction_text='{}'.format(result))


if __name__ == "__main__":
    app.run()