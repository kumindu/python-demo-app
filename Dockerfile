FROM tiangolo/uwsgi-nginx-flask:python3.7
RUN pip install -r requirements.txt
COPY ./app /app