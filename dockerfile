# Use a lightweight Python 3.12 image
FROM python:3.12-slim

# Install required native libraries (for python-magic, ssdeep, lief)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gcc \
    libmagic1 libmagic-dev \
    libfuzzy-dev \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Create a non-root user
RUN useradd -m -u 10001 -s /usr/sbin/nologin appuser

# Set the working directory
WORKDIR /app

# Copy requirements.txt
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project source code
COPY collector /app/collector
COPY utils /app/utils

# Create the samples directory (for uploaded files)
RUN mkdir -p /samples && chown -R appuser:appuser /samples

# Switch to the non-root user
USER appuser

# Server port exposition
EXPOSE 8000

# Start the FastAPI server (you can enable --reload in dev mode)
CMD ["python", "-m", "uvicorn", "collector.main:app", "--host", "0.0.0.0", "--port", "8000"]
