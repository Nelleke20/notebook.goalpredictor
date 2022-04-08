FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

RUN pip install --upgrade pip
WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app /app   

# EXPOSE 8000
# ENTRYPOINT ["uvicorn", "app.main:app --reload"]
# CMD ["uvicorn", "app.main:app", "8000"]

FROM python:3.8
WORKDIR /app 

COPY requirements.txt /
RUN pip install --requirement /requirements.txt

COPY ./app /app

EXPOSE 8000
# CMD ["uvicorn", "app.main:app", "--host=0.0.0.0" , "--reload" , "--port", "8000"]

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
