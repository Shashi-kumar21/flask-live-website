# from flask import Flask, render_template, request
# import pickle

# app = Flask(__name__)
# # load the model
# model = pickle.load(open('AIIMS_modelN.sav', 'rb'))

# @app.route('/')
# def home():
#     result = ''
#     return render_template('index.htm', **locals())


# @app.route('/predict', methods=['POST', 'GET'])
# def predict():
#     bnp= float(request.form['bnp'])
#     age = int(request.form['age'])
#     BUrea= float(request.form['BUrea'])
#     SGOT= float(request.form['SGOT'])
#     SGPT= float(request.form['SGPT'])
#     result = model.predict([[bnp,age, BUrea, SGOT, SGPT]])[0]
#     return render_template('index.htm', **locals())

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
# load the model
model = pickle.load(open('JSS_modelN.sav', 'rb'))

@app.route('/')
def home():
    result = ''
    return render_template('index2.htm', **locals())

@app.route('/predict', methods=['POST', 'GET'])
@app.route('/predict', methods=['POST', 'GET'])
def predict():
    Age = int(request.form['Age'])
    Weight = float(request.form['Weight'])
    Orthopnoea = int(request.form['Orthopnoea'])
    T2DM = int(request.form['T2DM'])
    HTN = int(request.form['HTN'])
    IHD = int(request.form['IHD'])
    PVD_PAD = int(request.form['PVD_PAD'])
    Obesity = int(request.form['Obesity'])
    ECHO = float(request.form['ECHO'])
    Ejection_Fraction = float(request.form['Ejection_Fraction'])
    features = [[Age, Weight, Orthopnoea, T2DM, HTN, IHD, PVD_PAD, Obesity, ECHO, Ejection_Fraction]]
    prediction = model.predict(features)[0]
    if prediction == 1:
        result = 1
    else:
        result = 0
    return render_template('index2.htm', result=result)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
