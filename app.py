import streamlit as st

st.title('CampusX')

col1, col2 = st.columns(2)

with col1:
    st.image('ai.jpeg')
with col2:
    st.write("""Name: Monir Khan
Institute: Dhaka university
Department :statistics and data science ( cse and math related subject)
Year: 2022-2023(3rd year in University)""")