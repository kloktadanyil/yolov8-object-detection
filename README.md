# YOLOv8 Foreign Object Debris (FOD) Detection

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![YOLOv8](https://img.shields.io/badge/Model-YOLOv8-green)
![Roboflow](https://img.shields.io/badge/Data-Roboflow-purple)

This project demonstrates a pipeline for detecting Foreign Object Debris (FOD) using computer vision. The model is trained on a custom dataset using the **YOLOv8** architecture and the **Roboflow** platform.

Such a system can be used for automatic monitoring of surface cleanliness (for example, airport runways or industrial floors).

## Demo

The model is capable of recognizing small objects in real-time.

![Demo Animation](https://github.com/user-attachments/assets/19406a09-835a-48e6-9d72-e2a19e2f309e)

**[Watch the full video on YouTube](https://youtube.com/shorts/5oNuL0XsUKY)**

---

## Repository Structure

* `best8.pt` — weights of the trained version 8 model (ready to use).
* `best11.pt` — weights of the trained version 11 model (ready to use).
* `best26.pt` — weights of the trained version 26 model (ready to use).
* `yolo_inf.py` — script required to run the detection.
  
## How to run the project

## Testing on the example 

**Attention! All files must be located in the same folder.**

#### 1. Environment setup

##### 1.1 Clone the repository
```bash
git clone https://github.com/kloktadanyil/yolov8-object-detection.git
```
##### 1.2 Move to the directory
```bash
cd yolov8-object-detection
```
##### 1.3 Activate the environment
Create an environment and activate it

Creation

```bash
python -m venv venv
```
Activation (for  Mac)
```bash
source venv/bin/activate
```
Activation (for  Windows)
```bash
.\venv\Scripts\Activate.ps1
```
#### 2. Upload video
To ensure the model works correctly, you can use my test video.
1. **Download the test video:** **[Download video_test.mp4](https://youtube.com/shorts/WpaYRwc7CQA)** *(Save it to the project folder)*

#### 3. Installing dependencies
```bash
pip install ultralytics opencv-python
```
**Prepare the video:** Put your video (test_video.mp4) in the project directory.
#### 4. Start inference:
  You can run the detection with a single command in the terminal:
 ```bash
 python yolo_inf.py
 ```
To stop detection, press Cntl+C in the terminal.
## Testing on your own video 
**Attention! All files must be in the same folder**
To test the model on your own computer, follow these steps:

###### 1.1 Install the repository
```bash
git clone https://github.com/kloktadanyil/yolov8-object-detection.git
```
##### 1.2 Move to the directory
```bash
cd yolov8-object-detection
```
##### 1.3 Activate the environment
Create an environment and activate it

Creation

```bash
python -m venv venv
```
Activation (for  Mac)
```bash
source venv/bin/activate
```
Activation (for  Windows)
```bash
.\venv\Scripts\Activate.ps1
```
#### 2. Installing dependencies
```bash
pip install ultralytics opencv-python
```
#### 3. Start inference:
Create a main.py file and paste this code there to run detection on your video or via webcam:
```python
from ultralytics import YOLO

# your model
model = YOLO("best8.pt")

# start detection
model.predict(source="path/to/your/video.mp4", show=True, conf=0.5)
```
The video should preferably be similar to the one in this link, as the model may not find the objects.
**[YouTube Video](https://youtube.com/shorts/WpaYRwc7CQA)**

# yolov8-object-detection
Object detection pipeline using YOLOv8 and Roboflow. Includes training notebooks and inference scripts.

Technology stack
Model: YOLOv8 (Ultralytics),YOLOv11 (Ultralytics),YOLOv26 (Ultralytics)

Language: Python

Dataset: Roboflow (annotation and augmentation)

Learning environment: Google Colab
