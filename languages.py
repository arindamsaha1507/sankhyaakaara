"""List of languages supported by the font."""

from enum import Enum

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


class LanguageEnum(str, Enum):
    """Enum for supported languages."""

    AHOM = "Ahom"
    ARIYAKA = "Ariyaka"
    ASSAMESE = "Assamese"
    AVESTAN = "Avestan"
    BALINESE = "Balinese"
    BENGALI = "Bengali"
    BHAIKSUKI = "Bhaiksuki"
    BRAHMI = "Brahmi"
    BUGINESE = "Buginese"
    BUHID = "Buhid"
    BURMESE = "Burmese"
    CHAKMA = "Chakma"
    CHAM = "Cham"
    DEVANAGARI = "Devanagari"
    DOGRA = "Dogra"
    GRANTHA = "Grantha"
    GUJARATI = "Gujarati"
    GURMUKHI = "Gurmukhi"
    HANUNOO = "Hanunoo"
    HEBREW = "Hebrew"
    HK = "HK"
    IAST = "IAST"
    IPA = "IPA"
    ITRANS = "ITRANS"
    JAVANESE = "Javanese"
    KAITHI = "Kaithi"
    KANNADA = "Kannada"
    KAWI = "Kawi"
    KHAROSHTHI = "Kharoshthi"
    KHMER = "Khmer"
    KHOJKI = "Khojki"
    KHUDAWADI = "Khudawadi"
    LAO = "Lao"
    LEPCHA = "Lepcha"
    LIMBU = "Limbu"
    MAHAJANI = "Mahajani"
    MAKASAR = "Makasar"
    MALAYALAM = "Malayalam"
    MARCHEN = "Marchen"
    MODI = "Modi"
    MON = "Mon"
    MONGOLIAN = "Mongolian"
    MRO = "Mro"
    MULTANI = "Multani"
    NANDINAGARI = "Nandinagari"
    NEWA = "Newa"
    ORIYA = "Oriya"
    PALLAVA = "Pallava"
    PHAGSPA = "PhagsPa"
    REJANG = "Rejang"
    ROMANCOLLOQUIAL = "RomanColloquial"
    SANTALI = "Santali"
    SAURASHTRA = "Saurashtra"
    SHAHMUKHI = "Shahmukhi"
    SHAN = "Shan"
    SHARADA = "Sharada"
    SIDDHAM = "Siddham"
    SINHALA = "Sinhala"
    SOYOMBO = "Soyombo"
    SUNDANESE = "Sundanese"
    TAGALOG = "Tagalog"
    TAGBANWA = "Tagbanwa"
    TAKRI = "Takri"
    TAMIL = "Tamil"
    TELUGU = "Telugu"
    THAANA = "Thaana"
    THAI = "Thai"
    TIBETAN = "Tibetan"
    TIRHUTA = "Tirhuta"
    URDU = "Urdu"
    VATTELUTTU = "Vatteluttu"
    WANCHO = "Wancho"
