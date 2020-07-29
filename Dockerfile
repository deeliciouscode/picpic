FROM ubuntu:latest

WORKDIR /app

# TODO: Change so the versions are fine.
# NEED: nodejs: 10.19.0 | npm: 6.14.4 | python: 3.8.2 | pip: 20.0.2
# ALSO: check the python packages for the right version

RUN apt-get update

RUN apt-get install -y nodejs && apt-get install -y npm
RUN nodejs -v  && npm -v

RUN apt-get install -y python3 && apt install -y python3-pip
RUN python3 -V && pip3 -V

COPY ./client/package.json ./client/
RUN cd ./client && npm install 

COPY ./client/ ./client/
RUN mkdir server
RUN cd ./client && npm run build && cp -r ./dist ../server/static

COPY ./server/install.sh ./server/
RUN cd ./server && chmod +x install.sh && ./install.sh

RUN cd ./server && mkdir img && cd ./img && mkdir final && mkdir pics && cd ./pics && mkdir meta && mkdir small

COPY . .

CMD ["python3", "./server/app.py"]