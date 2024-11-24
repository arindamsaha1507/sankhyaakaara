"""Module for doing sandhi."""

import os
from dataclasses import dataclass, field
from akshara import varnakaarya as vk


@dataclass
class Sandhi:
    """Class for doing sandhi."""

    source: os.PathLike = "data/sandhi.csv"
    rules: dict[str, list[str]] = field(init=False)

    def __post_init__(self):
        data = {}
        with open(self.source, "r", encoding="utf-8") as f:
            for line in f:
                left, right, result = line.strip().split(",")

                inp = f"{left} {right}"
                out = vk.get_vinyaasa(result)
                data[inp] = out

        self.rules = data

    @staticmethod
    def preprocess(string: str) -> str:
        """Preprocess."""
        return string.replace("-", " ")

    def sandhi(self, string: str) -> str:
        """Sandhi."""
        string = self.preprocess(string)

        vinyaasa = vk.get_vinyaasa(string)

        for index, letter in enumerate(vinyaasa):
            if letter != " ":
                continue

            part = vk.get_shabda(vinyaasa[index - 1 : index + 2])

            # print(part)

            if part in self.rules.keys():
                part = self.rules[part]
                # print(part)
                vinyaasa[index - 1 : index + 2] = part
                # print(vinyaasa)

        if vinyaasa[-1] == "अ":
            vinyaasa.append("म्")
        elif vinyaasa[-1] in ["इ", "उ"]:
            vinyaasa.append("ः")

        ret = vk.get_shabda(vinyaasa)
        ret = ret.replace(" ", "")

        return ret


if __name__ == "__main__":
    sandhi = Sandhi()

    print(sandhi.sandhi("अग्निः अग्निः"))
    print(sandhi.sandhi("अग्नि अग्निः"))
