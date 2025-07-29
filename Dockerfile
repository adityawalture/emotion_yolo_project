# FROM python:3.10-slim

# WORKDIR /app

# COPY requirements.txt .
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     libgl1 \
#     libglib2.0-0 \
#     ffmpeg && \
#     apt-get clean && rm -rf /var/lib/apt/lists/*


# COPY . .

# # To run FastAPI, uncomment the line below:
# # CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "8000"]

# # To run Streamlit UI for video upload:
# CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
FROM python:3.10-slim

WORKDIR /app

# Install system dependencies including build tools and libraries needed for Python packages and OpenCV
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1 \
    libglib2.0-0 \
    ffmpeg \
    build-essential \
    gcc \
    g++ \
    python3-dev \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Upgrade pip to ensure compatibility with wheels
RUN pip install --upgrade pip

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your application code
COPY . .

# Default command (FastAPI app)
# CMD ["uvicorn", "app:", "--host", "0.0.0.0", "--port", "8000"]
CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]

