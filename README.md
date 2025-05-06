CerpenScraper & Kategori Analisis: Web Scraping, Preprocessing Teks, dan Klasifikasi Genre Cerpen
📚 CerpenScraper & Kategori Analisis
Sebuah proyek Python untuk melakukan web scraping cerpen dari cerpenmu.com, dilanjutkan dengan preprocessing teks dan analisis kategori/genre menggunakan TF-IDF dan cosine similarity.

🔍 Ringkasan Proyek
Proyek ini bertujuan untuk:

Mengambil cerpen dari situs web secara otomatis (web scraping).

Membersihkan dan memproses teks cerpen (preprocessing: case folding, tokenisasi, normalisasi, dll).

Menganalisis dan mengklasifikasikan cerpen ke dalam kategori/genre berdasarkan kata kunci dan kemiripan semantik.

Fitur Utama:
1. Scraping Cerpen:
Ekstrak judul, kategori, dan isi cerpen dari situs target.

2. Preprocessing Teks:
Case folding (penyatuan format huruf).

Pembersihan karakter spesial dan angka.

Tokenisasi & normalisasi kata tidak baku (colloquial words).

Stopword removal, stemming, dan filtering berdasarkan KBBI.

3. Analisis Kategori:
Klasifikasi genre menggunakan pencocokan kata kunci.

Klasifikasi berbasis TF-IDF dan cosine similarity.

Ekspor hasil ke CSV untuk analisis lebih lanjut.

🛠️ Instalasi
Prasyarat
Python 3.10+

Library yang diperlukan:
bash
Salin
Edit
pip install requests beautifulsoup4 pandas sastrawi scikit-learn
Langkah-Langkah Instalasi:
Clone repositori:

bash
Salin
Edit
git clone https://github.com/[username]/cerpen-scraper-analysis.git
cd cerpen-scraper-analysis
Siapkan file kamus eksternal:

Unduh stopwords-id.txt, kbbi.txt, dan colloquial-indonesian-lexicon.txt.

Simpan file-file tersebut di direktori utama proyek.

🚀 Cara Penggunaan
1. Jalankan Web Scraping (Mengumpulkan cerpen):
bash
Salin
Edit
python scraping_web.py
Hasil disimpan di folder cerpen/.

2. Preprocessing Teks:
bash
Salin
Edit
python preprocessing.py
Hasil preprocessing disimpan di cerpen_preprocessed.csv.

3. Analisis Kategori:
bash
Salin
Edit
python analisis.py
Hasil analisis disimpan di hasil_analisis_tfidf.csv dan cosine_similarity_matrix.csv.

📂 Struktur Proyek
python
Salin
Edit
cerpen-scraper-analysis/
├── cerpen/                   # Folder hasil scraping cerpen
├── scraping_web.py           # Script scraping web
├── preprocessing.py          # Script preprocessing teks
├── analisis.py               # Script analisis kategori
├── kamus.py                  # Load kamus (stopwords, KBBI, dll)
├── kbbi.txt                  # Kamus KBBI
├── stopwords-id.txt          # Daftar stopwords Bahasa Indonesia
├── colloquial-indonesian-lexicon.txt  # Kamus kata tidak baku
├── cerpen_preprocessed.csv   # Data teks setelah preprocessing
└── hasil_analisis_tfidf.csv  # Hasil klasifikasi kategori
📊 Metode Analisis
1. Klasifikasi Berbasis Kata Kunci:
Setiap kategori memiliki daftar kata kunci (misalnya, "horor" → "hantu", "kuburan").

Hitung kemunculan kata kunci dalam teks untuk menentukan kategori.

2. Klasifikasi dengan TF-IDF & Cosine Similarity:
Transformasi teks ke vektor TF-IDF.

Hitung kemiripan dengan vektor referensi kategori menggunakan cosine similarity.

📌 Sumber Data
Daftar Stopwords: stopwords-id

Stemmer Bahasa Indonesia: Sastrawi

Kamus Kata Tidak Baku: colloquial-indonesian-lexicon

Kamus KBBI: kumpulan-kata-bahasa-indonesia-KBBI

📜 Lisensi
Proyek ini dilisensikan di bawah MIT License.

🖥️ Contoh Hasil
File hasil_analisis_tfidf.csv:
Judul	Kategori_Original	Kategori_Keyword	Kategori_Cosine	Kata_Kunci_Penting
"Sebuah Misteri..."	Misteri	misteri	misteri	pembunuhan, detektif

Catatan:
Proyek ini mengandalkan metode web scraping untuk mengekstrak cerpen dari situs web, kemudian melakukan preprocessing untuk menghilangkan noise dalam teks. Setelah itu, cerpen diklasifikasikan ke dalam genre yang relevan menggunakan teknik TF-IDF dan cosine similarity. Semua data hasil analisis dapat diekspor ke dalam format CSV untuk keperluan analisis lebih lanjut.
