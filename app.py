
# -----------------------------------------------------------------------------------------------------------------------
import streamlit as st
import tempfile
import os
import shutil
import cv2
import subprocess
from src.inference_pipeline import detect_emotions_from_video


def convert_and_prepare_video(input_video):
    output_video = "converted_output.mp4"
    input_video = os.path.abspath(input_video)
    output_video = os.path.abspath(output_video)

    # Convert to H.264 video
    cmd = [
        "ffmpeg",
        "-i", input_video,
        "-c:v", "libx264",
        "-an",
        "-f", "mp4",
        "-y",
        output_video
    ]
    subprocess.run(cmd, capture_output=True, text=True)

    # Add silent AAC audio
    audio_cmd = [
        "ffmpeg",
        "-i", output_video,
        "-f", "lavfi", "-i", "anullsrc=channel_layout=stereo:sample_rate=44100",
        "-c:v", "copy",
        "-c:a", "aac",
        "-shortest",
        "-y",
        output_video
    ]
    subprocess.run(audio_cmd, capture_output=True, text=True)

    return output_video


st.set_page_config(page_title="Live Emotion Detection", layout="centered")
st.title("🎭 Hipster YoloV8 Emotion Detection from Video")

uploaded_video = st.file_uploader("Upload a video file", type=["mp4", "mov", "avi"])

if uploaded_video is not None:
    # Save uploaded video to a temporary file
    input_tempfile = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
    input_tempfile.write(uploaded_video.read())
    input_tempfile.flush()

    st.video(input_tempfile.name)
    st.info("Processing video... This might take a few seconds.")

    # Run detection
    with st.spinner("Detecting emotions..."):
        output_path = detect_emotions_from_video(input_tempfile.name)
        output_path = convert_and_prepare_video(output_path)

        # Move to a predictable path
        os.makedirs("temp_output", exist_ok=True)
        output_display_path = os.path.join("temp_output", os.path.basename(output_path))
        shutil.move(output_path, output_display_path)

    st.success("Detection complete! 🎉")

    # Read and re-save video bytes into a temp file for Streamlit
    with open(output_display_path, "rb") as video_file:
        video_bytes = video_file.read()

        display_tempfile = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
        display_tempfile.write(video_bytes)
        display_tempfile.flush()

        st.video(display_tempfile.name)

    # st.caption(f"Video processed and saved at: `{output_display_path}`")
