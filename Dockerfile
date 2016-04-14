FROM frolvlad/alpine-python3

WORKDIR /app
ADD ./quest/ /app

RUN apk --no-cache update

RUN apk add --no-cache gcc python3 postgresql-dev python3-dev musl-dev
RUN pip install gunicorn meinheld
RUN pip install -r requirements.txt

RUN python3 manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "-w", "2", "--worker-class=meinheld.gmeinheld.MeinheldWorker", \
        "quest.wsgi:application", "-b", "0.0.0.0:8000"]