import streamlit as st
import pandas as pd

st.title('Machine Learning App')

st.write('This is a ml app!')

with st.expander('Data'):
  st.write('**Raw data**')
  df = pd.read_csv('https://raw.githubusercontent.com/cnrkr-dev/data/master/penguins_cleaned.csv')
  df

with st.expander('Data visualization'):
  st.scatter_chart(data=df, x='bill_length_mm', y='body_mass_g', color='species')
