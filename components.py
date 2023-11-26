"""Module for components of the number."""

import os
from dataclasses import dataclass, field


@dataclass
class Components:
    """Class for components of the number."""

    source_two_digit: os.PathLike = "data/two_digit.csv"
    source_large: os.PathLike = "data/large.csv"

    two_digit: dict[int, str] = field(default_factory=dict, init=False)
    large: dict[int, str] = field(default_factory=dict, init=False)

    def __post_init__(self):
        """Post init."""
        self.two_digit = self._load_data(self.source_two_digit)
        self.large = self._load_data(self.source_large)

    def _load_data(self, source: os.PathLike) -> dict[int, str]:
        """Load data from csv file."""
        data = {}
        with open(source, "r", encoding="utf-8") as f:
            for line in f:
                num, word = line.strip().split(",")
                data[int(num)] = word
        return data

    def get_two_digit(self, num: int) -> str:
        """Get two digit."""
        return self.two_digit.get(num)

    def get_large(self, num: int) -> str:
        """Get large."""
        return self.large.get(num)
