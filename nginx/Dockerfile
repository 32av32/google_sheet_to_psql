FROM nginx:latest
  
WORKDIR /usr/src/nginx

COPY nginx.conf /etc/nginx/nginx.conf
COPY conf.d/site.conf /etc/nginx/conf.d/site.conf

RUN rm /etc/nginx/conf.d/default.conf