# ITC 630 Homework 1 : File Upload Service

To run:

1. Ensure Docker is installed on your computer
2. Ensure `init_server.sh` has execute permissions: `chmod +x init_server.sh`
3. Build the docker container using the Dockerfile: `docker build -t upload-site .`
4. Run the docker container with: `docker run -it -p 3000:3000 -e DJANGO_SUPERUSER_USERNAME=admin -e DJANGO_SUPERUSER_PASSWORD=demopass -e DJANGO_SUPERUSER_EMAIL=admin@example.com upload-site`
5. The site is now accessible at `localhost:3000`