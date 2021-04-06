FROM nginx:alpine

COPY archive.zip .
RUN apk add zip && \
	unzip archive.zip && \
	apk del zip

ENV SOME_VARIABLE=/root

EXPOSE 8002