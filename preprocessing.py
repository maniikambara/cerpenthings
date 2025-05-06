import os
import re
import json
import pandas as pd
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from kamus import load_kbbi, load_stopwords

# Inisialisasi stemmer
factory = StemmerFactory()
stemmer = factory.create_stemmer()

# Muat kamus dan stopwords
stopwords = load_stopwords()
kbbi_words = load_kbbi()

# Muat kamus alay (colloquial Indonesian lexicon)
alay_file = os.path.join(os.path.dirname(__file__), 'colloquial-indonesian-lexicon.txt')
try:
    with open(alay_file, 'r', encoding='utf-8') as f:
        alay_dict_raw = json.load(f)
    # Pastikan kunci dan nilai dalam lowercase
    alay_dict = {k.lower(): v.lower() for k, v in alay_dict_raw.items()}
except Exception as e:
    print(f"[Error] Gagal memuat kamus alay: {e}")
    alay_dict = {}

def preprocess_text(text):
    # Case folding
    text = text.lower()
    # Hapus angka
    text = re.sub(r"\d+", "", text)
    # Hapus karakter non-word kecuali spasi
    text = re.sub(r"[^\w\s]", " ", text)
    # Tokenisasi
    tokens = text.split()
    # Normalisasi alay: ganti token jika ada di kamus
    normalized = []
    for token in tokens:
        if token in alay_dict:
            normalized.append(alay_dict[token])
        else:
            normalized.append(token)
    # Filtering stopwords
    filtered = [word for word in normalized if word not in stopwords]
    # Stemming
    stemmed = [stemmer.stem(word) for word in filtered]
    # Filtering berdasarkan kamus KBBI
    valid = [word for word in stemmed if word in kbbi_words]
    # Gabung kembali menjadi string
    return ' '.join(valid)


def process_cerpen_files():
    data = []
    # Direktori berisi file .txt cerpen
    base_dir = os.path.dirname(__file__)
    cerpen_dir = os.path.join(base_dir, 'cerpen')

    for filename in os.listdir(cerpen_dir):
        if not filename.lower().endswith('.txt'):
            continue
        path = os.path.join(cerpen_dir, filename)
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Ekstrak judul
        judul_match = re.search(r'Judul\s*:\s*(.+)', content)
        judul = judul_match.group(1).strip() if judul_match else ''
        # Ekstrak kategori
        kategori_match = re.search(r'Kategori\s*:\s*(.+)', content)
        kategori = kategori_match.group(1).strip() if kategori_match else ''
        # Ekstrak isi setelah label 'Isi :' hingga akhir
        isi_match = re.search(r'Isi\s*:\s*([\s\S]+)$', content)
        teks_raw = isi_match.group(1).strip() if isi_match else ''

        # Preprocessing teks
        teks_clean = preprocess_text(teks_raw)
        data.append({
            'judul': judul,
            'kategori': kategori,
            'teks': teks_clean,
            'file_name': filename
        })

    # Simpan ke CSV
    df = pd.DataFrame(data)
    output_csv = os.path.join(base_dir, 'cerpen_preprocessed.csv')
    df.to_csv(output_csv, index=False, encoding='utf-8')
    print(f"Preprocessing selesai. Data tersimpan di {output_csv}")

if __name__ == '__main__':
    process_cerpen_files()