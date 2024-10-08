# Use the official Python 3.12.7 slim image as the base image
FROM python:3.12.7-slim

# Set the working directory within the container
WORKDIR /dnd

# Copy the necessary files and directories into the container
COPY src/ /dnd/src/
COPY templates/ /dnd/templates/
COPY .env main.py requirements.txt  /dnd/

# Upgrade pip and install Python dependencies
RUN pip3 install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Expose port 5000 for the Flask application
EXPOSE 5000

# Define the command to run the Flask application using Gunicorn
CMD ["gunicorn", "main:app", "-b", "0.0.0.0:5000", "-w", "4"]