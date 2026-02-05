import streamlit as st
import pandas as pd
st.title('German games as visit')

data = pd.read_csv('germany.csv', delimiter = ';')
data.columns = ['Estadio', 'Equipo_local', 'Equipo_visitante', 'Posesion_local', 'Posesion_visitante', 'Tiros_arco_local', 'Tiros_arco_visitante', 'Goles_local', 'Goles_visitante']
columns_to_drop = ['Estadio']
data.drop(columns_to_drop, axis = 'columns', inplace = True)
data['Dif'] = data['Goles_visitante']-data['Goles_local']
data_visit = data[data['Equipo_visitante'] == 'Alemania']

st.dataframe(data_visit.head(6))

X = data_visit[['Posesion_visitante','Tiros_arco_visitante']]
y = data_visit['Dif']

import matplotlib.pyplot as plt
st.subheader('Variable Relations')
fig, ax = plt.subplots(2)
ax[0].scatter(data_visit['Posesion_local'],y,color = 'skyblue', alpha = 0.3)
ax[0].set_ylabel('Diferencia')
ax[1].scatter(data_visit['Posesion_visitante'],data_visit['Tiros_arco_visitante'],color = 'darkgray', alpha = 0.3)
ax[1].set_xlabel('Posesión visitante (Alemania)')
ax[1].set_ylabel('Tiros al visitante (Alemania)')
st.pyplot(fig)

import seaborn as sns
import numpy as np
st.subheader('Histograma de goles Selección Alemana')
col1,col2 = st.columns(2)
with col1:
    fig2, ax = plt.subplots()
    sns.histplot(
        data = data_visit,
        x = 'Dif',
        binwidth = 1
        )
    plt.xlabel('Points favor to Germany')
    plt.ylabel('Count of Points')
    st.pyplot(fig2)
with col2:
    fig3,ax = plt.subplots()
    sns.kdeplot(
        data = data_visit,
        x = 'Dif'
        )
    plt.ylabel('Probability')
    plt.xlabel('Diference of Points')
    st.pyplot(fig3)

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2, random_state=9)

from sklearn.tree import DecisionTreeRegressor
tree = DecisionTreeRegressor()
tree.fit(X_train,y_train)
y_test_cal = tree.predict(X_test)

from sklearn.metrics import r2_score
r2 = r2_score(y_test,y_test_cal)
st.write('- _r2 value_ according your test size is: ',r2)

st.markdown(
    "<h5 style = 'text-align: center;'> Select the opponent </h5>",
    unsafe_allow_html = True)

Mean_team = data_visit.groupby('Equipo_local')[['Posesion_visitante','Tiros_arco_visitante']].mean()
country =  st.selectbox('Selección de equipo',Mean_team.index.tolist())

if st.button('Predecir Resultado'):
    features = Mean_team.loc[[country]]
    y_pred = tree.predict(features)
    st.write('The diference of points is : ',y_pred)
    if y_pred <= 0:
         st.write('Germany loss -GAME OVER')
    else:
         st.write('Germany win -WIN-')

    fig3,ax = plt.subplots(2,1)
    ax[0].scatter(Mean_team.loc[country, 'Posesion_visitante'], y_pred, color = '#292266')
    ax[0].set_ylabel('Goles a favor de Alemania')
    ax[1].scatter(Mean_team.loc[country, 'Tiros_arco_visitante'], y_pred, color = '#080759')
    ax[1].set_xlabel('Tiros al arco a favor de Alemania')
    st.pyplot(fig3)