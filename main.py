import ultralytics
import os
import cv2
from datetime import datetime
from pytz import timezone
import supervision as sv

from dataset import Dataset


# https://blog.roboflow.com/how-to-train-yolov8-on-a-custom-dataset/
def show_sample_image(image_path: str):
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

def track_in_video(weights_path: str, video_path: str):
    model = ultralytics.YOLO(weights_path)
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video.")
        return
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc('M','J','P','G'), fps, (frame_width, frame_height))
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        results = model(frame)
        for box in results[0].boxes:
            x1, y1, x2, y2, conf, cls = box.data.tolist()[0]
            label = f'{model.names[int(cls)]}: {conf:.2f}'
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
            cv2.putText(frame, label, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        cv2.imshow('YOLOv8 Detection', frame)
        out.write(frame)
        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    

# -------------------------------------------------------- main ---------------------------------------------------- #
print('starting')
""" shoing sample image """
# show_sample_image(os.path.join(os.getcwd(), f'dog.jpeg'))

""" rebuild dataset """
# dataset = Dataset(val_ratio=0.2, test_ratio=0.1)
# dataset.save_data()

""" training the model """
# now = datetime.now(timezone('Asia/Jerusalem'))
# save_dir = os.path.join(os.getcwd(), f'training_results_{now.strftime("%d-%m-%Y_%H:%M:%S")}')
# os.mkdir(save_dir)
# model = ultralytics.YOLO('yolov8n.pt')
# results = model.train(data='config.yaml', epochs=2, project=save_dir)

""" run on video """
weights_path = os.path.join("training_results_23-06-2024_17:18:37", "train", "weights", "best.pt")

video_path = "output.mp4"
track_in_video(weights_path, video_path)

print("finished")