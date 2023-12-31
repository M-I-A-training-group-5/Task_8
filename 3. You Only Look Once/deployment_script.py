from ultralytics import YOLO

model = YOLO(r"Model_Weights.pt")

output = model.predict(source=r"yolo_test2.mov", classes=[0, 1, 2], show=True)

