# Use the official Python runtime as a parent image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy the project files to the working directory
COPY . /app

# Upgrade pip and install dependencies
RUN pip install --no-cache-dir --upgrade pip 
RUN pip install --no-cache-dir -r requirnments.txt

# Expose the ports your application uses
EXPOSE 8000

# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]