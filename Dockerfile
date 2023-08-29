# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE mysite.settings

# Set the working directory in the container
WORKDIR /app

# Install Daphne
RUN pip install daphne

# Install any needed packages specified in requirements.txt
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app/
COPY . /app/

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run Daphne when the container launches
CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "mysite.asgi:application"]
