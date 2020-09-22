FROM python:3.7

RUN pip install requests

WORKDIR /app

COPY . .

CMD ["python","/app/src/app.py"]
