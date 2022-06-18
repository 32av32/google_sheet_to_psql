FROM python:3.10.4-alpine

WORKDIR /usr/src/app

COPY req.txt .

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r req.txt

COPY . .

RUN mkdir ./static \
    && python3 manage.py collectstatic

RUN chmod +x /usr/src/app/entrypoint.sh

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]