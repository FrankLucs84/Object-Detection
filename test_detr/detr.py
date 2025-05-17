from transformers import DetrImageProcessor, DetrForObjectDetection
import torch
from PIL import Image, ImageDraw, ImageFont
import os
import random

# 📁 Percorso immagine
image_path = r"C:\Users\frank\Desktop\Object Detection\test_detr\Depositphotos_174628074_XL.jpg"
image = Image.open(image_path).convert("RGB")

# 🧠 Caricamento modello
processor = DetrImageProcessor.from_pretrained("facebook/detr-resnet-50", revision="no_timm")
model = DetrForObjectDetection.from_pretrained("facebook/detr-resnet-50", revision="no_timm")

# 🔁 Preprocessing
inputs = processor(images=image, return_tensors="pt")
outputs = model(**inputs)

# 📐 Post-processing
target_sizes = torch.tensor([image.size[::-1]])
results = processor.post_process_object_detection(
    outputs, 
    target_sizes=target_sizes,
    threshold=0.9
)[0]

# 📂 Crea cartella 'risultati'
output_dir = os.path.join(os.path.dirname(image_path), "risultati")
os.makedirs(output_dir, exist_ok=True)

# ✏️ Disegna box + label
draw = ImageDraw.Draw(image)

# 🎨 Colori distinti per classe
unique_labels = list(set(results["labels"].tolist()))
label_colors = {label: tuple(random.choices(range(64, 256), k=3)) for label in unique_labels}

# 📏 Font leggibile
try:
    font = ImageFont.truetype("arial.ttf", size=130)
except IOError:
    font = ImageFont.load_default()
    print("⚠️ Font TrueType non trovato, uso font predefinito.")

# 🔁 Loop predizioni
for score, label, box in zip(results["scores"], results["labels"], results["boxes"]):
    box = [round(i, 2) for i in box.tolist()]
    label_id = label.item()
    label_text = f"{model.config.id2label[label_id]} {round(score.item(), 2)}"
    color = label_colors[label_id]

    print(f"Detected {label_text} at {box}")

    draw.rectangle(box, outline=color, width=3)

    # 🧮 Calcolo dimensioni testo con textbbox
    text_bbox = draw.textbbox((0, 0), label_text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    text_origin = (box[0], box[1] - text_height if box[1] - text_height > 0 else box[1])

    # 🏷️ Sfondo + testo
    draw.rectangle(
        [text_origin, (text_origin[0] + text_width, text_origin[1] + text_height)],
        fill=color
    )
    draw.text(text_origin, label_text, fill="white", font=font)

# 💾 Salva immagine annotata
output_path = os.path.join(output_dir, "output_detr.jpg")
image.save(output_path)
print(f"\n✅ Immagine salvata in: {output_path}")
