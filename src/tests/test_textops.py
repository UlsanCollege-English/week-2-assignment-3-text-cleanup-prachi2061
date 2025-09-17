import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from textops import unique_words_preserve_order, top_k_frequent_first_tie, redact_words
import pytest


def test_unique_words_preserve_order():
    assert unique_words_preserve_order(["a", "b", "a", "c", "b"]) == ["a", "b", "c"]
    assert unique_words_preserve_order([]) == []
    assert unique_words_preserve_order(["x", "x", "x"]) == ["x"]
    assert unique_words_preserve_order(["one", "two", "three"]) == ["one", "two", "three"]


def test_top_k_frequent_first_tie():
    words = ["a", "b", "a", "c", "b", "b"]
    assert top_k_frequent_first_tie(words, 1) == ["b"]
    assert top_k_frequent_first_tie(words, 2) == ["b", "a"]
    assert top_k_frequent_first_tie(words, 3) == ["b", "a", "c"]
    assert top_k_frequent_first_tie(["x", "y", "z"], 2) == ["x", "y"]
    with pytest.raises(ValueError):
        top_k_frequent_first_tie(words, 0)
    with pytest.raises(ValueError):
        top_k_frequent_first_tie(words, -5)


def test_redact_words():
    words = ["apple", "banana", "cherry", "date"]
    redacts = ["banana", "date"]
    assert redact_words(words, redacts) == ["apple", "***", "cherry", "***"]
    assert redact_words(words, []) == ["apple", "banana", "cherry", "date"]
    assert redact_words([], ["anything"]) == []
    words2 = ["foo", "bar", "foo", "baz"]
    assert redact_words(words2, ["foo"]) == ["***", "bar", "***", "baz"]
