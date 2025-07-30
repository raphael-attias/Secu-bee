from ultralytics import YOLO

# Charger ton modèle
model = YOLO("data/runs/detect/train3/weights/best.pt")

# Analyser la vidéo téléchargée
model.predict(
    source="inputs/videos/abeilles1.mp4",
    save=True,
    save_txt=True,
    save_conf=True,
    project="outputs",
    name="abeilles_analysis"
)
