# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy your Python application files into the container
COPY evaluator.py /app/evaluator.py
COPY utils.py /app/utils.py
COPY run_tests.py /app/run_tests.py
COPY problems.py /app/problems.py

# Copy 'requirements.txt'
COPY test_requirements.txt /app/requirements.txt

# Copy the entire 'logs' directory into the container
COPY logs /app/logs

# Copy 'problems.jsonl' into the container
COPY problems.jsonl /app/problems.jsonl

# Install any needed packages (if any) for your application
# You can add additional dependencies to your requirements.txt
# and install them here using pip.
RUN pip install -r requirements.txt

# Command to run your tests
CMD ["python", "run_tests.py"]


# CHEATSHEET
# docker build -t test-container .
# docker run --rm -v "C:\Users\Rina Carvalho\Documents\TG2\logs":"/app/logs" test-container

