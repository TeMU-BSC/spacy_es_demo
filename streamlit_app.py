#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 10 09:16:13 2021

@author: crodri
"""

import spacy_streamlit
import streamlit as st

models = ["es_core_news_md", "es_dep_news_trf"]  # ,"ca_core_news_lg","ca_core_news_trf"]
st.set_page_config(page_title="Modelos Spacy castellano", page_icon="aina_small.jpg", layout='wide',
                   initial_sidebar_state='auto')
default_text = "Los últimos datos confirman una buena evolución de la pandemia en España."
st.title("Demo de las cadenas de Spacy 3.4 en castellano")
st.subheader("*Elegir un modelo en la columna de la derecha*")
visualizers = ["ner", "similarity", "tokens", "parser", "textcat"]
similarity_texts = ('gato', 'perro')
spacy_streamlit.visualize(models, default_text, visualizers, similarity_texts=('perro', 'gato'),
                          show_visualizer_select=True, sidebar_title="Visualización modelos Spacy-PlanTL",
                          sidebar_description="Es posible elegir el modelo y la funcionalidad para la demostración")
# streamlit run streamlit_app.py --server.port 8081 --theme.font serif --browser.serverPort 8081 --browser.serverAddress http://aina.bsc.es
