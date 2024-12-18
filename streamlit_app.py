import streamlit as st
import pandas as pd

st.title('Machine Learning App')

st.write('This is a ml app!')

df = pd.read_csv('https://raw.githubusercontent.com/cnrkr-dev/data/master/penguins_cleaned.csv')
df
