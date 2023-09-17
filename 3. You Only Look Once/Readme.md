# You Only Look Once - Documentation

The goal of the project is to train a model to be able to differentiate a one egyptian pound, a half egp and a quarter EGP from a random picture.

## Data Collection
For this project, the team collected a diverse set of photos that included different angles, lighting conditions, distances from the camera, and various types of coins. Each team member contributed to the dataset creation process.

The dataset can be accessed through the following link: [Dataset zip file](https://drive.google.com/drive/folders/19sA4E8vhA0LRcKoVw7PZ4nM7MDCfgBuI?usp=sharing)

## Image Annotation
To annotate the collected images, the team utilized the online platform [roboflow.com](https://app.roboflow.com/ezz-eldeen-mohammad-j3amd). This platform facilitated the annotation process by providing features like label assist to speed up the process and ensure accurate bounding of each object in the images.

## Exportation and Data Files
After completing the image annotation process, the team exported the dataset using roboflow. This exportation allowed for the splitting of the dataset into training and validation images. Additionally, roboflow generated the necessary data.yaml file, which describes the dataset and its classes, eliminating the need for manual creation.

## Installation and Training
The team proceeded to work with a Jupyter notebook. They installed the Ultralytics library, which provides the YOLOv8 implementation. To access the dataset, they mounted the Google Drive within the notebook environment. After unzipping the dataset file and changing directories to the dataset location using the `cd` command, they performed a test training with a single epoch to verify that everything was set up correctly. Once confirmed, they trained the model for 200 epochs, utilizing the available GPU resources provided by Google.

## Deployment Script
To test the trained model on a video, the team implemented a simple deployment script in Python. This script allowed them to apply the model to a test video and observe its performance in detecting and differentiating the Egyptian pound coins.

## Conclusion
Throughout the project, the team successfully collected a diverse dataset of Egyptian pound coins, annotated the images using roboflow, and trained a YOLOv8 model using the Ultralytics library. The team also implemented a deployment script to apply the model to a test video. The project demonstrates the ability to differentiate between one Egyptian pound, half Egyptian pound, and quarter Egyptian pound coins. Further improvements and fine-tuning can be explored to enhance the model's accuracy and expand its capabilities.