FROM python:latest as stage

#
#
#

FROM alpine:latest

WORKDIR /srv

COPY --from=stage /path/copy/from .

EXPOSE port

ENTRYPOINT []

