# -*- coding:utf8 -*-
# !/usr/bin/env python

"""
テキストを変換するファンクションを格納
"""

def to_romaji(text):
    """
    TODO:docstring here
    """
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
    """
    TODO:docstring here
    """
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
    """
    TODO:docstring here
    """
    from pykakasi import kakasi
    kakasi = kakasi()
    kakasi.setMode('K', 'K')
    kakasi.setMode('H', 'K')
    kakasi.setMode('E', 'K')
    kakasi.setMode('J', 'K')
    kakasi.setMode('a', 'K')
    converter = kakasi.getConverter()
    return converter.do(text.decode('utf-8'))