from fastapi import FastAPI, UploadFile, File
from src.inference_pipeline import detect_emotions_from_video
import shutil

app = FastAPI()

@app.post("/detect_emotions/")
async def detect_emotions(video: UploadFile = File(...)):
    with open("temp.mp4", "wb") as buffer:
        shutil.copyfileobj(video.file, buffer)
    output_path = detect_emotions_from_video("temp.mp4")
    return {"processed_video": output_path}
