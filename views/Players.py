import streamlit as st

st.markdown(
    "<h3 style = 'text-align: center;'> German Soccer Players to World Cup 2026 </h3>",
    unsafe_allow_html = True)

col1,col2,col3 = st.columns(3)
with col1:
    st.image('Joshua.jpg',width=320)
    st.subheader('Joshua Kimich')
    st.write(
        """
        - 30 Years old
        - Middle center [Captain]
        - FC Bayer Múnchen
        """
    )
with col2:
    st.image('Nick.jpg',width=320)
    st.subheader('Nick Woltemade')
    st.write(
        """
        - 23 Years old
        - Middle offensive
        - Newcastle United
        """
    )

with col3:
    st.image('Wirtz.jpeg',width=320)
    st.subheader('Florian Wirtz')
    st.write(
        """
        - 22 Years old
        - Middle offensive
        - Liverpol FC
        """
    )

col4, col5, col6 = st.columns(3)
with col4:
    st.image('David.jpeg',width=320)
    st.subheader('David Raum')
    st.write(
        """
        - 27 Years old
        - Left-back
        - RB Leipzig
        """
    )
with col5:
    st.image('goretzka.jpg',width=320)
    st.subheader('Leon Goretzka')
    st.write(
        """
        - 30 Years old
        - Middle center
        - FC Bayer Múnich
        """
    )
with col6:
    st.image('Sane.jpg',width=320)
    st.subheader('Leroy Sané')
    st.write(
        """
        - 30 Years old
        - Right-back
        - Galatasaray
        """
    )
st.image('germany.jpg')