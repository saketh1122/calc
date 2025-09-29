# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy all files into container
COPY . .

# Install any dependencies if needed (none for now)
# RUN pip install -r requirements.txt

# Run calculator when container starts
CMD ["python3", "calc.py"]
