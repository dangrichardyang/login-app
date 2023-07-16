FROM node:16-alpine

WORKDIR app

COPY package.json .

RUN yarn install

COPY . .

CMD [ "yarn", "run", "dev", "--host", "0.0.0.0", "--port", "3000" ]
