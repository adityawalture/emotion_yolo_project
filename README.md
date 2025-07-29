# Emotion Detection from Video using YOLOv8 and ResNet18

This project detects human emotions from uploaded videos using a combination of YOLOv8 for face detection and a ResNet18-based CNN classifier trained on the FER2013 dataset.

---

## 🚀 Features

- Detect faces in videos using YOLOv8.
- Predict emotions like happy, sad, fear, surprise, etc., using a ResNet18 model.
- Upload and visualize the results via a clean Streamlit web UI.
- Export processed videos with annotated face boxes and predicted emotions.

---

## 🧠 Emotions Detected

- Angry
- Disgust
- Fear
- Happy
- Sad
- Surprise
- Neutral

---

## 🗂️ Project Structure

```
emotion_yolo_project/
├── models/
│   ├── yolov8n-face.pt              # YOLOv8 face detection model
│   └── resnet18_emotion.pth         # Trained ResNet18 model for emotion classification
├── datasets/                        # FER2013 dataset (organized by class folders)
├── src/
│   ├── emotion_model.py             # Emotion classification logic
│   ├── inference_pipeline.py        # Face detection + emotion pipeline
│   └── train_emotion_model.py       # Training script for ResNet18
├── streamlit_app.py                 # Streamlit UI code
├── requirements.txt                 # Python dependencies
└── Dockerfile                       # Docker build instructions
```

---

## 🔧 Installation

### Option 1: Run Locally

```bash
# Clone the repository
git clone https://github.com/yourusername/emotion_yolo_project.git
cd emotion_yolo_project

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Run the app
streamlit run streamlit_app.py
```

Open your browser at [http://localhost:8501](http://localhost:8501)

---

### Option 2: Run with Docker

```bash
# Build the image
docker build -t emotion_yolo_ui .

# Run the container
docker run -p 8501:8501 emotion_yolo_ui
```

Visit [http://localhost:8501](http://localhost:8501)

---

## 📥 Required Downloads

- YOLOv8n face detector: [Download yolov8n-face.pt](https://github.com/derronqi/yolov8-face/releases/download/v0.1/yolov8n-face.pt) → save to `models/`

## 🧾 Requirements

```
streamlit
torch
torchvision
ultralytics
opencv-python
fastapi
pillow
numpy
tqdm
scikit-learn
python-multipart
```

---



## 🙋‍♂️ Streamlit

## [Emotion_Yolo](https://github.com/adityawalture/emotion_yolo_project)
