from flask import Flask,request
from main import generateAI
import pickle

generateAI()
ai=pickle.load(open('model.pkl','rb'))

app=Flask(__name__)

@app.route('/')
def home():
return('AI Model Server is Running')

@app.route('/predict',methods=['GET'])
def predict():
    temp=request.args.get('temp')
    temp=float(temp)
    data=[[temp]]
    result=ai.predict(data)
    result=result[ø]
    return (result)

if(_name _== "_main_"):
app.run(host='0.0.0.0',port=5000,debug=True)
