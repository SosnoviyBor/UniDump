# Downloading preconfigured Nginx image based on Alpine Linux
FROM nginx:alpine

# Copying our archive to the file system's root folder
# It's a bad practice, but it'll do for lab
COPY archive.zip .
# Downloading Zip via Alpine Packet Manager
# Then unarchiving our archive (it contains file "open me.mp4")
# And then deleting Zip because we won't need it later
RUN apk add zip && \
	unzip archive.zip && \
	apk del zip

# Adding Enviromental Variable to our OS
# It can also be accessed later in our Dockerfile
ENV SOME_VARIABLE=/root

# Setting default port for our web-server to 8002
EXPOSE 8002