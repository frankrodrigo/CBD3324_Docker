# Base image for Python
FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libmariadb-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . /app
WORKDIR /app

# Set the Flask environment variables
ENV FLASK_APP=app.py
ENV FLASK_ENV=development

# Expose the port Flask runs on
EXPOSE 5000

# Command to run the app
CMD ["flask", "run", "--host=0.0.0.0"]
