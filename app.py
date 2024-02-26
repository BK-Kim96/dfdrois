#%%writefile app.py

import pickle
import streamlit as st

# loading the trained model
pickle_in = open('rf.pkl', 'rb')
classifier = pickle.load(pickle_in)

@st.cache()

def prediction(temperature,bpm):
    prediction=rf.predict(temperature,bpm)
    return prediction


def main():
    # front end elements of the web page
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
