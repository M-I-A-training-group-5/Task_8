import cv2
import numpy as np

class BallDetector:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = cv2.imread(image_path)
        self.hsv = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)

    def detect_balls(self):
        # Define the lower and upper bounds of the blue color in HSV
        lower_blue = np.array([110, 50, 50])
        upper_blue = np.array([130, 255, 255])

        # Define the lower and upper bounds of the red color in HSV
        lower_red1 = np.array([0, 50, 50])
        upper_red1 = np.array([10, 255, 255])
        lower_red2 = np.array([160, 50, 50])
        upper_red2 = np.array([180, 255, 255])

        # Create masks for blue and red colors
        blue_mask = cv2.inRange(self.hsv, lower_blue, upper_blue)
        red_mask1 = cv2.inRange(self.hsv, lower_red1, upper_red1)
        red_mask2 = cv2.inRange(self.hsv, lower_red2, upper_red2)
        red_mask = cv2.bitwise_or(red_mask1, red_mask2)

        # Apply Gaussian Blur to the masks
        blurred_blue_mask = cv2.GaussianBlur(blue_mask, (9, 9), 2)
        blurred_red_mask = cv2.GaussianBlur(red_mask, (9, 9), 2)

        # Detect Circles for Blue Balls
        blue_circles = cv2.HoughCircles(
            blurred_blue_mask,
            cv2.HOUGH_GRADIENT,
            dp=1,
            minDist=200,
            param1=80,
            param2=22.4,
            minRadius=10,
            maxRadius=200
        )

        # Detect Circles for Red Balls
        red_circles = cv2.HoughCircles(
            blurred_red_mask,
            cv2.HOUGH_GRADIENT,
            dp=1,
            minDist=200,
            param1=470,
            param2=23.4,
            minRadius=19,
            maxRadius=150
        )

        largest_red_circle = None
        largest_blue_circle = None

        # Initialize variables to track smallest and largest radii
        min_red_radius = float('inf')
        max_blue_radius = 0

        # Detect the smallest red and largest blue circles
        if blue_circles is not None:
            blue_circles = np.uint16(np.around(blue_circles))
            for circle in blue_circles[0, :]:
                center = (circle[0], circle[1])
                radius = circle[2]
                if radius > max_blue_radius:
                    max_blue_radius = radius
                    largest_blue_circle = (center, radius)

        if red_circles is not None:
            red_circles = np.uint16(np.around(red_circles))
            for circle in red_circles[0, :]:
                center = (circle[0], circle[1])
                radius = circle[2]
                if radius < min_red_radius:
                    min_red_radius = radius
                    largest_red_circle = (center, radius)

        # Draw the largest red and blue circles on the original image
        if largest_red_circle is not None:
            center, radius = largest_red_circle
            cv2.circle(self.image, center, radius, (255, 0, 0), 2)

        if largest_blue_circle is not None:
            center, radius = largest_blue_circle
            cv2.circle(self.image, center, radius, (0, 0, 255), 2)

    def display_result(self):
        cv2.imshow('Balls Detected', self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def save_result(self, output_path):
        cv2.imwrite(output_path, self.image)