docker build -t ga .
docker run -it --rm --entrypoint /bin/bash ga make %1