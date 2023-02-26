FROM python:3.10

WORKDIR /APIEndpoints 
COPY ./requirements.txt /APIEndpoints/requirements.txt
RUN python3 -m pip install --upgrade -r /APIEndpoints/requirements.txt

COPY . /APIEndpoints/API
CMD ["uvicorn", "API.test:app", "--host", "0.0.0.0", "--port", "8080"]
