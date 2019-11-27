####
# Base Image
####
FROM ubuntu


####
# Working Direcotry
####
WORKDIR /srv

#### 
# Copy Content Inside Container
####
COPY . .

####
# Set Variables
# Create Non-Privileged User and Group
####
ARG user
ENV user=${user}
RUN groupadd -r docker-workers -g 1500 && useradd -u 1500 -r -g docker-workers $user

####
# Run as $USER
####
USER $user

#### 
# Exectutable
####
CMD /srv/script.sh

