FROM python:3.8-slim

#RUN mkdir /home/spacy_demo

RUN apt-get update && apt-get install --no-install-recommends -y git && \
     rm -rf /var/lib/{apt,dpkg,cache,log}

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /usr/src/app

COPY .streamlit /usr/src/app/.streamlit

COPY requirements.txt streamlit_app.py ./

RUN pip install --no-cache-dir -r requirements.txt

#COPY . .

#RUN python -m  pip install spacy_streamlit-1.0.4-py38-none-any.whl

#RUN python -m  pip install https://huggingface.co/spacy/es_dep_news_trf/resolve/main/es_dep_news_trf-any-py3-none-any.whl

#RUN python -m  pip install https://huggingface.co/spacy/es_core_news_md/resolve/main/es_core_news_md-any-py3-none-any.whl

#streamlit run streamlit_app.py --server.port 8081 --theme.font serif --browser.serverPort 8081 --browser.serverAddress http://aina.bsc.es
ENTRYPOINT ["streamlit", "run", "streamlit_app.py", "--server.port", "8081", "--browser.serverAddress", "0.0.0.0"]
