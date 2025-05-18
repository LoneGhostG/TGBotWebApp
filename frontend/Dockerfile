FROM node:latest AS build

WORKDIR /frontend

COPY /frontend/package*.json .
RUN npm install

COPY frontend/. .
RUN npm run build


FROM nginx:latest

COPY --from=build /frontend/dist /usr/share/nginx/html
COPY /frontend/nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
