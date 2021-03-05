FROM python:3.8

WORKDIR /usr/src/app

RUN mkdir logs

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 9200

COPY . .

CMD ["python", "main.py"]
