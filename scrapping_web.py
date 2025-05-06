import os
import requests
from bs4 import BeautifulSoup

BASE_LIST_URL = 'https://cerpenmu.com/cerpen-of-the-month'
OUTPUT_DIR = 'cerpen'
REQUEST_TIMEOUT = 10  # dalam detik

def get_soup(url):
    try:
        resp = requests.get(url, timeout=REQUEST_TIMEOUT)
        resp.raise_for_status()
        return BeautifulSoup(resp.text, 'html.parser')
    except requests.RequestException as e:
        print(f"[Error] Gagal mengambil {url}: {e}")
        return None

def scrape_list_of_cerpen():
    soup = get_soup(BASE_LIST_URL)
    if soup is None:
        return []
    cerpen = []
    for strong in soup.select('a[href*="/cerpen-"] > strong'):
        title = strong.get_text(strip=True)
        link = strong.parent.get('href', '')
        if not link:
            continue
        full_url = link if link.startswith('http') else 'https://cerpenmu.com' + link
        cerpen.append({'title': title, 'url': full_url})
    return cerpen

def clean_article_text(article_soup):
    # Hapus elemen yang tidak diinginkan
    for h1 in article_soup.find_all('h1'):
        h1.decompose()
    for p in article_soup.find_all('p'):
        if p.get_text(strip=True).startswith('Cerpen Karangan:'):
            p.decompose()
    # Ambil seluruh teks
    raw = article_soup.get_text(separator='\n')
    # Potong mulai setelah moderasi
    if 'Lolos moderasi pada:' in raw:
        raw = raw.split('Lolos moderasi pada:', 1)[1]
    # Hapus tagline iklan
    cleaned = raw.replace('ADVERTISEMENT', '')
    return cleaned.strip()

def extract_category(article_soup):
    cat_tag = article_soup.find('a', rel='category tag')
    return cat_tag.get_text(strip=True) if cat_tag else 'Unknown'

def scrape_and_export():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    cerpen_list = scrape_list_of_cerpen()
    for idx, item in enumerate(cerpen_list, start=1):
        title = item['title']
        url = item['url']
        print(f"({idx}) {title} — {url}")
        soup = get_soup(url)
        if soup is None:
            print("  [skip] Tidak dapat memuat halaman cerpen.")
            continue
        article = soup.find('article', class_='post')
        if not article:
            print("  [skip] Artikel tidak ditemukan.")
            continue
        category = extract_category(article)
        isi = clean_article_text(article)

        # Simpan ke file
        filename = os.path.join(OUTPUT_DIR, f'Cerpen {idx}.txt')
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"Judul : {title}\n")
            f.write(f"Kategori : {category}\n\n")
            f.write("Isi :\n")
            f.write(isi)
        print(f"  → Tersimpan: {filename}")

if __name__ == '__main__':
    scrape_and_export()