# 📊 Prediksi Software Defect NASA CM1 dengan SMOTE & Machine Learning

Tugas Besar Data Mining  
Kelompok 2 - Diploma IV Teknik Informatika  
Universitas Logistik dan Bisnis Internasional, Bandung  
Semester Genap 2025

## 👥 Anggota Kelompok

- Aliffathur Muhammad Revan — 714220066  
- Hammi Ahlan Abdulmujib — 714220062  
- Andhika Muhammad Fatiha — 714220063  

---

## 🧩 Deskripsi Kasus

Penelitian ini berfokus pada prediksi keberadaan *defect* (cacat) dalam perangkat lunak menggunakan dataset NASA CM1 dari NASA Metrics Data Program (MDP). Dataset ini berisi metrik perangkat lunak dan status defect dari modul-modulnya. Masalah utama yang dihadapi adalah ketidakseimbangan kelas (class imbalance), di mana modul non-defect jauh lebih banyak dibanding modul defect.

---

## 💾 Sumber Dataset

Dataset final hasil preprocessing disimpan di repository ini:  
📄 [`cm1_final.csv`](https://github.com/nekowawolf/NASA-promise-dataset/blob/main/cm1_final-23-07-2025.csv)

Dataset Raw di simpan di sini:  
📄 [`cm1.csv`](https://github.com/ApoorvaKrisna/NASA-promise-dataset-repository/)


Dataset terdiri dari:
- 498 baris data
- 21 fitur numerik
- 1 kolom target: `defects` (0 = tidak cacat, 1 = cacat)
- Sudah melalui proses normalisasi dan cleaning

---

## ⚙️ Langkah Preprocessing

1. **Menghapus Missing Values**  
2. **Label Encoding**: Konversi label defect ke numerik  
3. **Normalisasi** fitur numerik menggunakan `MinMaxScaler`  
4. **Menangani Ketidakseimbangan Kelas** dengan **SMOTE**  
5. **Split Data**: 80% train, 20% test

---

## 🤖 Algoritma yang Digunakan

Tiga algoritma klasifikasi digunakan dan dibandingkan:

- **Logistic Regression**
- **Random Forest**
- **K-Nearest Neighbors (KNN)**

Semua model dilatih setelah proses oversampling dengan SMOTE.

---

## 📈 Evaluasi & Hasil

Evaluasi dilakukan menggunakan:
- **Accuracy**
- **Precision**
- **Recall**
- **F1-Score**
- **Confusion Matrix**

| Model               | Akurasi | Recall (Defect) | F1-Score (Defect) |
|---------------------|---------|------------------|-------------------|
| **Logistic Regression** | 82%     | **75%**           | **0.50**          |
| Random Forest        | 83%     | 0%               | 0.00              |
| KNN                  | 68%     | 33%              | 0.20              |

📌 **Logistic Regression menghasilkan performa terbaik**, dengan kemampuan deteksi defect mencapai 75% (recall), menjadikannya model yang paling cocok digunakan dalam konteks klasifikasi cacat perangkat lunak.

---

## 💻 Cara Menjalankan

### 1. Jalankan di Google Colab (direkomendasikan)

Klik tombol berikut untuk membuka notebook di Colab:  
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/)

Lalu import file ini ke google collab:  
[Notebook](https://github.com/nekowawolf/tugas-besar-datamining-kelompok2/tree/main/notebook)

### 2. Jalankan secara lokal

▶️ Cara Menjalankan

### 0. Membuat Virtual Environment (OPSIONAL - Jika DIbutuhkan)
```bash
python3 -m venv env
source env/bin/activate
```

### 1. Install dependencies yang dibutuhkan
```bash
pip install -r src/requirements.txt
```

### 2. Jalankan secara lokal

```bash
python src/main.py
```
