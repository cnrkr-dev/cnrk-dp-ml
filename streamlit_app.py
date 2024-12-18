import streamlit as st
import pandas as pd

st.title('Machine Learning App')

st.write('This is a ml app!')

df = pd.read_csv('https://github.com/cnrkr-dev/data/master/main/penguins_cleaned.csv')
df
