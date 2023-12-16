FROM python:3.7-alpine
# FROM - prebuilt package for Docker

WORKDIR /app
# WORKDIR (working directory) - Create a working directory called "app"

COPY . /app
# COPY - copies python file, dockerfile, and requirements.txt file and plot them into a new operating system called "app" 

RUN pip install -r requirements.txt
# RUN - Take requirements.txt file and install whatever is in the file 

EXPOSE 5000
# EXPOSE - Expose Port 5000 to operating shell

CMD ["python","app.py"]
# CMD - Ready to start application we want docker to run

# Docker build command: docker build -t docker_example_1 .
# Docker run command: docker run -d -p 5001:5000 docker_example_1