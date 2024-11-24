FROM python:3.7

# Set working directory
WORKDIR /app

# Set environment variable for Flask app
ENV FLASK_APP=main.py

# Copy requirements.txt
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app/

# Expose port for Flask app
EXPOSE 5000

# Run the application
CMD ["python", "main.py"]
