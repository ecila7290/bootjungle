FROM python:3.8

LABEL version=0.1

RUN apt-get update && apt-get install -y --no-install-recommends \
		netcat \
	&& rm -rf /var/lib/apt/lists/*

RUN mkdir /data

WORKDIR /data

COPY requirements.txt /data

RUN pip install -r requirements.txt

COPY . /data

EXPOSE 5000

CMD [ "python", "./run.py", "flask run", "-h 0.0.0.0", "-p 5000" ]
