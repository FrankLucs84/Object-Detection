import os
from ultralytics import YOLO
from ultralytics.utils import SETTINGS  # 👈 forzatura globale

# 🔁 Imposta path di output globale dentro test_yolo/
SETTINGS['runs_dir'] = os.path.join("test_yolo", "runs")

# 📁 Percorsi principali
image_path = os.path.join("test_yolo", "Depositphotos_174628074_XL.jpg")
model_path = os.path.join("test_yolo", "yolov8n.pt")
output_dir = os.path.join("test_yolo", "runs", "detect", "custom")
os.makedirs(output_dir, exist_ok=True)

# 📦 Caricamento modello
model = YOLO(model_path)

# 🚀 Inferenza e salvataggio completo
results = model.predict(
    source=image_path,
    save=True,
    save_txt=True,
    save_conf=True,
    save_dir=output_dir,
    conf=0.9
)

# 📝 Log leggibile
log_path = os.path.join(output_dir, "results_log.txt")
with open(log_path, "w", encoding="utf-8") as log_file:
    log_file.write("🔍 Risultati dell'inferenza YOLOv8:\n\n")
    for r in results:
        for box in r.boxes:
            cls_id = int(box.cls)
            cls_name = model.names[cls_id]
            conf = round(float(box.conf), 2)
            coords = [round(x, 2) for x in box.xyxy[0].tolist()]
            log_file.write(f"Detected {cls_name} with confidence {conf} at {coords}\n")

# 🔍 Verifica finale
label_dir = os.path.join(output_dir, "labels")
if os.path.exists(label_dir):
    print(f"📂 Etichette YOLO salvate in: {label_dir}")
else:
    print("⚠️ Nessuna cartella 'labels/' trovata. Verifica che ci siano predizioni.")

print(f"\n✅ Inferenzia completata.")
print(f"📸 Immagine annotata salvata in: {output_dir}")
print(f"📝 Log scritto in: {log_path}")
