FROM python:3.7.3-alpine

LABEL maintainer="Nikkorenz Clarin"

COPY requirements.txt /tmp/requirements.txt 

#RUN apk add --no-cache --update python3-dev  gcc build-base
RUN pip3 install -r /tmp/requirements.txt

COPY src /src/

WORKDIR /src/

EXPOSE 5000

ENTRYPOINT [ "tail", "-f", "/dev/null" ]
#ENTRYPOINT ["python", "/src/app.py"]