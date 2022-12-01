FROM python:3.8-slim

#RUN mkdir /home/spacy_demo

RUN apt-get update && apt-get install --no-install-recommends -y git && \
     rm -rf /var/lib/{apt,dpkg,cache,log}

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /usr/src/app

COPY .streamlit /usr/src/app/.streamlit

COPY requirements.txt streamlit_app.py ./

RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir  --upgrade -r requirements.txt


ENTRYPOINT ["streamlit", "run", "streamlit_app.py", "--server.port", "8081", "--browser.serverAddress", "0.0.0.0"]
