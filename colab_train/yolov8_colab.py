from ultralytics import YOLO

model = YOLO("C:\\Users\\pedro\\VS_CODE\\PS_EDRA_YOLOV8n\\colab_train\\colab_model.pt")

results = model(source=0, show=True, conf=0.6, save=True)