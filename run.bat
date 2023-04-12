docker build -t ga .
docker run -it -v %cd%/data/out:/mnt/data/out/ --rm --entrypoint /bin/bash ga make data