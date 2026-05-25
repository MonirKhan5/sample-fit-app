import streamlit as st

st.title('CampusX')

col1, col2 = st.columns(2)

with col1:
     st.image('ai2.jpeg')
with col2:
    st.write("""Name:Monir Khan
Institute: Dhaka university
Department :statistics and data science ( cse and math related subject)
Year: 2022-2023(3rd year in University)""")

st.header('Courses offered')
st.subheader('Data Science and Machine Learning')
st.subheader('Data Analysis')
st.subheader('Python')
st.subheader('SQL')
st.subheader('DSA')

st.sidebar.title('Menu')
st.sidebar.markdown("""
- Home
- About
- Contact
- Career
- Login
""")


option = st.sidebar.selectbox('Select one',['Teacher','Student'])
btn = st.sidebar.button('Select')

if btn:
    st.title('hello' + option)

