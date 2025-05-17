# 🔍 DETR - DEtection TRansformer: Architettura e Funzionamento

## 📖 Introduzione

**DETR (DEtection TRansformer)** è un modello per l’object detection introdotto da Facebook AI Research (FAIR) nel 2020. È il primo framework **end-to-end** che utilizza l’architettura **Transformer**, tipica del NLP, per la rilevazione degli oggetti all’interno di immagini.

📚 *Riferimento principale*:  
Carion, N., Massa, F., Synnaeve, G., Usunier, N., Kirillov, A., & Zagoruyko, S. (2020).  
*End-to-End Object Detection with Transformers*. arXiv:2005.12872.  
<https://arxiv.org/abs/2005.12872>

---

## 🧠 Idea chiave

DETR riformula il problema del rilevamento oggetti come una **trasduzione diretta da immagine a sequenza di oggetti**:  
> “Data un’immagine, produce direttamente un set di box con classi, senza alcuna euristica come anchor box o non-max suppression.”

---

## ⚙️ Architettura di DETR

### 1. 🔍 Feature Extractor (CNN Backbone)
- Solitamente una **ResNet-50 o ResNet-101**.
- Estrae una **mappa di caratteristiche** (feature map) dall’immagine.

### 2. 🔄 Transformer Encoder-Decoder
- **Encoder**: codifica le feature globalmente usando self-attention.
- **Decoder**: riceve un numero fisso di **query vettoriali (es. 100)**, ciascuna delle quali rappresenta una potenziale predizione oggetto.

### 3. 🎯 Prediction Heads
- Ogni output del decoder è passato a:
  - Un **MLP per la bounding box** (`[cx, cy, w, h]`).
  - Una **softmax per la classificazione**.

---

## 🔬 Dettagli chiave del funzionamento

- Le **object queries** sono **parametri appresi** che "cercano" gli oggetti nella scena.
- L’**output è una sequenza di predizioni** con punteggio di confidenza e coordinate spaziali.
- Si utilizza un algoritmo di **Hungarian Matching** per associare predizioni e oggetti reali nel calcolo della loss.
- La loss totale include:
  - **Classification loss** (Cross-Entropy).
  - **Bounding box loss** (L1 + GIoU loss).

---

## 🧪 Pipeline di elaborazione

1. **Input immagine** → CNN (es. ResNet) → Feature Map.
2. **Feature Map** → Linearizzata + Positional Encoding → Transformer Encoder.
3. **Decoder** + Query vettoriali → Predizioni (classi + box).
4. **Post-processing**: Matching predizione-verità a terra via Hungarian Algorithm.

---

## 🧾 Caratteristiche principali

| Caratteristica                 | Dettaglio                                                       |
|-------------------------------|------------------------------------------------------------------|
| Architettura                  | Transformer Encoder-Decoder                                      |
| Componente CNN                | Solo per l’estrazione iniziale delle feature (es. ResNet)       |
| Rimozione NMS                 | ✅ Eliminato (uso di Hungarian Matching)                         |
| End-to-End                    | ✅ Nessun bisogno di euristiche manuali                          |
| Numero di predizioni          | Fisso (es. 100 oggetti per immagine, alcuni possono essere "vuoti") |
| Interpretabilità              | ✅ Attention maps interpretabili                                 |
| Convergenza                   | ❌ Lenta (necessita training più lungo)                          |

---

## 📉 Limiti noti

- **Addestramento lento**: richiede più epoche rispetto a modelli classici.
- **Prestazioni iniziali inferiori su oggetti piccoli** (risolto in parte con *Deformable DETR*).
- **Inferenza più pesante** rispetto a modelli lightweight.

---

## 🚀 Evoluzioni di DETR

- **Deformable DETR**: introduce *multi-scale attention* e *sparse attention*, migliora su oggetti piccoli.
- **Conditional DETR**: migliora la stabilità delle predizioni.
- **DETR-2**: ottimizzazioni nella velocità e accuratezza, convergenza più rapida.

---

## 📚 Altri riferimenti

- Zhu, X. et al. (2021). *Deformable DETR: Deformable Transformers for End-to-End Object Detection*.  
  <https://arxiv.org/abs/2010.04159>

- Hugging Face repository:  
  <https://huggingface.co/facebook/detr-resnet-50>

---

## 🧩 Conclusione

DETR rappresenta una svolta concettuale nell’object detection, offrendo un approccio elegante e end-to-end che elimina molte complicazioni dei metodi tradizionali. Pur avendo dei limiti, ha aperto la strada a nuove architetture di visione artificiale basate sui Transformer.

