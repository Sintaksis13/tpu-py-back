FROM python:3.8-alpine 
WORKDIR /usr/src/app 
COPY requirements.txt ./
RUN python3 -m pip install --user --no-cache-dir -r requirements.txt 
COPY . . 
ENTRYPOINT ["python", "app.py"]
