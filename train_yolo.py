from ultralytics import YOLO

# Reprise de l'entraînement avec ton modèle précédent
model = YOLO("runs/detect/train4/weights/best.pt")  # ou 'yolov8n.pt' pour repartir de zéro

# Lance l'entraînement
model.train(
    data="data/data.yaml",
    epochs=50,
    resume=True  # ou False si tu veux tout reprendre
)
