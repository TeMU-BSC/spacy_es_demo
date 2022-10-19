FROM python:3.8-slim

RUN mkdir /home/es_demo

COPY spacy_streamlit-1.0.4-py38-none-any.whl streamlit_app.py /home/es_demo/


WORKDIR /home/es_demo

RUN apt-get update && apt-get install -y unzip wget

RUN python -m pip install spacy streamlit

RUN python -m  pip install /home/es_demo/spacy_streamlit-1.0.4-py38-none-any.whl

RUN python -m  pip install https://huggingface.co/spacy/es_dep_news_trf/resolve/main/es_dep_news_trf-any-py3-none-any.whl

RUN python -m  pip install https://huggingface.co/spacy/es_core_news_md/resolve/main/es_core_news_md-any-py3-none-any.whl

#streamlit run streamlit_app.py --server.port 8081 --theme.font serif --browser.serverPort 8081 --browser.serverAddress http://aina.bsc.es
ENTRYPOINT ["streamlit", "run", "streamlit_app.py", "--server.port 8084", "--theme.font serif", "--browser.serverPort 8084"]
