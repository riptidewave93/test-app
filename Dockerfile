FROM python:3.8.1

WORKDIR /src

COPY ./src/ .

RUN "ls"

RUN ["cat", "requires.txt"]

RUN ["/usr/local/bin/pip3", "install", "-r", "requires.txt"]

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]
