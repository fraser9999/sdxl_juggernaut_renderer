# SDXL Juggernaut Lightning Renderer

Dieses Projekt ist ein **Python‑basiertes Bildgenerierungstool**, das ein **SDXL Juggernaut Lightning 4‑Step Modell** verwendet, um Bilder aus Textprompts zu erzeugen. Neben dem Einzelbild‑Modus verfügt es über einen **Batch‑Modus**, der automatisiert mehrere Bilder mit zufälligen Seeds erzeugt.

Das Programm bietet zusätzlich ein **grafisches Live‑Preview‑Fenster (Tkinter)** und speichert alle generierten Bilder automatisch im Ordner `render/`.

---

## ✨ Funktionen

- Text‑to‑Image Rendering über **Stable Diffusion XL (SDXL)**
- Verwendung des **Juggernaut Lightning 4‑Step Modells** für extrem schnelle Inference
- **Batch‑Modus** mit zufälligen Seeds
- Live‑Bildvorschau im **512×512 Tkinter‑Previewfenster**
- Automatische Erstellung des Speicherordners `render/`
- GPU‑Nutzung via **CUDA + PyTorch (float16)**
- Speicheroptimierungen (Attention Slicing, xFormers, VAE Slicing)

---

## 🚀 Voraussetzungen

- Python **3.10+ (64‑bit)**
- NVIDIA GPU mit CUDA‑Unterstützung
- Das SDXL‑Modell **sdxl_juggernaut_4step.safetensors** muss sich im Programmverzeichnis befinden

---

## 📦 Installation

```bash
pip install -r requirements.txt
```

Modell-Datei in das Projektverzeichnis legen:
```
sdxl_juggernaut_4step.safetensors
```

---

## ▶️ Ausführung

```bash
python main.py
```

Nach Start fragt das Programm:
- **Prompt eingeben**
- **Negativen Prompt eingeben** (optional)
- Wahl zwischen **Einzelmodell** oder **Batch‑Modus**

---

## 🧪 Batch‑Modus

Der Batch‑Modus generiert automatisch mehrere Bilder:

- automatisch neue Seeds
- Preview jedes Bilds
- automatische Speicherung als PNG

Der Modus stoppt, sobald die angegebene Bildanzahl erreicht ist.

---

## 📁 Verzeichnisstruktur

```
/project
 ├── main.py
 ├── requirements.txt
 ├── README.md
 ├── sdxl_juggernaut_4step.safetensors
 └── render/
```

---

## ⚠️ Hinweise

- Das Programm ist als **Early Alpha** gekennzeichnet.
- Die GPU‑Speichernutzung ist optimiert, dennoch kann bei sehr kleinen GPUs Out‑of‑Memory auftreten.
- Nur für lokale Tests gedacht.

---

## 📝 Lizenz

Keine explizite Lizenz angegeben — bitte entsprechend ergänzen.

