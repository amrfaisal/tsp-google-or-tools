echo "Building docker image..."
docker build -t tsp-or-tools .
docker run --rm -it tsp-or-tools