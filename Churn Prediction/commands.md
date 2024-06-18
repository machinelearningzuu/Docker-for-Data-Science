### Docker commands used here

docker build -t churn-analysis-image .
docker run -d --name churn-analysis-container churn-analysis-image

### Summary of Docker commands

docker build -t <my-image-name> to build the Docker Image
docker run -d --name <my-container-name> <my-image-name> to build the Docker Container
docker images to display the list of created images
docker ps -a to show the list of containers
docker rmi <my-image-id> to remove an image
docker stop <my-container-id> to stop a running container
docker rm <my-container-id> to remove a stopped container