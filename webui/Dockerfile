FROM node:alpine
WORKDIR /code
COPY package.json yarn.lock ./
RUN npm install
COPY . .

EXPOSE 3000/tcp
ENTRYPOINT ["yarn", "run", "dev", "--host"]