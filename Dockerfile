FROM python:3

WORKDIR /project

COPY . /project

EXPOSE 8000

RUN pip install -r requirements.txt

ENV NAME evtWorld

CMD ["python", "project.py"]
