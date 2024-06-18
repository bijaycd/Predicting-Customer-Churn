from flask import Flask, render_template, request,jsonify,Request
from pickle4 import pickle

app = Flask(__name__,template_folder='template')

model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

@app.route('/', methods=['GET'])
def Home():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        CreditScore = int(request.form['CreditScore'])
        Age = int(request.form['Age'])
        Tenure = int(request.form['Tenure'])
        Balance = float(request.form['Balance'])
        NumOfProducts = int(request.form['NumOfProducts'])
        HasCrCard = int(request.form['HasCrCard'])
        IsActiveMember = int(request.form['IsActiveMember'])
        EstimatedSalary = float(request.form['EstimatedSalary'])

        Geography = request.form['Geography']
        if(Geography == 'France'):
            Geography = 0        
        elif(Geography == 'Germany'):
            Geography = 1
        else:
            Geography = 2

        Gender = request.form['Gender']
        if(Gender == 'Male'):
            Gender = 1
        else:
            Gender = 0

        prediction = model.predict([[CreditScore,Age,Tenure,Balance,NumOfProducts,HasCrCard,IsActiveMember,EstimatedSalary,Geography,Gender]])
        if prediction==1:
             return render_template('home.html',prediction_text="The Customer will leave the bank")
        else:
             return render_template('home.html',prediction_text="The Customer will not leave the bank")
                
if __name__=="__main__":
    app.run(debug=True)