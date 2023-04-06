FROM gcc:12.2 AS stage0
ARG ROOTDIR=/home/root/temp
WORKDIR $ROOTDIR
COPY . $ROOTDIR
RUN gcc -o nn neural_network.c -lm

FROM python:3.10-slim AS stage1
ARG ROOTDIR=/home/root/temp
WORKDIR $ROOTDIR
COPY --from=stage0 $ROOTDIR .
RUN bash make

FROM stage1 AS stage2
ENTRYPOINT [ "bash", "make", "dev" ]