FROM python:3

RUN apt-get update && apt-get install nginx -y
COPY nginx.default /etc/nginx/sites-available/default

RUN mkdir -p /opt/upload_site
COPY requirements.txt init_server.sh /opt/upload_site/
COPY upload_site /opt/upload_site/
WORKDIR /opt/upload_site
RUN pip install -r requirements.txt --no-cache-dir
RUN chown -R www-data:www-data /opt/upload_site

# Run init script
CMD ["./init_server.sh"]