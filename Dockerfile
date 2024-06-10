FROM python

WORKDIR /modirSakhteman
RUN pip3 install --upgrade pip 

COPY ./requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
EXPOSE 8000

RUN openssl req -new -newkey rsa:2048 -days 365 -nodes -x509 -subj "/C=IR/ST=TH/L=TH/O=TCT/OU=TMN/CN=home.local" -keyout cert.key  -out cert.crt

CMD ["python3","manage.py","runserver_plus","0:8000","--cert-file","cert.crt","--key-file","cert.key"]
