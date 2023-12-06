from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.yaml")  # build a new model from scratch

# Use the model
results = model.train(data='C:\\Users\\pedro\\VS_CODE\\PS_EDRA_YOLOV8n\\config.yaml', epochs=100)  # train the model