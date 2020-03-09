FROM python:3.6.5-slim
LABEL maintainer="Kumindu Ranawaka, kirlogapanet@gmail.com"
RUN apt-get update
RUN mkdir /app
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
EXPOSE 5055
CMD ["python","manage.py" ]
