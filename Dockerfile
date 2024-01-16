# base image 
FROM python:3.12.1
ENV PYTHONUNBUFFERED 1
# create root directory for our project in the container
RUN mkdir /app
# Set the working directory to /app
WORKDIR /app
# Copy the current directory contents into the container at /app
COPY . /app/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt 
# Make port 8000 available to the world outside this container
EXPOSE 8000
# Define environment variable
ENV NAME e-commerce 
# Run app.py when the container launches 

CMD ["make", "run"]

