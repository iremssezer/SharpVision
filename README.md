# SharpVision
License Plate Recognition YOLOV8 and EasyOCR (with Videos)

## Ultralytics
Ultralytics YOLOv8 is the latest version of the YOLO (You Only Look Once) object detection and image segmentation model developed by Ultralytics. The YOLOv8 (with version YOLOv8.0.20) model is designed to be fast, accurate, and easy to use, making it an excellent choice for a wide range of object detection and image segmentation tasks. It can be trained on large datasets and is capable of running on a variety of hardware platforms, from CPUs to GPUs.

![ultralyticshub](https://github.com/iremssezer/SharpVision/assets/74788732/0198f428-e3b7-464b-8eb4-bc7d1174929b)


## Dataset from the Roboflow: [https://universe.roboflow.com/iremsezer2trakyaedutr/plate_detection-mtyuz]
This dataset contains images of car license plates captured in various locations and under different lighting conditions. The dataset comprises a total of 724 images, each of which includes one or more car license plates. The images were annotated with bounding boxes around the license plates, indicating their precise location in the image. The dataset I obtained from this link [https://storage.googleapis.com/openimages/web/visualizer/index.html?type=detection&amp%3Bset=train&amp%3Bc=%2Fm%2F01jfm_&set=train&c=%2Fm%2F0703r8] and It consists of images showing vehicle registration plates that I have tagged using Roboflow. 
### Train / Test Split
Training Set: %84
1.1k images
Validation Set: %11
144 images
Testing Set: %4
51 images
### Preprocessing
Auto-Orient: Applied
Resize: Stretch to 640x640
### Augmentations
Outputs per training example: 2
Grayscale: Apply to 25% of images
Blur: Up to 2.5px
Noise: Up to 5% of pixels

![roboflow2](https://github.com/iremssezer/CharpVision/assets/74788732/3970e663-c5f1-40c6-aff9-ff5a97c01711)

## Custom Training
YOLOv8 Object Detection
Once the dataset version is generated,it has dataset you can load directly into our notebook for easy training. 
https://colab.research.google.com/github/roboflow-ai/notebooks/blob/main/notebooks/train-yolov8-object-detection-on-custom-dataset.ipynb

## Deploy model on Roboflow
When the YOLOv8 model is trained, you’ll have a set of trained weights ready for use. These weights will be `best.pt` folder. You can upload your model weights to Roboflow Deploy to use your trained weights on our infinitely scalable infrastructure.

## Detection License Plate and Reading on Video
![detectionn](https://github.com/iremssezer/CharpVision/assets/74788732/46603abb-af17-4fbd-8269-fae08f560402)

![detection2](https://github.com/iremssezer/CharpVision/assets/74788732/0eeb0940-a72c-4c7c-a1f0-da4717d49a3b)

![detection 3](https://github.com/iremssezer/CharpVision/assets/74788732/3402f420-9d35-43df-be34-bcfd2c4576c0)

![veritabanı3](https://github.com/iremssezer/CharpVision/assets/74788732/29c4aa75-1a73-4ce7-b73f-fc47f902a68f)

