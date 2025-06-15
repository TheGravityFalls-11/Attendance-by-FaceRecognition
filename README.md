# 🎯 Face Recognition Attendance System

A simple Face Recognition-based Attendance System using **DeepFace**, **OpenCV**, and **Facenet embeddings**.

---

## 📂 Project Structure

```
ATTENDANCE PROJECT/
│
├── dataset/             # Contains training images (one folder per person)
├── frontend/
│   ├── app.py           # Web interface (optional)
│   ├── index.html
│   └── style.css
│
├── attendance.csv       # Stores attendance records
├── encodings.pkl        # Stored embeddings for known faces
├── recognize_and_mark.py  # Main face recognition attendance code
├── requirements.txt     # Required Python packages
├── save_images.py       # To save images into dataset
├── train_model.py       # To generate face embeddings
└── venv/                # Virtual environment (ignored in git)
```

---

## 🚀 Features

- Detects faces in real-time using webcam.
- Recognizes faces using **Facenet embeddings** via **DeepFace**.
- Marks attendance into `attendance.csv` only once per person per session.
- Draws bounding boxes with names on video feed.

---

## 🔧 Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/TheGravityFalls-11/Attendance-by-FaceRecognition.git
cd Attendance-by-FaceRecognition
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows
```

### 3️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

### 4️⃣ Dataset Preparation

- Create a folder named `dataset/`
- Inside, create subfolders for each person:
  ```
  dataset/
    ├── Person1/
    ├── Person2/
  ```
- Add multiple front-face images for each person.

### 5️⃣ Generate Encodings

```bash
python train_model.py
```

This will generate `encodings.pkl` file.

### 6️⃣ Run Face Recognition Attendance

```bash
python recognize_and_mark.py
```

Press **q** to quit the webcam.

---

## ⚠ Important Notes

- `.gitignore` is configured to ignore:
  - Personal dataset images (`dataset/`)
  - Virtual environment (`venv/`)
  - Pickle & CSV files
- Attendance records are stored in `attendance.csv`.

---

## 🛠 Technologies Used

- Python 🐍
- OpenCV 🎥
- DeepFace 🧠
- Facenet Embeddings 🔬
- Pandas 📊

---

## 🤝 Contributions

PRs and improvements are welcome!

---

## 🔒 Disclaimer

Your dataset contains personal images. Keep `dataset/` local and never upload personal images to public repositories.

