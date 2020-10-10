FROM amd64/python

WORKDIR /unraid-accessor

COPY . /unraid-accessor

EXPOSE 8000

ENV GUNICORN_CMD_ARGS="--bind=0.0.0.0"

RUN pip3 install -r requirements.txt

RUN pip3 install gunicorn

CMD ["gunicorn", "-w 2", "main:app"]