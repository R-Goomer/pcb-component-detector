# PCB Component Detector

This project aims to develop an industry-level application for detecting components on a PCB (Printed Circuit Board) using the YOLO (You Only Look Once) model. The end goal is to deploy the application on Hugging Face Spaces using Streamlit, where users can upload PCB images and get an output image with bounding boxes around detected components and a list of detected elements.

## Table of Contents

- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Data Preparation](#data-preparation)
- [Model Training](#model-training)
- [Application Development](#application-development)
- [Containerization](#containerization)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Project Structure

```
pcb-component-detector/
├── data/
│   ├── raw/                  # Raw data (images)
│   ├── processed/            # Processed data (annotations)
├── notebooks/                # Jupyter notebooks for data exploration
├── src/
│   ├── data/                 # Data loading and preprocessing scripts
│   ├── models/               # Model definitions and training scripts
│   ├── utils/                # Utility scripts
├── app/
│   ├── app.py                # Streamlit application
│   ├── requirements.txt      # Application dependencies
├── docker/
│   ├── Dockerfile            # Dockerfile for containerizing the application
├── .gitignore
├── README.md
├── setup.py
├── train.py                  # Script to train the YOLO model
```

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- Docker (optional, for containerization)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/pcb-component-detector.git
    cd pcb-component-detector
    ```

2. Set up a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r app/requirements.txt
    ```

## Data Preparation
1. Annotate the images using a tool like [LabelImg](https://github.com/tzutalin/labelImg) and save the annotations in `data/train`.

## Model Training

1. Ensure the YOLO environment is set up (follow the [YOLOv5 documentation](https://github.com/ultralytics/yolov5) for setup instructions).
2. Run the training script:
    ```bash
    python train.py
    ```

## Application Development

1. Develop the Streamlit app in `app/app.py` to upload images and display detection results.
2. Run the Streamlit app locally for testing:
    ```bash
    streamlit run app/app.py
    ```

## Containerization

1. Build the Docker image:
    ```bash
    docker build -t pcb-detector -f docker/Dockerfile .
    ```

2. Run the Docker container:
    ```bash
    docker run -p 8501:8501 pcb-detector
    ```

## Deployment

1. Create a new Space on Hugging Face.
2. Connect your GitHub repository to the Space.
3. Deploy the application following the instructions provided by Hugging Face.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.
