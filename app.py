#%%writefile app.py

import pickle
import streamlit as st
from sklearn.ensemble import RandomForestClassifier
from flask import Flask
from flask_restful import Resource, Api, reqparse

# loading the trained model
pickle_in = open('rf.pkl', 'rb')
classifier = pickle.load(pickle_in)


@st.cache()

def prediction(temperature,bpm):
    input_data = [[bpm, temperature]]
    prediction=classifier.predict(input_data)
    return prediction


def main():
    # front end elements of the web page
    app = Flask(__name__)
    api = Api(app)
    
    class RegistUser(Resource):
        def post(self):
           
            parser = reqparse.RequestParser()
            parser.add_argument('TEMP', type=float)
            parser.add_argument('HR', type=float)
            parser.add_argument('RMSSD', type=float)
            args = parser.parse_args()
            temp = args['TEMP']
            hr = args['HR']
            rmssd = args['RMSSD']
            emotion = prediction(temp,hr)
            return {'predict emotion': emotion}
    
    api.add_resource(RegistUser, '/emotion')


    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Streamlit Loan Prediction ML App</h1> 
    </div> 
    """

    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html=True)

    temperature = st.number_input("Body Temperature")
    bpm = st.number_input("Beats per Minute")
    result=""

    if st.button("Predict"):
        result = prediction(temperature, bpm)
        st.success('Your emotion is {}'.format(result))

if __name__ == '__main__':
    main()
