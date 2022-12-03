FROM node:16.13.0-alpine
WORKDIR /angular-HitBack/src/app
COPY package.json .
COPY package-lock.json .
RUN npm install
COPY . .
EXPOSE 4200
CMD /angular-HitBack/src/app/node_modules/.bin/ng serve --host 0.0.0.0