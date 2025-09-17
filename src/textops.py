from collections import Counter
from typing import List


def unique_words_preserve_order(words: List[str]) -> List[str]:
    """Return a list of unique words in the order of their first appearance."""
    seen = set()
    result = []
    for word in words:
        if word not in seen:
            seen.add(word)
            result.append(word)
    return result


def top_k_frequent_first_tie(words: List[str], k: int) -> List[str]:
    """Return the top k frequent words; tie broken by first appearance."""
    if k <= 0:
        raise ValueError("k must be positive")

    # Count occurrences
    counts = Counter(words)
    # Preserve first appearance order for tie-breaking
    seen_order = {}
    for idx, word in enumerate(words):
        if word not in seen_order:
            seen_order[word] = idx

    # Sort by frequency descending, then first appearance
    sorted_words = sorted(
        counts.keys(),
        key=lambda w: (-counts[w], seen_order[w])
    )

    return sorted_words[:k]


def redact_words(words: List[str], redacts: List[str]) -> List[str]:
    """Replace any word in redacts with '***'."""
    redacts_set = set(redacts)
    return ["***" if w in redacts_set else w for w in words]
