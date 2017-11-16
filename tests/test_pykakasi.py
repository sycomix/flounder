# # -*- coding: utf-8 -*-

def to_romaji(text):
    from pykakasi import kakasi
    kakasi = kakasi()
    kakasi.setMode('H', 'a')
    kakasi.setMode('K', 'a')
    kakasi.setMode('J', 'a')
    kakasi.setMode('a', 'a')
    converter = kakasi.getConverter()
    print(converter.do(text.decode('utf-8')))

def to_hiragana(text):
    from pykakasi import kakasi
    kakasi = kakasi()
    kakasi.setMode('J', 'H')
    kakasi.setMode('K', 'H')
    kakasi.setMode('H', 'H')
    kakasi.setMode('a', 'H')
    converter = kakasi.getConverter()
    print(converter.do(text.decode('utf-8')))

def to_katakana(text):
    from pykakasi import kakasi
    kakasi = kakasi()
    kakasi.setMode('J', 'K')
    kakasi.setMode('H', 'K')
    kakasi.setMode('K', 'K')
    kakasi.setMode('a', 'K')
    converter = kakasi.getConverter()
    print(converter.do(text.decode('utf-8')))

if __name__ == '__main__':
    to_romaji('')
    to_hiragana('')
    to_katakana('')