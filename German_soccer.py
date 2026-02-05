import streamlit as st
st.sidebar.image('germany_flag.jpg', use_container_width = True)

#Page setup
players = st.Page(
    page = 'views/Players.py',
    title = 'Germany Soccer Players',
    icon = '👤',
)
local = st.Page(
    page = 'views/Local_model.py',
    title = 'Local games',
    icon = '⚽'
)
visit = st.Page(
    page = 'views/Visit_model.py',
    title = 'Visit games',
    icon = '⚽',
)
me = st.Page(
    page = 'views/About_me.py',
    title = 'About me',
    icon = '👤',
)

#Navigation setup
pg = st.navigation(
    {'Information':[players,me],
     'Models':[visit,local]}
)
pg.run()