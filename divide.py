import os
import random
import shutil

# Chemins des dossiers
base_path = "data"
image_train_dir = os.path.join(base_path, "images", "train")
label_train_dir = os.path.join(base_path, "labels", "train")
image_val_dir = os.path.join(base_path, "images", "val")
label_val_dir = os.path.join(base_path, "labels", "val")

# Pourcentage des images à mettre dans le dossier val
VAL_PERCENT = 0.2  # 20%

# Création des dossiers val s'ils n'existent pas
os.makedirs(image_val_dir, exist_ok=True)
os.makedirs(label_val_dir, exist_ok=True)

# Liste des fichiers image (filtrée sur .jpg ou .png)
image_files = [f for f in os.listdir(image_train_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

# Sélection aléatoire
val_sample = random.sample(image_files, int(len(image_files) * VAL_PERCENT))

# Traitement
for img_file in val_sample:
    # Nom du fichier sans extension
    basename = os.path.splitext(img_file)[0]

    # Chemins des fichiers
    img_src = os.path.join(image_train_dir, img_file)
    img_dst = os.path.join(image_val_dir, img_file)

    label_src = os.path.join(label_train_dir, basename + ".txt")
    label_dst = os.path.join(label_val_dir, basename + ".txt")

    # Déplacer l'image
    shutil.move(img_src, img_dst)

    # Déplacer le label s'il existe
    if os.path.exists(label_src):
        shutil.move(label_src, label_dst)
    else:
        print(f"⚠️  Label manquant pour {img_file}")

print(f"✅ {len(val_sample)} images déplacées dans le dossier validation.")
