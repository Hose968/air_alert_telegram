FROM python:3.12

RUN mkdir -p /opt/app
WORKDIR /opt/app

COPY ./requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt

COPY . .

ENTRYPOINT [ "python" "alert.py" ]

