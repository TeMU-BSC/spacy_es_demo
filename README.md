
## Prerequisites

Make

[Docker](https://docs.docker.com/engine/install/ubuntu/)

[Docker compose](https://docs.docker.com/compose/install/)


### Setup local environment
Create and activate a python 3.8 virtual environment

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements in python3.8

```bash
pip install -r requirements.txt
```

Run demo with
```bash
LANG=es streamlit run streamlit_app.py --server.port 8081 --theme.font serif --browser.serverPort 8081
```

## Deploy via docker compose

To deploy this project run

```bash
make deploy
```