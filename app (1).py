import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from st_on_hover_tabs import on_hover_tabs

st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align: center; color: black;'><em>Wild Code School 2025</em><br><strong>Projet 2 - IMDb</strong></h1>", unsafe_allow_html=True)
css = '''
<style>
    section[data-testid='stSidebar'] {
        background-color: #111;
        min-width: unset !important;
        width: unset !important;
        flex-shrink: unset !important;
    }

    button[kind="header"] {
        background-color: transparent;
        color: rgb(180, 167, 141);
    }

    @media(hover) {
        header[data-testid="stHeader"] {
            display: none;
        }

        section[data-testid='stSidebar'] > div {
            height: 100%;
            width: 95px;
            position: relative;
            z-index: 1;
            top: 0;
            left: 0;
            background-color: #111;
            overflow-x: hidden;
            transition: 0.5s ease;
            padding-top: 60px;
            white-space: nowrap;
        }

        section[data-testid='stSidebar'] > div:hover {
            width: 310px;
        }

        button[kind="header"] {
            display: none;
        }
    }

    @media(max-width: 272px) {
        section[data-testid='stSidebar'] > div {
            width: 15rem;
        }
    }
</style>
'''
st.markdown(css, unsafe_allow_html=True)


with st.sidebar:
    tabs = on_hover_tabs(tabName=['Présentation', 'Le Nord', 'Exploration', 'KPI',"Machine Learning","Axes d'amélioration"], 
                         iconName=['co_present', 'signpost', 'dashboard', 'data_thresholding','select_all','tips_and_updates'], default_choice=0)
	
if tabs =='Présentation':
    st.title('Bienvenue sur le Streamlit de notre projet')

    st.header("Nous sommes Dath solutions et notre équipe est composée de :")
    st.html(
    """<ul>
        <li>Thomas</li>
        <li>Halim</li>
        <li>Arnaud</li>
        <li>David</li>
    </ul>"""
    )
 

    st.write("Nous avons été contactés par un directeur de cinéma éprouvant des difficultés à relancer son activité.")

    st.header("Technos utilisées pour l'organisation et la réalisation du projet :")
    
    col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
    
    with col1 :	
        st.image("logo slack.PNG")
    with col2 :	
        st.image("logo imdb.PNG")
    with col3 :	
        st.image("logo tmdb.PNG")
    with col4 :	
        st.image("logo python.PNG")
    with col5 :	
        st.image("logo pandas.PNG")
    with col6 :	
        st.image("logo vscode.PNG")
    with col7 :	
        st.image("logo scikit-learn.PNG")
    with col8 :	
        st.image("logo streamlit.PNG")

elif tabs == 'Le Nord':
    st.title("Le département du Nord")

elif tabs == 'Exploration':
    st.title("Analysede marché")
    st.write('''Pour répondre au besoin de notre client, nous avons réalisé une étude de marché, 
             où nous sommes partie récupérer des données csv, excel et autres format afin de pouvoir trouver la spécialisation du cinéma''')

elif tabs == 'KPI':
    st.title("KPI à suivre")

elif tabs == 'Machine Learning':
    st.title("Machine Learning")

elif tabs == "Axes d'amélioration":
    st.title("Axes d'amélioration de notre livrable")

