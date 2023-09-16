import os
from Detector import BallDetector

if __name__ == "__main__":
    # Specify the folder path where your images are located and get stored
    location_folder = '1. Classical View/images/'
    store_folder = '1. Classical View/Detected_images/'
    
    # List all the image files in the folder
    image_files = [f for f in os.listdir(location_folder) if f.endswith('.jpg')]

    for image_name in image_files:
        location_path = os.path.join(location_folder, image_name)

        # Create a BallDetector instance for each image
        detector = BallDetector(location_path)
        detector.detect_balls()
        # detector.display_result() # Show the result
        store_path = os.path.join(store_folder, image_name)
        detector.save_result(store_path)  # Save the result
