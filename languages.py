"""List of languages supported by the font."""

LANGUAGES = """
Ahom
Ariyaka
Assamese
Avestan
Balinese
Bengali
Bhaiksuki
Brahmi
Buginese
Buhid
Burmese
Chakma
Cham
Devanagari
Dogra
Grantha
Gujarati
Gurmukhi
Hanunoo
Hebrew
HK
IAST
IPA
ITRANS
Javanese
Kaithi
Kannada
Kawi
Kharoshthi
Khmer
Khojki
Khudawadi
Lao
Lepcha
Limbu
Mahajani
Makasar
Malayalam
Marchen
Modi
Mon
Mongolian
Mro
Multani
Nandinagari
Newa
Oriya
Pallava
PhagsPa
Rejang
RomanColloquial
Santali
Saurashtra
Shahmukhi
Shan
Sharada
Siddham
Sinhala
Soyombo
Sundanese
Tagalog
Tagbanwa
Takri
Tamil
Telugu
Thaana
Thai
Tibetan
Tirhuta
Urdu
Vatteluttu
Wancho
"""

LANGUAGES = [x.strip() for x in LANGUAGES.split("\n") if x.strip() != ""]
