FROM python:3.12-slim

WORKDIR /home/user

COPY ./src/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src .

CMD ["python", "/home/user/example.py"]