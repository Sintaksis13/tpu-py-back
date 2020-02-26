FROM python:3.8-alpine 
EXPOSE 8080 
WORKDIR /opt/app 
COPY requirements.txt . 
RUN apk add --no-cache --virtual .build-deps build-base gcc musl-dev python3 \ 
&& pip3 install -r requirements.txt \
&& apk del .build-deps 
COPY app ./app 
ENTRYPOINT ["python3", "-m", "app"]
