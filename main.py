import ultralytics
import os
import cv2
from datetime import datetime
from pytz import timezone
import supervision as sv

from dataset import Dataset


# https://blog.roboflow.com/how-to-train-yolov8-on-a-custom-dataset/
def show_sample_image(image_path):
    image = cv2.imread(image_path)
    model = ultralytics.YOLO('yolov8n.pt')

    results = model.predict(image, conf=0.25)[0]
    print(results[0].boxes.xyxy)
    detections = sv.Detections.from_ultralytics(results[0])

    bounding_box_annotator = sv.BoundingBoxAnnotator()
    label_annotator = sv.LabelAnnotator()

    annotated_image = bounding_box_annotator.annotate(scene=image, detections=detections)
    annotated_image = label_annotator.annotate(scene=annotated_image, detections=detections)

    sv.plot_image(annotated_image)
    

# -------------------------------------------------------- main ---------------------------------------------------- #
print('starting')
# show_sample_image(os.path.join(os.getcwd(), f'dog.jpeg'))
# dataset = Dataset(val_ratio=0.2, test_ratio=0.1)
# dataset.save_data()
now = datetime.now(timezone('Asia/Jerusalem'))
save_dir = os.path.join(os.getcwd(), f'training_results_{now.strftime("%d-%m-%Y_%H:%M:%S")}')
os.mkdir(save_dir)
model = ultralytics.YOLO('yolov8n.pt')
results = model.train(data='config.yaml', epochs=2, project=save_dir)

print("finished")