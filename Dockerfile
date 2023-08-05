FROM python:3.10

WORKDIR /app
ADD app/ main.py

# RUN pip install pipenv && pipenv install --system --deploy --ignore-pipfile && \
#     apt-get update && apt-get install -y wget && apt-get install -y curl

RUN pip install fastapi && pip install uvicorn


CMD [ "python", "main.py" ]