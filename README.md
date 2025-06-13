# 🐾 Object Detection Model: Indonesian Endangered Wildlife

Repositori ini digunakan untuk mengembangkan model deteksi objek (**object detection**) yang difokuskan pada **hewan-hewan yang terancam punah di Indonesia**. Proyek ini ditujukan sebagai *Minimum Viable Product* (MVP) untuk membantu konservasi dan pemantauan satwa liar menggunakan teknologi visi komputer.

Model yang **diimplementasikan langsung** dan digunakan secara mendalam dalam proyek ini adalah **RetinaNet dengan backbone ResNet-50 dan FPN**, sementara model YOLOv8n juga dicoba sebagai pembanding.

---

## 📌 Daftar Kategori (Kelas Objek)

Model dilatih untuk mengenali 11 spesies hewan berikut:

1. Anoa
2. Babirusa
3. Biawak Pohon Biru
4. Harimau Sumatra
5. Jalak Bali
6. Kakatua Jambul Kuning
7. Kera Hitam
8. Orangutan
9. Owa Jawa
10. Rusa Bawean
11. Siamang

---

## ⚙️ Arsitektur Model

### ✅ Implementasi Utama: **RetinaNet (ResNet50 + FPN)**

* Framework: TensorFlow
* Format model: `SavedModel`
* Data format: TFRecord
* Log dan evaluasi tersedia

### ⚡Model Uji Coba Tambahan: **YOLOv8n**

* Framework: [Ultralytics YOLOv8](https://docs.ultralytics.com)
* Format model: `.pt`, `.onnx`, `.tfjs`
* Data format: YOLOv8 format

---

## 📁 Struktur Direktori

```
├── Deployment/     # REST API menggunakan FastAPI untuk inference
├── Models/         # Model hasil pelatihan (YOLOv8 dan RetinaNet)
├── Notebooks/      # Notebook untuk pelatihan, evaluasi, eksperimen
├── Utils/          # Script bantu seperti image scraping dari Google
```

---

## 📂 Dataset

Dataset diperoleh dari Roboflow dan sudah melalui proses anotasi:

🔗 **[Indonesian Endangered Wildlife Detection Dataset (Roboflow)](https://universe.roboflow.com/rioooranteproject/indonesian-endangered-wildlife-detection-dataset/)**

* RetinaNet: format **TFRecord**
* YOLOv8n: format **YOLOv8 (image + label .txt)**

---

## 🚀 Cara Menjalankan API Inference

1. **Install dependencies:**

```bash
pip install -r requirements.txt
```

2. **Jalankan FastAPI server:**

```bash
uvicorn main:app --host 0.0.0.0 --port 5000 --reload
```

API akan aktif di `http://localhost:5000`

---

## 🧪 Teknologi dan Framework

* **TensorFlow** (RetinaNet implementation)
* **Ultralytics YOLOv8**
* **Roboflow** (dataset handling & format conversion)
* **FastAPI** (untuk REST API)
* **OpenCV**, **NumPy**, **Selenium**, **Beautiful Soup** dan berbagai modul lainnya

---

## 📊 Log & Evaluasi

* Log pelatihan mencatat metrik seperti:

  * `loss`
  * `precision`
  * `recall`
  * `mean Average Precision (mAP)`
