import streamlit as st
from PIL import Image as PILImage
import subprocess
from pathlib import Path
import shutil
import os

import subprocess
import sys

subprocess.check_call([sys.executable, "-m", "pip", "install", "torch"])

# Function to run YOLOv5 inference and return annotated image path
def run_yolov5_inference(image_path, output_dir):
    command = [
        "python", "./Notebooks/yolov5/detect.py",
        "--weights", "./Notebooks/yolov5/runs/train/exp/weights/best.pt",  # Replace with your actual path
        "--img", "640",  # Inference size, adjust as needed
        "--conf", "0.4",  # Confidence threshold, adjust as needed
        "--source", image_path,
        "--save-txt",  # Save results to text files
        "--save-conf",  # Save confidence scores
        "--project", output_dir,  # Output directory for results
        "--name", "inference_output"  # Output folder name
    ]

    subprocess.run(command, check=True)

    # Return path to annotated image
    annotated_image_path = f"{output_dir}/inference_output/{Path(image_path).stem}.jpg"
    return annotated_image_path

def main():
    st.title("PCB Component ID (Yolov5)")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

    if uploaded_file is None:
        # If no file uploaded, show default sample images
        sample_images_dir = "sample_images"
        sample_images = os.listdir(sample_images_dir)
        if sample_images:
            selected_sample_image = st.selectbox("Choose a sample image", sample_images)
            image_path = os.path.join(sample_images_dir, selected_sample_image)
        else:
            st.warning("No sample images found.")
            return
    else:
        # Save the uploaded file to a temporary location
        image_path = "/tmp/uploaded_image.jpg"
        with open(image_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

    # Run YOLOv5 inference
    output_dir = "./temp_outputs"
    annotated_image_path = run_yolov5_inference(image_path, output_dir)

    # Display original and annotated images
    st.subheader("Original Image")
    st.image(PILImage.open(image_path), caption="Original Image", use_column_width=True)

    st.subheader("Annotated Image")
    temp_image = PILImage.open(annotated_image_path)
    # Cleanup: Delete the output folder (uncomment when integrating with deletion logic)
    shutil.rmtree(output_dir)
    st.image(temp_image, caption="Annotated Image", use_column_width=True)

if __name__ == "__main__":
    main()
