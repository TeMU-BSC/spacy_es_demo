#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 10 09:16:13 2021

@author: crodri
"""

import spacy_streamlit
import streamlit as st
from spacy_streamlit.util import Demotype

models = ["es_bsc_demo_trf", "es_bsc_demo_md", "es_core_news_md", "es_dep_news_trf"]  # ,"ca_core_news_lg","ca_core_news_trf"]
st.set_page_config(page_title="Modelos Spacy castellano", header_title="Spacy", menu_items={
    'Get Help': 'https://huggingface.co/PlanTL-GOB-ES',
    'Report a bug': 'https://github.com/TeMU-BSC/spacy_es_demo/issues',
    'About': None,

}, layout='wide', initial_sidebar_state='auto')
default_text = "El Fútbol Club Barcelona, conocido popularmente como Barça, es una entidad polideportiva con sede en Barcelona, España."
st.markdown("## Demo de las cadenas de Spacy 3.4 en castellano")
st.markdown("#### *Elegir un modelo en la columna de la izquierda*")
visualizers = ["ner", "similarity", "tokens", "parser", "textcat"]
similarity_texts = ('gato', 'perro')
spacy_streamlit.visualize(models, default_text, visualizers, similarity_texts=('perro', 'gato'),
                          show_visualizer_select=True, sidebar_title="Visualización modelos Spacy-PlanTL",
                          sidebar_description="Es posible elegir el modelo y la funcionalidad para la demostración",
                          demo_type=Demotype.PLANTL,
                          models_download_name_links=[{"name": "es_bsc_demo_trf",
                                                       "link": "https://huggingface.co/PlanTL-GOB-ES/es_bsc_demo_trf"}, {"name": "es_bsc_demo_md",
                                                       "link": "https://huggingface.co/PlanTL-GOB-ES/es_bsc_demo_md"}]
                          )
# streamlit run streamlit_app.py --server.port 8081 --theme.font serif --browser.serverPort 8081 --browser.serverAddress http://aina.bsc.es