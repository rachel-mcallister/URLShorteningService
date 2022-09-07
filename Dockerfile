FROM python:3

COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install -r requirements.txt

COPY ./ /app

EXPOSE 5000

CMD ["python", "app.py"]