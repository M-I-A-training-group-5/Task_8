# Visual Depth Estimate
# Overview
This project delves into the realm of depth estimation through cameras, providing a 3D perspective of the world. It employs various methodologies and camera types, including the Mono Camera, Stereo Camera, and RGBD Camera. Additionally, it delves into the utilization of trigonometric functions for calculating depth from a single image while considering the horizontal field of view (HFOV).

# Depth Estimation Methods

In this file, we explore the fundamental concepts and methods used to estimate depth from cameras, which is essential in computer vision for applications like virtual reality, autonomous navigation, and augmented reality.

## Mono Camera
Discusses the challenges of estimating depth from a single-camera system and introduces techniques to infer depth information.

* `Motion-based Approaches`: Explores the use of motion cues in the scene to estimate depth, including optical flow algorithms and visual odometry techniques.

* `Trigonometric Functions`: Describes how trigonometry can help calculate the distance to an object based on its angular size and the camera's focal length.

* `Depth from Defocus`: Explains the concept of estimating depth by analyzing the blur of objects at different distances from the camera.

## Stereo Camera
Introduces the concept of stereo cameras, which mimic human binocular vision, and explains how they estimate depth by capturing images from slightly different viewpoints.

* `Triangulation Using 2 Cameras`: Illustrates the triangulation principle using two cameras and discusses how the depth is inversely proportional to the disparity.

* `Stereo Correspondence`: Explains how stereo correspondence algorithms match pixels between left and right images to compute disparity and estimate depth.

* `Structure from Motion`: Describes the use of multiple camera views in Structure from Motion (SfM) to reconstruct a 3D point cloud and obtain depth information.

# RGBD Camera
Introduces RGBD cameras, which provide color and depth information for each pixel, and discusses technologies like Time-of-Flight (ToF) sensing and structured light.

* `Time-of-Flight`: Explains how ToF cameras measure the time it takes for light to bounce back from objects to compute depth.

* `Structured Light`: Describes the structured light approach used in RGBD cameras to estimate depth by analyzing patterns projected onto objects.

# Depth from image calculation using HFOV

This document provides guidance on how to determine the depth from a camera to each pole in an image. It leverages known pole diameters and the horizontal field of view (HFOV) of the camera, making use of trigonometric functions to achieve accurate depth estimations.

## Calculating the Angle
The first step in this depth estimation process involves calculating the angular size of each pole in the image. This is accomplished using the following formula:

Angle (in degrees) = (Apparent width of the pole in pixels / Image width in pixels) × HFOV

## Calculating the Distance to Each Pole

Once you have determined the angle of each pole, you can proceed to calculate the distance from the camera to each pole using trigonometric functions. This calculation assumes that the camera is at the center of the image, and the poles are at the same height from the ground. The formula for calculating the distance to a pole is as follows:

Distance to the pole (in centimeters) = (Actual pole diameter / 2) / tan(Angle for the pole / 2)

# Conclusion

This project provided a comprehensive overview of depth estimation techniques using various camera types. From Mono Cameras with motion-based approaches and trigonometric functions to Stereo Cameras employing triangulation and correspondence algorithms, and RGBD Cameras utilizing ToF and structured light, we explored diverse methodologies.

Additionally, we covered a practical application - estimating depth from images using the Horizontal Field of View (HFOV) and trigonometry, enabling accurate distance calculations for objects like poles.