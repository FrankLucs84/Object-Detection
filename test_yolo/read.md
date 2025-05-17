# ⚡ YOLO - You Only Look Once: Architettura e Funzionamento

## 📖 Introduzione

**YOLO (You Only Look Once)** è una delle architetture più popolari per l’**object detection in tempo reale**. Introdotto da Joseph Redmon nel 2016, ha rivoluzionato il settore proponendo un approccio **single-shot**, capace di rilevare oggetti in un’unica passata di rete neurale.

📚 *Riferimento principale*:  
Redmon, J., Divvala, S., Girshick, R., & Farhadi, A. (2016).  
*You Only Look Once: Unified, Real-Time Object Detection*.  
[https://arxiv.org/abs/1506.02640](https://arxiv.org/abs/1506.02640)

---

## 🧠 Idea chiave

YOLO considera l’object detection come un **problema di regressione**:  
> “Divide l’immagine in griglie e per ciascuna predice direttamente bounding boxes e classi, in un’unica passata.”

Questo approccio è estremamente **veloce**, rendendolo adatto per applicazioni **real-time** su dispositivi embedded o edge.

---

## ⚙️ Architettura di YOLO

### 1. 📷 Input Image
- L’immagine è ridimensionata (tipicamente 416×416 o 640×640).
- È divisa in una **griglia S × S** (es. 13×13).

### 2. 🧮 Griglia predittiva
- Ogni cella predice:
  - **B** bounding box (centro, larghezza, altezza).
  - Score di confidenza.
  - Distribuzione delle **classi C**.

### 3. 🧠 Rete CNN
- Passa l’immagine attraverso una **CNN profonda** (es. Darknet, CSPNet).
- Produce un tensore di output con dimensioni `(S, S, B×5 + C)`.

---

## 🔍 Pipeline di Elaborazione

1. L’immagine è **divisa in griglie**.
2. Per ogni cella si predice:
   - Posizione box relativa.
   - Confidenza che l’oggetto esista.
   - Classi softmax.
3. Si applica il **Non-Maximum Suppression (NMS)** per filtrare i box sovrapposti.

---

## 🚦 Caratteristiche principali

| Caratteristica            | Descrizione                                                             |
|---------------------------|-------------------------------------------------------------------------|
| Architettura              | CNN pura                                                                |
| Modalità operativa        | Regressione diretta box + classi                                        |
| Velocità                  | 🔥 Estremamente elevata (decine di FPS)                                 |
| NMS                       | ✅ Richiesto                                                             |
| Output                    | Tensore `(S, S, B×5 + C)`                                                |
| Scalabilità               | Diverse versioni: YOLOv3, v4, v5, v7, v8, Nano...                        |
| Addestrabilità            | Semplice da addestrare anche su piccoli dataset                         |
| Interpretabilità          | ❌ Limitata rispetto a modelli con attention                            |

---

## 📈 Evoluzione delle versioni

- **YOLOv1** (2016): modello iniziale.
- **YOLOv3**: miglioramento architetturale con Darknet-53.
- **YOLOv4**: introduzione di CSPDarknet e nuove tecniche di training.
- **YOLOv5**: scritto in PyTorch da Ultralytics (non ufficiale, ma popolarissimo).
- **YOLOv7**: multitask head + architettura ottimizzata.
- **YOLOv8**: auto-anchor, supporto per segmentation e tracking.

---

## ✅ Vantaggi

- **Velocità eccezionale** anche su CPU o GPU modeste.
- Adatto per **real-time video analysis**, **robotica**, **automotive**.
- Rete singola per tutti i compiti: detection + classificazione + localizzazione.
- Molte implementazioni ottimizzate disponibili (TensorRT, OpenVINO, ONNX).

---

## ❌ Limiti noti

- Precisione inferiore su **oggetti piccoli o sovrapposti**.
- Richiede **NMS manuale**, quindi non è completamente end-to-end.
- La divisione in griglie può introdurre errori se un oggetto cade tra due celle.

---

## 📚 Risorse utili

- 🔗 Paper originale: [https://arxiv.org/abs/1506.02640](https://arxiv.org/abs/1506.02640)
- 🔗 YOLOv5 GitHub: [https://github.com/ultralytics/yolov5](https://github.com/ultralytics/yolov5)
- 🔗 YOLOv8: [https://docs.ultralytics.com](https://docs.ultralytics.com)

---

## 🧩 Conclusione

YOLO ha ridefinito l’object detection puntando su **efficienza, leggerezza e velocità**, rendendola utilizzabile in tempo reale su hardware a bassa potenza. È la scelta ideale quando i requisiti computazionali sono stringenti e la rapidità è fondamentale.

