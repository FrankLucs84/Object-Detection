# 📦 Guida Scientifica all’Object Detection: Confronto tra YOLO e DETR

## 📘 Introduzione

L’**Object Detection** è una delle sfide fondamentali della **computer vision**, con l’obiettivo di **identificare e localizzare oggetti** all’interno di immagini. A differenza della classificazione, essa restituisce sia la **categoria dell’oggetto**, sia le **coordinate spaziali (bounding box)**.

Due modelli rappresentativi di approcci differenti sono:

- **YOLO (You Only Look Once)** – ottimizzato per la velocità.
- **DETR (DEtection TRansformer)** – basato su Transformer e attenzione globale.

---

## 🧱 1. Architettura di Base

| Caratteristica        | YOLO                                                | DETR                                                  |
|-----------------------|-----------------------------------------------------|--------------------------------------------------------|
| Architettura          | CNN (Convolutional Neural Network)                  | Transformer Encoder-Decoder                           |
| Tipo di approccio     | Regressione diretta su griglie                      | Sequence-to-sequence con attenzione globale           |
| Post-processing       | Necessita NMS (Non-Max Suppression)                 | Nessun NMS – Hungarian Matching                       |
| Output                | Bounding box + classi                               | Matching tra query learnable e oggetti reali          |

### 🔹 YOLO
YOLO segmenta l’immagine in griglie e per ciascuna predice:
- Coordinate del bounding box.
- Confidenza.
- Classe dell’oggetto.

**📖 Riferimento**:  
Redmon, J. et al. (2016). *You Only Look Once: Unified, Real-Time Object Detection*.  
<https://arxiv.org/abs/1506.02640>

### 🔹 DETR
DETR elimina il classico schema CNN+NMS e utilizza un Transformer con:
- Query learnable per ogni oggetto potenziale.
- Attention meccanismo globale.
- Hungarian Matching per associare predizione e ground truth.

**📖 Riferimento**:  
Carion, N. et al. (2020). *End-to-End Object Detection with Transformers*.  
<https://arxiv.org/abs/2005.12872>

---

## 🔍 2. Meccanismo di Rilevamento

| Aspetto                      | YOLO                            | DETR                             |
|-----------------------------|----------------------------------|----------------------------------|
| Predizione                  | Diretta (box + classe)          | Matching query-oggetto           |
| Eliminazione box ridondanti | NMS                              | Hungarian Matching               |
| Posizionamento              | Diretto tramite CNN             | Attention + Positional Encoding  |

---

## ⚙️ 3. Performance Comparata

| Metica                         | YOLO                             | DETR                             |
|--------------------------------|----------------------------------|----------------------------------|
| 🔄 Velocità                    | 🔥 Molto alta (real-time)         | 🐢 Più lenta (migliorata in DETR-2) |
| 🎯 Accuratezza oggetti piccoli| ❌ Limitata                       | ✅ Elevata grazie all’attention  |
| 🧠 Training                    | Facile                           | Lungo e con dataset ampio        |
| 📏 Scalabilità                | Elevata (YOLOv7, v8, Nano, etc.) | Limitata (maggior uso di GPU)    |

---

## 🛠️ 4. Applicazioni Pratiche

| Scenario                           | YOLO         | DETR         |
|------------------------------------|--------------|--------------|
| Sistemi embedded (edge devices)    | ✅ (es. YOLOv5s, Nano) | ❌ Troppo pesante |
| Accuratezza estrema (medico, industria) | ❌        | ✅            |
| Visione in tempo reale             | ✅            | ❌            |
| Progetti accademici e R&D         | ✅/❌         | ✅            |

---

## 🔬 5. Sintesi Concettuale

- **YOLO**: Efficiente, compatto, adatto per l’inferenza rapida in ambienti con risorse limitate.
- **DETR**: Elegante, end-to-end, promettente per future evoluzioni della visione artificiale, ma computazionalmente intensivo.

---

## 📈 6. Evoluzioni Recenti

### 🔧 YOLOv7
- Head multitasking
- Moduli Efficient Layer Aggregation
- Performance eccellenti su COCO

### 🔧 Deformable DETR / DETR-2
- Sparse attention per velocizzare l'addestramento.
- Supporto per backbone ibridi CNN + Transformer.

---

## 📚 Riferimenti in Stile APA

- Redmon, J., Divvala, S., Girshick, R., & Farhadi, A. (2016). *You Only Look Once: Unified, Real-Time Object Detection*. arXiv preprint arXiv:1506.02640. <https://arxiv.org/abs/1506.02640>

- Carion, N., Massa, F., Synnaeve, G., Usunier, N., Kirillov, A., & Zagoruyko, S. (2020). *End-to-End Object Detection with Transformers*. arXiv preprint arXiv:2005.12872. <https://arxiv.org/abs/2005.12872>

---
