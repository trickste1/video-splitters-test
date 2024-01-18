FROM node:16

WORKDIR /usr/src/app

COPY package*.json ./

RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get install -y ffmpeg
RUN npm install

COPY . .

CMD mkdir frames
CMD ["node", "split.js"]
