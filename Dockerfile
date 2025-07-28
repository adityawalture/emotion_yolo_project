FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1 \
    libglib2.0-0 \
    ffmpeg && \
    apt-get clean && rm -rf /var/lib/apt/lists/*


COPY . .

# To run FastAPI, uncomment the line below:
# CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "8000"]

# To run Streamlit UI for video upload:
CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
