# 📊 Prediksi Software Defect NASA CM1 dengan SMOTE & Machine Learning

Tugas Besar Data Mining  
Kelompok 2 - Diploma IV Teknik Informatika  
Universitas Logistik dan Bisnis Internasional, Bandung  
Semester Genap 2025

## 👥 Anggota Kelompok & NIM

- Aliffathur Muhammad Revan — 714220066  
- Hammi Ahlan Abdulmujib — 714220062  
- Andhika Muhammad Fatiha — 714220063  

---

## 🧩 Deskripsi Kasus

Penelitian ini berfokus pada prediksi keberadaan *defect* (cacat) dalam perangkat lunak menggunakan dataset NASA CM1 dari NASA Metrics Data Program (MDP). Dataset ini mengandung metrik-metrik perangkat lunak serta informasi apakah suatu modul memiliki cacat atau tidak. Masalah utama adalah ketidakseimbangan kelas (class imbalance) antara modul yang *defect* dan tidak.

---

## 💾 Sumber Dataset

Dataset dapat ditemukan di repository kami:  
📁 [`NASA-promise-dataset`](https://github.com/ApoorvaKrisna/NASA-promise-dataset-repository)  
📄 File: `cm1.csv`

Dataset ini terdiri dari 498 baris dan 22 kolom, termasuk:
- 21 fitur numerik (seperti LOC, cyclomatic complexity, dll)
- 1 target label (`defects`) bernilai 0 (tidak cacat) atau 1 (cacat)

---

## ⚙️ Langkah Preprocessing

1. **Handling Missing Values**: Drop baris kosong.
2. **Label Encoding**: Pastikan label `defects` bertipe numerik.
3. **Normalisasi Fitur**: Menggunakan `MinMaxScaler` untuk rentang 0–1.
4. **Handling Imbalance**: Oversampling dengan teknik **SMOTE**.
5. **Split Data**: Data dibagi 80% train dan 20% test.

---

## 🤖 Algoritma yang Digunakan

Tiga algoritma supervised learning digunakan dan dibandingkan performanya:

- **Logistic Regression**
- **Random Forest**
- **K-Nearest Neighbors (KNN)**

---

## 📈 Evaluasi & Hasil

Evaluasi dilakukan menggunakan:
- **Akurasi**
- **Precision**
- **Recall**
- **F1-Score**

| Model              | Akurasi | F1-Score |
|--------------------|---------|----------|
| Logistic Regression| 76.11%  | 0.75     |
| KNN                | 78.89%  | 0.81     |
| Random Forest      | **91.11%** | **0.91** |

📌 *Random Forest menunjukkan performa terbaik, diikuti oleh KNN dan Logistic Regression.*

---

## ▶️ Cara Menjalankan

> 💡 **Note**: Notebook ini menggunakan Python dan library `sklearn`, `pandas`, `numpy`, `seaborn`, `matplotlib`, dan `imblearn`.

### 1. Jalankan di Google Colab (direkomendasikan)

Klik tombol berikut untuk membuka notebook di Colab:  
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/)

### 2. Jalankan secara lokal

```bash
git clone https://github.com/nekowawolf/tugas-besar-datamining-kelompok2.git
cd tugas-besar-datamining-kelompok2
pip install -r requirements.txt  # Buat file requirements.txt jika diperlukan
python main.py  # atau jalankan file notebook dengan Jupyter
