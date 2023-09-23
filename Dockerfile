# Use the official Python base image with version 3.9
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Update and install default-mysql-client
RUN apt-get update \
    && apt-get install -y default-mysql-client

# install black
# RUN pip install black

# Copy the requirements file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the container
COPY . .
