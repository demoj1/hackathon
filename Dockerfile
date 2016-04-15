FROM alpine:latest

WORKDIR /app
ADD ./repo/requirements.txt /app
RUN apk --no-cache update

RUN apk add --no-cache gcc python3 postgresql-dev python3-dev musl-dev

RUN apk add --no-cache --virtual=build-dependencies wget ca-certificates && \
    wget "https://bootstrap.pypa.io/get-pip.py" -O /dev/stdout --no-check-certificate | python3

RUN pip3 install gunicorn meinheld
RUN pip3 install -r requirements.txt

EXPOSE 8000

ADD ./repo/ /app

CMD ["gunicorn", "-w", "2", "--worker-class=meinheld.gmeinheld.MeinheldWorker", \
        "quest.wsgi:application", "-b", "0.0.0.0:8000"]

