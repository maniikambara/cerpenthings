# CerpenScraper & Kategori Analisis: Web Scraping, Preprocessing Teks, dan Klasifikasi Genre Cerpen

📚 **CerpenScraper & Kategori Analisis**  
Sebuah proyek Python untuk melakukan web scraping cerpen dari cerpenmu.com, dilanjutkan dengan preprocessing teks dan analisis kategori/genre menggunakan TF-IDF dan cosine similarity.

## 🔍 Ringkasan Proyek
Proyek ini bertujuan untuk:

1. **Mengambil cerpen** dari situs web secara otomatis (web scraping).
2. **Membersihkan dan memproses teks cerpen** (preprocessing: case folding, tokenisasi, normalisasi, dll).
3. **Menganalisis dan mengklasifikasikan cerpen** ke dalam kategori/genre berdasarkan kata kunci dan kemiripan semantik.

### Fitur Utama:
#### 1. **Scraping Cerpen**:
   - Ekstrak **judul**, **kategori**, dan **isi cerpen** dari situs target.

#### 2. **Preprocessing Teks**:
   - **Case folding** (penyatuan format huruf).
   - Pembersihan **karakter spesial** dan **angka**.
   - **Tokenisasi** & normalisasi kata tidak baku (colloquial words).
   - **Stopword removal**, **stemming**, dan **filtering berdasarkan KBBI**.

#### 3. **Analisis Kategori**:
   - Klasifikasi genre menggunakan **pencocokan kata kunci**.
   - Klasifikasi berbasis **TF-IDF** dan **cosine similarity**.
   - Ekspor hasil ke **CSV** untuk analisis lebih lanjut.

---

## 🛠️ Instalasi

### Prasyarat
- Python 3.10+

### Library yang diperlukan:
```bash
pip install requests beautifulsoup4 pandas sastrawi scikit-learn
