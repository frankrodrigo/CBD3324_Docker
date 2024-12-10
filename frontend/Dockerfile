FROM nginx:alpine

# Copy static files
COPY . /usr/share/nginx/html

# Copy the nginx.conf template
COPY nginx.conf /etc/nginx/conf.d/default.conf.template

# Install envsubst for variable substitution
RUN apk add --no-cache gettext

# Replace environment variables in nginx.conf at runtime
CMD ["/bin/sh", "-c", "envsubst '$BACKEND_URL' < /etc/nginx/conf.d/default.conf.template > /etc/nginx/conf.d/default.conf && nginx -g 'daemon off;'"]
