import csv
import random
from dataclasses import dataclass
from typing import List


@dataclass
class WordPair:
    nl: str
    en: str


def read_words() -> List[WordPair]:
    with open('dutch_words.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        return [WordPair(row['NL'].strip(), row['EN'].strip()) for row in reader]


def display_word(word: str, solution: str, lang: str, counter: int, total: int):
    print(f"--- {counter}/{total} ({lang}) ---")
    input(f"{word}")
    print(f"{solution}")


if __name__ == '__main__':
    words = read_words()
    random.shuffle(words)
    counter = 1
    total = len(words)
    for word in words:
        if random.choice([True, False]):
            display_word(word.en, word.nl, 'EN', counter, total)
        else:
            display_word(word.nl, word.en, 'NL', counter, total)
        counter += 1
