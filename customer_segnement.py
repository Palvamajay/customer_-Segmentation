import pandas as pd
import streamlit as st

data = pd.read_excel('marketing_campaign1.xlsx')

option = st.selectbox(
    'Show',
    ('head', 'tail', 'sample')
)

number = st.slider('number of rows', 1, 100, 5)

if option == 'head':
    st.write(data.head(number))
elif option == 'tail':
    st.write(data.tail(number))
elif option == 'sample':
    st.write(data.sample(number))
