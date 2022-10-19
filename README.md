

Se instala nuestra versión de streamlit-spacy, que permite ordenar de mayor a menor la ponderación de los clasificadores

pip install spacy_streamlit-1.0.4-py38-none-any.whl --no-cache-dir 

!pip install https://huggingface.co/spacy/es_dep_news_trf/resolve/main/es_dep_news_trf-any-py3-none-any.whl


Ejecutar así:

streamlit run streamlit_app.py --server.port 8081 --theme.font serif --browser.serverPort 8081 --browser.serverAddress http://plantl.bsc.es
