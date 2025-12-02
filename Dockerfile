# Must match the python version of your .so file (3.10)
FROM python:3.10-slim

# Install system dependencies required for CV/ML (OpenCV often needs these)
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy your package files (setup.py, src/, MANIFEST.in)
COPY . .

# Install your package (this handles the .so placement via setup.py)
RUN pip install .

# Verification step: Ensure import works inside the container
RUN python -c "import SpiraLibs; print('SpiraLibs loaded successfully')"