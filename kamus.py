import re

def load_kbbi():
    with open('kbbi.txt', 'r', encoding='utf-8') as f:
        return set(word.strip().lower() for word in f if word.strip())

def load_stopwords():
    with open('stopwords-id.txt', 'r', encoding='utf-8') as f:
        return set(word.strip().lower() for word in f if word.strip())

def load_keywords():
    return {
        'realistik': [
            'sekolah', 'uang', 'masalah', 'konflik',
            'pernikahan', 'pendidikan', 'ekonomi',
            'transportasi', 'lingkungan', 'kemiskinan', 'pengangguran',
            'birokrasi', 'urbanisasi'
        ],
        'fantasi': [
            'sihir', 'naga', 'peri', 'gaib', 'kerajaan', 'dunia',
            'teleportasi', 'ilusi', 'khayal', 'mitos', 'ramuan',
            'kastil', 'penyihir', 'quest', 'artefak', 'dimensi',
            'portal', 'troll', 'drakon', 'orc'
        ],
        'romantis': [
            'cinta', 'cium', 'debar', 'asmara', 'rayuan',
            'janji', 'setia', 'cemburu', 'rindu', 'manja', 'mesra',
            'kerinduan', 'mawar', 'senandung'
        ],
        'misteri': [
            'pembunuhan', 'detektif', 'petunjuk', 'saksi', 'alibi',
            'forensik', 'rahasia', 'konspirasi', 'arsip', 'kode',
            'bisikan', 'jejak', 'tersangka', 'motif', 'labirin',
            'sketsa', 'sidikjari', 'autopsi', 'profiling', 'retina', 'bunuh'
        ],
        'horor': [
            'hantu', 'kuburan', 'teror', 'setan', 'roh', 'jeritan',
            'gelap', 'berdarah', 'kematian',
            'kutukan', 'angker', 'supranatural', 'penampakan',
            'poltergeist', 'kubur', 'neraka', 'neri', 'gore'
        ],
        'fabel': [
            'hewan', 'binatang', 'burung', 'serigala', 'kura', 'kelinci',
            'cerdik', 'rubah', 'gajah', 'semut', 'lebah', 'ratu', 'rusa', 'kancil'
        ]
    }