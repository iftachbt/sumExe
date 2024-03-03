FROM python:latests

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENV DATABASE_URI="sqlite:///iftachDB.db"

CMD ["python", "app.py"]