# # -*- coding: utf-8 -*-
import csv

def to_romaji(text):
    from pykakasi import kakasi
    kakasi = kakasi()
    kakasi.setMode('a', 'a')
    kakasi.setMode('E', 'a')
    kakasi.setMode('K', 'a')
    kakasi.setMode('H', 'a')
    kakasi.setMode('J', 'a')
    converter = kakasi.getConverter()
    return converter.do(text.decode('utf-8'))


def to_hiragana(text):
    from pykakasi import kakasi
    kakasi = kakasi()
    kakasi.setMode('H', 'H')
    kakasi.setMode('E', 'H')
    kakasi.setMode('K', 'H')
    kakasi.setMode('J', 'H')
    kakasi.setMode('a', 'H')
    converter = kakasi.getConverter()
    return converter.do(text.decode('utf-8'))


def to_katakana(text):
    from pykakasi import kakasi
    kakasi = kakasi()
    kakasi.setMode('K', 'K')
    kakasi.setMode('H', 'K')
    kakasi.setMode('E', 'K')
    kakasi.setMode('J', 'K')
    kakasi.setMode('a', 'K')
    converter = kakasi.getConverter()
    return converter.do(text.decode('utf-8'))

def to_list(csv_path):
    tmp_list = []
    with open(csv_path, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            tmp_list.append(row[0])
        return tmp_list 

if __name__ == '__main__':
    entity = to_list('entity.csv')
    for synonym in entity:
        print synonym
        print to_romaji(synonym)
        print to_hiragana(synonym)
        print to_katakana(synonym)