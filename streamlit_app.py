import streamlit as st
import tempfile
import os
import shutil
import cv2
from src.inference_pipeline import detect_emotions_from_video

st.set_page_config(page_title="Live Emotion Detection", layout="centered")
st.title("🎭 Emotion Detection from Video")

uploaded_video = st.file_uploader("Upload a video file", type=["mp4", "mov", "avi"])

if uploaded_video is not None:
    tfile = tempfile.NamedTemporaryFile(delete=False, suffix='.mp4')
    tfile.write(uploaded_video.read())
    tfile.flush()

    st.video(tfile.name)
    st.info("Processing video... This might take a few seconds.")

    with st.spinner("Detecting emotions..."):
        output_path = detect_emotions_from_video(tfile.name)
        output_display_path = os.path.join("temp_output", os.path.basename(output_path))
        os.makedirs("temp_output", exist_ok=True)
        shutil.move(output_path, output_display_path)

    st.success("Detection complete! 🎉")

    with open(output_display_path, 'rb') as video_file:
        video_bytes = video_file.read()
        st.video(video_bytes)
