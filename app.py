#%%writefile app.py

import pickle
import streamlit as st
from sklearn.ensemble import RandomForestClassifier

# loading the trained model
pickle_in = open('rf.pkl', 'rb')
classifier = pickle.load(pickle_in)

@st.cache()

def predict(temperature,bpm):
    input_data = [[bpm, temperature]]
    prediction=classifier.predict(input_data)
    return prediction


def main():
    # front end elements of the web page
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">스마트 워치를 사용한 감정추론</h1> 
    </div> 
    """

    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html=True)

    temperature = st.number_input("Body Temperature")
    bpm = st.number_input("Beats per Minute")
    result=""

    if st.button("Predict"):
        result = predict(temperature, bpm)
        st.success('Your emotion is {}'.format(result))

if __name__ == '__main__':
    main()
