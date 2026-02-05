import streamlit as st

col1, col2, col3 = st.columns([1, 2, 1]) 
with col1:
    st.image('enca.jpg', width = 320)
with col2:
    st.image("me4.jpeg", width = 300)
st.markdown(
    "<h5 style = 'text-align: center;'> Elaborated by Agribusiness Analyst -Alejandro Molina- </h5>",
    unsafe_allow_html = True)
with col3:
    st.image('zamo.png', width = 320)

col4, col5= st.columns(2, vertical_alignment = 'center') 
with col4:
    st.subheader('Who I am?')
    st.write(
        """
        - Christian guy
        - Entrepreneur Agribusiness
        - Honest & Worker
        - Paloma '27
        - Alejandro José Mora Molina
        """
    )
    
with col5:
    st.subheader('Experience & Studies', anchor = False)
    st.write(
        """
        - Escuela Nacional Central de Agricultura [ENCA]
        - Python & Data visualization [DATACAMP]
        - Machine Learning -Agro Data Science- [PLATZI]
        - Agribusiness [Zamorano University]
        """
    )


st.write('This page may help you to take decisions and predict the results, App based in Statistics & Machine Learning.  Paloma 27')

st.markdown(
    "<h3 style = 'text-align: center;'> Germany Soccer Team will win! </h3>",
    unsafe_allow_html = True)