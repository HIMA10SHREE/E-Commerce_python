##################### BASE IMAGE ####################################
#############################################

FROM ubuntu:latest AS base
WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install -y python3 python3-pip 

###############DISTROLESS IMAGE################################333


FROM gcr.io/distroless/python3

COPY --from=base /app /app

ENTRYPOINT ["/app"]




