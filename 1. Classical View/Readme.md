# Classical View

This Python code is designed to detect blue and red balls in a series of images. It uses classical algorithms in OpenCV to perform color-based object detection and Hough Circle detection to find the balls in the images.

### Requirements
* Python 3.x
* OpenCV (cv2)
* numpy
  
You can install the necessary dependencies using pip.

# Usage
1. Place your images that you want to process in the 1. Classical View/images/ folder.

2. Create a folder where the detected images will be stored. You can specify the name and location of this folder in the store_folder variable in the main.py file.

3. Run **main.py** file.

# Detector Class
The BallDetector class is responsible for detecting balls in an image. It uses the following steps:

* Converts the image to the HSV color space for better color detection.
* Defines lower and upper bounds for blue and red colors in HSV.
* Creates masks for blue and red colors in the image.
* Applies Gaussian Blur to the masks to reduce noise.
* Uses Hough Circle detection to find blue and red circles in the image.
* Choose the largest blue and red circles in the image
* Draws these circles on the original image.
* Provides methods to display and save the results.

You can customize the color detection parameters and Hough Circle detection parameters in the detect_balls method of the BallDetector class to suit your specific needs.

# Conclusion
The provided Python code offers a practical yet traditional approach for detecting blue and red balls in images using OpenCV. While it might serve its purpose, it's important to note that this classical method can be relatively inefficient and inaccurate, especially in scenarios with complex backgrounds or varying lighting conditions.

For more robust and accurate ball detection tasks, considering the adoption of deep learning methods could be a beneficial step forward. Deep learning approaches, such as convolutional neural networks (CNN), have shown significant advancements in object detection tasks, offering better adaptability to various environments and increased accuracy.