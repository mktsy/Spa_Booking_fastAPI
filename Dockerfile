FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

WORKDIR /server

RUN python -m pip install --upgrade pip

COPY . /server

RUN pip install -r requirements.txt

EXPOSE 80

CMD ["uvicorn", "server.app:app", "--host", "0.0.0.0", "--port", "80"]