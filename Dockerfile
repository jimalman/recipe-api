FROM python:3.11 

COPY requirements.txt /tmp/requirements.txt
COPY requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

ARG DEV=false
RUN pip3 install --upgrade pip && \
    pip3 install -r /tmp/requirements.txt --no-cache-dir && \
    if [ $DEV = "true" ]; \
        then pip3 install -r /tmp/requirements.dev.txt ; \
    fi && \
    rm -rf /tmp && \
    adduser \
    --disabled-password \
    --no-create-home \
    django-user

USER django-user
