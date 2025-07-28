import torch
import torchvision.transforms as transforms
from torchvision.models import resnet18
from PIL import Image

# Load Model
model = resnet18()
model.fc = torch.nn.Linear(model.fc.in_features, 7)
model.load_state_dict(torch.load(r'models\resnet18_emotion.pth', map_location=torch.device("cuda" if torch.cuda.is_available() else "cpu")))
model.eval()

# Classes
classes = ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']

# Transformation
transform = transforms.Compose([
    transforms.Grayscale(num_output_channels=3),
    transforms.Resize((48, 48)),
    transforms.ToTensor(),
])

import numpy as np
import cv2

def predict_emotion(face_img):
    image = Image.fromarray(face_img)
    image = transform(image).unsqueeze(0)
    with torch.no_grad():
        outputs = model(image)
        _, predicted = torch.max(outputs, 1)
    return classes[predicted.item()]


# # Load image as numpy array using OpenCV
# img_path = r'D:\hipster\hipster\emotion_yolo_project\datasets\fer2013\versions\1\test\disgust\PrivateTest_807646.jpg'
# face_img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
# print(predict_emotion(face_img))