from __future__ import annotations

from collections import Counter


def max_word_length(text: str) -> int:
    """Returns the length of the longest word in the input text."""
    words = text.split()
    return max(len(word) for word in words)


def min_word_length(text: str) -> int:
    """Returns the length of the shortest word in the input text."""
    words = text.split()
    return min(len(word) for word in words)


def average_word_length(text: str) -> float:
    """Returns the average word length in the input text."""
    words = text.split()
    total_length = sum(len(word) for word in words)
    return total_length / len(words)


def word_count(texts: list[str]) -> dict[str, int]:
    """Returns the count of each word in the input texts."""
    word_counter = Counter()
    for text in texts:
        word_counter.update(text.split())
    return word_counter


def find_longest_word(texts: list[str]) -> str:
    """Returns the longest word in the input texts."""
    longest_word = ""
    for text in texts:
        for word in text.split():
            if len(word) > len(longest_word):
                longest_word = word
    return len(longest_word)
