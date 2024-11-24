"""Module for converting digits to words."""

from enum import Enum
import requests
from aksharamukha import transliterate

from .components import Components
from .sandhi import Sandhi
from .languages import LANGUAGES


class Style(Enum):
    """Style of the number."""

    UTTARA = 1
    ADHIKA = 2


class Converter:
    """Class for converting digits to words."""

    @staticmethod
    def contains_english_alphabet(string: str):
        """Check if the string contains English alphabet."""

        return any(
            char in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
            for char in string
        )

    @staticmethod
    def change_script(string: str, language: str) -> str:
        """Change script."""

        if Converter.contains_english_alphabet(string):
            transliterated = string
        else:
            transliterated = transliterate.process("autodetect", language, string)

        return transliterated

    @staticmethod
    def change_script_aoi(string: str, language: str) -> str:
        """Change script."""
        url = f"https://aksharamukha-plugin.appspot.com/api/public?target={language}&text={string}"
        response = requests.get(url, timeout=5)

        response = response._content.decode("utf-8")  # pylint: disable=protected-access

        if response == string and language != "Devanagari":
            raise ValueError("Invalid script.")

        return response

    @staticmethod
    def string_to_int(num: str) -> int:
        """Convert string to integer."""
        return int(num)

    @staticmethod
    def is_small(num: int) -> bool:
        """Check if the number is small."""
        return 0 <= num <= 99

    @staticmethod
    def get_large(num: int) -> str:
        """Get large."""

        string = str(num)
        length = len(string)
        if length < 3:
            raise ValueError("The number is too small.")

        check_string = string[1:]
        if set(check_string) != {"0"}:
            raise ValueError("Number is not a multiple of 100.")

        base = Components().get_large(length - 1)

        if string[0] == "1":
            return base

        prefix = Components().get_two_digit(int(string[0]))

        return f"{prefix}-{base}"

    @staticmethod
    def get_small(num: int) -> str:
        """Get small."""
        if not Converter.is_small(num):
            raise ValueError("The number is too large.")

        return Components().get_two_digit(num)

    @staticmethod
    def get_word(num: int, script: str, style: Style = Style.ADHIKA) -> str:
        """Get word."""

        if num == 0:
            string = "शून्यः । शून्या । शून्यम्"

        elif num == 1:
            string = "एकः । एका । एकम्"

        elif num == 2:
            string = "द्वौ । द्वे । द्वे"

        elif num == 3:
            string = "त्रयः । तिस्रः । त्रीणि"

        elif num == 4:
            string = "चत्वारः । चतस्रः । चत्वारि"

        elif num < 19:
            string = Converter.get_small(num)

        elif Converter.is_small(num):
            string = Sandhi().sandhi(Converter.get_small(num))

        else:
            small_part = num % 100
            if small_part > 0:
                string = Converter.get_small(small_part)
            else:
                string = ""

            residue = num - small_part

            parts = [int(str(x)) for x in str(residue)]

            parts = parts[::-1]

            for index, part in enumerate(parts):
                if part == 0:
                    continue

                large_part = part * 10**index
                if string == "":
                    string = Converter.get_large(large_part)
                else:
                    string = f"{string}+{Converter.get_large(large_part)}"

            if style == Style.UTTARA:
                string = string.replace("+", "-उत्तर-")
            elif style == Style.ADHIKA:
                string = string.replace("+", "-अधिक-")

            string = Sandhi().sandhi(string)

        string = Converter.change_script(string, script)

        return string


if __name__ == "__main__":
    print(Converter().get_large(10000))
    print(Converter().get_small(54))

    for lang in LANGUAGES:
        # print(language)
        # print()
        try:
            Converter().get_word(10000, lang)
        except ValueError:
            print(lang)
