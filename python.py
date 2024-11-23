from ultralytics import YOLO
import os 

video_path = r'C:\Users\91708\Desktop\Untitled Folder\08fd33_4.mp4'

model=YOLO('yolov8x')
results = model.predict(video_path, save=True)
print(results[0])  
print("=========================")
for box in results[0].boxes:
    print(box)
