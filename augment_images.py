import cv2
import os
import albumentations as A
from glob import glob

# Dossier d’entrée/sortie
input_dir = 'outputs/test_images'
output_dir = 'outputs/test_images_aug'

os.makedirs(output_dir, exist_ok=True)

# Transformations variées
transform = A.Compose([
    A.HorizontalFlip(p=0.5),
    A.RandomBrightnessContrast(p=0.3),
    A.MotionBlur(blur_limit=5, p=0.2),
    A.Rotate(limit=25, p=0.3),
    A.ShiftScaleRotate(shift_limit=0.05, scale_limit=0.05, rotate_limit=10, p=0.3)
])

# Application à chaque image
for img_path in glob(f"{input_dir}/*.jpg"):
    img = cv2.imread(img_path)
    name = os.path.basename(img_path).split('.')[0]
    for i in range(3):  # 3 augmentations par image
        augmented = transform(image=img)['image']
        cv2.imwrite(os.path.join(output_dir, f"{name}_aug{i}.jpg"), augmented)
