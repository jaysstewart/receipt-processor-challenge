# Dockerfile

# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /receipt-processor-challenge

# Copy the current directory contents into the container at /app
COPY . /receipt-processor-challenge

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define the command to run the FastAPI api using Uvicorn
CMD ["uvicorn", "main:api", "--host", "0.0.0.0", "--port", "80", "--reload"]