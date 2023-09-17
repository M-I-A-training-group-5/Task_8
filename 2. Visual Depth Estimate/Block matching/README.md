# Block matching algorithm

## Introduction
This document provides documentation for the implementation of the block
matching algorithm using OpenCV and NumPy.

## Explanation
The code can be divided into several parts:
1. Camera Initialization: The code initializes the left and right cameras
with their respective IDs.
2. Stereo Image Rectification: The code reads the stereo rectification
mapping values from a file and applies rectification to the left and right
images.
3. Trackbar Initialization: The code creates trackbars to adjust various
parameters for the block matching algorithm.
4. StereoBM Algorithm Configuration: The code creates a StereoBM
object and configures its parameters based on the trackbar positions.
5. Disparity Computation: The code computes the disparity map using
the StereoBM algorithm and the rectified left and right images.
6. Disparity Processing: The code converts the disparity map to a float32
format, scales down the disparity values, and normalizes them.
7. Displaying the Disparity Map: The code displays the disparity map
in a window.

## Conclusion
The block matching algorithm implemented using OpenCV and NumPy allows
for the computation of the disparity map from a stereo pair of images. By
adjusting the trackbar parameters, the user can control the quality and accuracy
of the disparity map.