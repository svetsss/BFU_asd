import re
from dataclasses import dataclass
from pathlib import Path

INPUT_PATH = Path("tests/data_14/input.txt")

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
class BucketEntry:
    key: str
    count: int


class ChainingHashTable:
    def __init__(self, bucket_count: int):
        self.bucket_count = max(3, bucket_count)
        self.buckets: list[list[BucketEntry]] = [[] for _ in range(self.bucket_count)]

    def add(self, key: str, delta: int = 1) -> None:
        i = fnv1a_hash_32(key) % self.bucket_count
        bucket = self.buckets[i]
        for entry in bucket:
            if entry.key == key:
                entry.count += delta
                return
        bucket.append(BucketEntry(key, delta))


def format_table(hash_table: ChainingHashTable):
    lines = ["index:key=count"]
    for i, bucket in enumerate(hash_table.buckets):
        for entry in bucket:
            lines.append(f"{i}:{entry.key}={entry.count}")
    return "\n".join(lines) + "\n"


def main():
    text = INPUT_PATH.read_text(encoding="utf-8", errors="replace")
    words = extract_words(text)

    bucket_count = next_prime(max(1, len(set(words))) + 1)
    hash_table = ChainingHashTable(bucket_count)

    for w in words:
        hash_table.add(w)

    output_path = INPUT_PATH.parent / f"output.txt"
    output_path.write_text(format_table(hash_table), encoding="utf-8")


if __name__ == "__main__":
    main()


# хеш-функция (FNV-1a, 32-bit)
# 1) Слово переводится в UTF-8 байты, для ру и англ.
# 2) Берётся стартовое число h = 2166136261.
# 3) Дальше по очереди берётся каждый байт:
#    - h “смешивается” с байтом через XOR
#    - потом умножается на специальное простое число 16777619
#    - и оставляется только 32-битный результат (mod 2^32)
# 4) В итоге получается большое число (хеш), а индекс в таблице берётся так: index = h % size.


