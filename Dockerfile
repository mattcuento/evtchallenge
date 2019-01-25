#pull python image
FROM python:3.6

#make a working directory called app
WORKDIR /app

#copy contents of source into the app directory
COPY src ./

#run the installation of requirements (empty)
RUN pip install -r requirements.txt

#expose containers port
EXPOSE 8000

#run the project script
CMD ["python", "project.py"]
