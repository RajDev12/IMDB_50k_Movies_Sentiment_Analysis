import streamlit as st
import pickle
import pandas as pd
import tensorflow.keras as keras

st.title("Sentiment Analysis")
# pipe=pickle.load(open('LSTM_model.pkl','rb'))
# model = keras.models.load_model('LSTM_model.pkl')
col1=st.columns(1)
with col1:
    new_review=st.text_input('New_review')