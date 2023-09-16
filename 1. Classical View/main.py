from Detector import BallDetector

if __name__ == "__main__":
    detector = BallDetector('1. Classical View/images/b_010.jpg')
    detector.detect_balls()
    detector.display_result()
    # detector.save_result('1. Classical View/Detected_images/rb_000.jpg')  # Uncomment to save the result
