import re
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

INPUT_PATH = Path("tests/data_13/input.txt")

WORD_PATTERN = re.compile(r"[A-Za-zА-Яа-яЁё]+(?:'[A-Za-z]+)?", re.UNICODE)
FNV_OFFSET_BASIS_32, FNV_PRIME_32, MASK_32 = 2166136261, 16777619, 0xFFFFFFFF


def fnv1a_hash_32(text: str):
    hv = FNV_OFFSET_BASIS_32
    for b in text.encode("utf-8"):
        hv = ((hv ^ b) * FNV_PRIME_32) & MASK_32
    return hv


def is_prime(number: int):
    if number < 2:
        return False
    if number % 2 == 0:
        return number == 2
    div = 3
    while div * div <= number:
        if number % div == 0:
            return False
        div += 2
    return True


def next_prime(number: int):
    cand = max(3, number)
    if cand % 2 == 0:
        cand += 1
    while not is_prime(cand):
        cand += 2
    return cand


def extract_words(text: str):
    return [w.lower() for w in WORD_PATTERN.findall(text)]


@dataclass
class TableEntry:
    key: str
    count: int


class OpenAddressingHashTable:
    def __init__(self, capacity: int):
        self.capacity = max(3, capacity)
        self.slots: list[Optional[TableEntry]] = [None] * self.capacity
        self.unique_keys = 0

    def _index(self, key: str):
        return fnv1a_hash_32(key) % self.capacity

    def _need_resize(self):
        return (self.unique_keys + 1) / self.capacity > 0.65

    def _resize(self):
        old = self.slots
        self.capacity = next_prime(self.capacity * 2 + 1)
        self.slots = [None] * self.capacity
        self.unique_keys = 0
        for entry in old:
            if entry:
                self.add(entry.key, entry.count)

    def add(self, key: str, delta: int = 1):
        if self._need_resize():
            self._resize()
        i = self._index(key)
        while True:
            entry = self.slots[i]
            if entry is None:
                self.slots[i] = TableEntry(key, delta)
                self.unique_keys += 1
                return
            if entry.key == key:
                entry.count += delta
                return
            i = (i + 1) % self.capacity


def format_table(hash_table: OpenAddressingHashTable):
    lines = ["index:key=count"]
    lines += [f"{i}:{e.key}={e.count}" for i, e in enumerate(hash_table.slots) if e]
    return "\n".join(lines) + "\n"


def main():
    text = INPUT_PATH.read_text(encoding="utf-8", errors="replace")
    words = extract_words(text)
    capacity = next_prime(max(1, len(set(words))) * 2 + 1)

    hash_table = OpenAddressingHashTable(capacity)
    for w in words:
        hash_table.add(w)

    output_path = INPUT_PATH.parent / f"output.txt"
    output_path.write_text(format_table(hash_table), encoding="utf-8")


if __name__ == "__main__":
    main()


# 32-bit:
# Offset basis: 2166136261
# FNV prime: 16777619
