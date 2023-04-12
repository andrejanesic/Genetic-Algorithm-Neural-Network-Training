FROM gcc:12.2 AS stage0
ARG ROOTDIR=/home/root/temp
WORKDIR ${ROOTDIR}
COPY neural_network.c ${ROOTDIR}
RUN gcc -o nn neural_network.c -lm

FROM python:3.10-slim AS stage1
ARG ROOTDIR=/home/root/temp
WORKDIR ${ROOTDIR}
COPY --from=stage0 ${ROOTDIR} .
COPY make ${ROOTDIR}
COPY requirements.txt ${ROOTDIR}
COPY setup.py ${ROOTDIR}
RUN bash make

FROM stage1 AS stage2
ARG ROOTDIR=/home/root/temp
WORKDIR ${ROOTDIR}
COPY genetic_algorithm_neural_network_training ${ROOTDIR}/genetic_algorithm_neural_network_training
COPY tests ${ROOTDIR}/tests
COPY data ${ROOTDIR}/data
WORKDIR ${ROOTDIR}/data/in
RUN python ./generate_configs.py
WORKDIR ${ROOTDIR}
ENTRYPOINT [ "bash", "make", "dev" ]