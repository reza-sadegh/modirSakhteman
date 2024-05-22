FROM python

# RUN apt-get update && apt-get install -y python3.10 python3.10-dev
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

WORKDIR /modirSakhteman
RUN pip3 install --upgrade pip 

COPY ./requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
EXPOSE 8000

# RUN python3 manage.py migrate  --noinput

CMD ["python3","manage.py","runserver","0.0.0.0:8000"]