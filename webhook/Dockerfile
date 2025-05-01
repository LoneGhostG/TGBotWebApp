FROM python:3.13-slim

WORKDIR /webhook

RUN pip install --no-cache-dir --upgrade pip

COPY /webhook/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY /utils/requirements.txt ./utils/requirements.txt
RUN pip install --no-cache-dir -r utils/requirements.txt

COPY webhook .
COPY utils ./utils

CMD ["python3", "__main__.py"]
