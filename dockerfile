# Use official Python runtime as a parent image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements first (for caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN  apt update && apt install -y iputils-ping

# Copy the rest of the app
COPY main.py .

# Run the script by default
CMD ["python", "main.py"]
