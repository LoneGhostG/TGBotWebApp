FROM python:3.13-slim

WORKDIR /backend

RUN pip install --no-cache-dir --upgrade pip

COPY /backend/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY /utils/requirements.txt ./utils/requirements.txt
RUN pip install --no-cache-dir -r utils/requirements.txt

COPY backend .
COPY utils ./utils

CMD ["python3", "__main__.py"]
