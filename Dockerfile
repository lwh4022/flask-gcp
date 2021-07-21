FROM python:3.8.5

WORKDIR /home

COPY . .

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8080

CMD python ./app.py