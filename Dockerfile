FROM python:3.7

RUN pip install pandas-datareader DateTime

WORKDIR /app

COPY . .

# CMD ["python","/src/app.py"]
