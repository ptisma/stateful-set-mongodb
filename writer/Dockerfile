# Use an official Python runtime as a parent image
FROM python:3.11-bullseye

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container and install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Copy the script and any other necessary files into the container
COPY main.py /app/main.py

# Run the script when the container starts
CMD ["python", "main.py"]
