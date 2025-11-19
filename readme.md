# SDXL Juggernaut Lightning Renderer

This project is a **Python-based image generation tool** that uses an **SDXL Juggernaut Lightning 4-Step model** to generate images from text prompts. In addition to single-image generation, it includes a **batch mode** that automatically produces multiple images using random seeds.

The program also provides a **live preview window (Tkinter)** and automatically stores all generated images in the `render/` directory.

---

## ✨ Features

- Text-to-image generation using **Stable Diffusion XL (SDXL)**
- Uses the **Juggernaut Lightning 4-Step Model** for extremely fast inference
- **Batch mode** with random seed generation
- Live 512×512 image preview via **Tkinter**
- Automatic creation of the `render/` output directory
- GPU acceleration via **CUDA + PyTorch (float16)**
- Memory optimizations (Attention Slicing, xFormers, VAE Slicing)

---

## 🚀 Requirements

- Python **3.10+ (64-bit)**
- NVIDIA GPU with CUDA support
- SDXL model file placed in the project directory:

```
sdxl_juggernaut_4step.safetensors
```

---

## 📦 Installation

Install all required dependencies:

```bash
pip install -r requirements.txt
```

Ensure the SDXL model file is present in the same folder as the script.

---

## ▶️ Running the Program

Start the renderer with:

```bash
python main.py
```

After launching, the program will ask you to:

- Enter a **positive prompt**
- Enter a **negative prompt** (optional)
- Choose between **single render** or **batch mode**

---

## 🧪 Batch Mode

Batch mode automatically generates multiple images based on your prompt:

- A new random seed for every image
- Live preview of each render
- Automatic PNG export
- Stops after reaching the user-defined maximum number of images

---

## 📁 Folder Structure

```
/project
 ├── main.py
 ├── requirements.txt
 ├── README.md
 ├── sdxl_juggernaut_4step.safetensors
 └── render/
```

---

## ⚠️ Notes

- This program is labeled as **Early Alpha**.
- GPU memory usage is optimized, but very small GPUs may still encounter out-of-memory issues.
- Intended for local testing only.

---

## 📝 License

No license has been specified yet — consider adding one if needed.
