FROM nginx:alpine

# Copy static files
COPY . /usr/share/nginx/html

# Copy custom NGINX config
COPY nginx.conf /etc/nginx/conf.d/default.conf
