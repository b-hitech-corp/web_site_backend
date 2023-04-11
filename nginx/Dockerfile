# Fetching the latest nginx image
#FROM nginx:1.23-alpine
FROM nginx:alpine-slim

# Removing default nginx.conf
RUN rm /etc/nginx/conf.d/default.conf

# Copying our nginx.conf
COPY nginx.conf /etc/nginx/conf.d

#FROM nginx:stable-alpine
#
#COPY default.conf /etc/nginx
#COPY default.conf /etc/nginx/conf.d
#
#EXPOSE 80
