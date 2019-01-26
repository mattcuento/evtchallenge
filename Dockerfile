#pull python image
FROM python:3.6

#make a working directory called app
WORKDIR /app

#copy contents of source into the app directory
COPY . /app
COPY start.sh /usr/local/bin

#expose containers port
EXPOSE 8888

#run the project
ENTRYPOINT ["/bin/bash", "start.sh"]

#change ip to local host(windows issue)
