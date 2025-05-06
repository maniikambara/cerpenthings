import pandas as pd
import re
import sys
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from kamus import load_keywords

keywords = load_keywords()

def load_data():
    """Membaca dan memvalidasi data"""
    try:
        df = pd.read_csv('cerpen_preprocessed.csv', encoding='utf-8')
        required_columns = ['judul', 'kategori', 'teks', 'file_name']
        missing = set(required_columns) - set(df.columns)
        if missing:
            raise ValueError(f"Format CSV tidak valid. Kolom hilang: {', '.join(missing)}")
        return df
    except FileNotFoundError:
        print("ERROR: File cerpen_preprocessed.csv tidak ditemukan")
        sys.exit(1)

def label_genres(text):
    """Labeling genre berdasarkan keyword matching"""
    t = text.lower()
    scores = {g: 0 for g in keywords}
    for word in re.findall(r'\w+', t):
        for genre, terms in keywords.items():
            if any(term in word for term in terms):
                scores[genre] += 1
    valid = {g: s for g, s in scores.items() if s >= 3}
    if not valid:
        return 'lainnya'
    top2 = sorted(valid.items(), key=lambda x: x[1], reverse=True)[:2]
    if len(top2) > 1 and top2[0][1] == top2[1][1]:
        for g in keywords:
            if g in (top2[0][0], top2[1][0]):
                return g
    return top2[0][0]

def cosine_genre_classification(df, tfidf, tfidf_matrix, keywords):
    """Klasifikasi genre berdasarkan cosine similarity dengan dokumen keyword genre"""
    print("Mencocokkan genre berdasarkan cosine similarity dengan dokumen keyword genre …")
    genre_docs = [' '.join(terms) for terms in keywords.values()]
    genre_names = list(keywords.keys())
    genre_tfidf = tfidf.transform(genre_docs)
    cosine_scores = cosine_similarity(tfidf_matrix, genre_tfidf)
    genre_pred_cosine = [genre_names[row.argmax()] for row in cosine_scores]
    return genre_pred_cosine

def analyze_and_export():
    """Proses labeling, TF-IDF, dan ekspor CSV hasil analisis"""
    df = load_data()

    print("Memproses label Kategori_Keyword …")
    df['Kategori_Keyword'] = df['teks'].apply(label_genres)

    print("Menghitung TF-IDF …")
    tfidf = TfidfVectorizer(
        ngram_range=(1, 2),
        max_features=800,
        stop_words=None
    )
    tfidf_matrix = tfidf.fit_transform(df['teks'])
    feature_names = tfidf.get_feature_names_out()

    print("Menghitung cosine similarity antar teks …")
    cos_sim_matrix = cosine_similarity(tfidf_matrix)
    cos_sim_df = pd.DataFrame(cos_sim_matrix, index=df['judul'], columns=df['judul'])
    cos_sim_df.to_csv("cosine_similarity_matrix.csv", encoding='utf-8')

    # Kategori berdasarkan cosine similarity
    df['Kategori_Cosine'] = cosine_genre_classification(df, tfidf, tfidf_matrix, keywords)

    print("Mengekstrak kata kunci penting per dokumen …")
    arr = tfidf_matrix.toarray()
    top_keywords = []
    top_scores = []
    for row in arr:
        idx_desc = row.argsort()[-3:][::-1]
        kws = [feature_names[i] for i in idx_desc]
        scs = [row[i] for i in idx_desc]
        scs_fmt = [f"{s:.2f}" for s in scs]
        top_keywords.append(", ".join(kws))
        top_scores.append(", ".join(scs_fmt))

    result = pd.DataFrame({
        'Judul': df['judul'],
        'File': df['file_name'],
        'Kategori_Original': df['kategori'],
        'Kategori_Keyword': df['Kategori_Keyword'],
        'Kategori_Cosine': df['Kategori_Cosine'],
        'Kata_Kunci_Penting': top_keywords,
        'Skor_TFIDF': top_scores,
        'Panjang_Teks': df['teks'].str.split().str.len()
    })

    out_path = 'hasil_analisis_tfidf.csv'
    result.to_csv(out_path, index=False, encoding='utf-8')
    print(f"Hasil analisis berhasil disimpan di {out_path}")

if __name__ == '__main__':
    analyze_and_export()