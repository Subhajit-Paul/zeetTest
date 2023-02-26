FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10

COPY ./app/DomainChecker/requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY ./app/DomainChecker /app

CMD ["ls", "-l"]
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]