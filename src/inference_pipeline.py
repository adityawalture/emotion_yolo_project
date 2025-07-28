import cv2
from ultralytics import YOLO
from src.emotion_model import predict_emotion

model = YOLO("models/yolov8n-face.pt", task="detect")

def detect_emotions_from_video(video_path):
    cap = cv2.VideoCapture(video_path)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)
        boxes = results[0].boxes
        if boxes is not None and boxes.xyxy is not None:
            for bbox in boxes.xyxy.cpu().numpy():
                x1, y1, x2, y2 = map(int, bbox)
                # Ensure coordinates are within frame bounds
                x1, y1 = max(0, x1), max(0, y1)
                x2, y2 = min(frame.shape[1], x2), min(frame.shape[0], y2)
                if x2 <= x1 or y2 <= y1:
                    continue
                face = frame[y1:y2, x1:x2]
                if face.size == 0:
                    continue
                emotion = predict_emotion(face)
                cv2.putText(frame, emotion, (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        out.write(frame)
    cap.release()
    out.release()
    return 'output.mp4'


# cd D:/hipster/hipster/emotion_yolo_project/models
# wget https://github.com/derronqi/yolov8-face/releases/download/v0.1/yolov8n-face.pt




