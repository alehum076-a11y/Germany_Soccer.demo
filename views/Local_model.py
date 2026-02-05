import streamlit as st

st.title('German games as local')
import pandas as pd

data = pd.read_csv('germany.csv', delimiter = ';')
data.columns = ['Estadio', 'Equipo_local', 'Equipo_visitante', 'Posesion_local', 'Posesion_visitante', 'Tiros_arco_local', 'Tiros_arco_visitante', 'Goles_local', 'Goles_visitante']
columns_to_drop = ['Estadio']
data.drop(columns_to_drop, axis = 'columns', inplace = True)
data['Dif'] = data['Goles_local']-data['Goles_visitante']
data_local = data[data['Equipo_local'] == 'Alemania']

st.dataframe(data_local.head(6))

X = data_local[['Posesion_local','Tiros_arco_local']]
y = data_local['Dif']

import matplotlib.pyplot as plt
st.subheader('Variable Relations')
fig, ax = plt.subplots(2)
ax[0].scatter(data_local['Posesion_local'],y,color = 'darkblue', alpha = 0.3)
ax[0].set_ylabel('Diferencia')
ax[1].scatter(data_local['Posesion_local'],data_local['Tiros_arco_local'],color = 'darkgray', alpha = 0.3)
ax[1].set_xlabel('Posesión local (Alemania)')
ax[1].set_ylabel('Tiros al arco (Alemania)')
st.pyplot(fig)

import seaborn as sns
import numpy as np
st.subheader('Histograma de goles Selección Alemana')
col1,col2 = st.columns(2)
with col1:
    fig2, ax = plt.subplots()
    sns.histplot(
        data = data_local,
        x = 'Dif',
        binwidth = 1
        )
    plt.xlabel('Points favor to Germany')
    plt.ylabel('Count of Points')
    st.pyplot(fig2)
with col2:
    fig3,ax = plt.subplots()
    sns.kdeplot(
        data = data_local,
        x = 'Dif'
        )
    plt.ylabel('Probability')
    plt.xlabel('Diference of Points')
    st.pyplot(fig3)

test_size_value = st.slider('Test size',
                                      min_value = np.float64(0.2),
                                      max_value = np.float64(0.8),
                                      step = np.float64(0.1))
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = test_size_value, random_state=9)

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

Mean_team = data_local.groupby('Equipo_visitante')[['Posesion_local','Tiros_arco_local']].mean()
country =  st.selectbox('Selección de equipo',Mean_team.index.tolist())

if st.button('Predecir Resultado'):
    features = Mean_team.loc[[country]]
    y_pred = tree.predict(features)
    st.write('The diference of points is : ',y_pred)
    if y_pred <= 0:
         st.write('Germany loss')
    else:
         st.write('Germany win')

    fig3,ax = plt.subplots(2,1)
    ax[0].scatter(Mean_team.loc[country, 'Posesion_local'], y_pred, color = '#292266')
    ax[0].set_ylabel('Goles a favor de Alemania')
    ax[1].scatter(Mean_team.loc[country, 'Tiros_arco_local'], y_pred, color = '#080759')
    ax[1].set_xlabel('Tiros al arco a favor de Alemania')
    st.pyplot(fig3)