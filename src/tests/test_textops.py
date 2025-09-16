import pytest
from src.textops import unique_words_preserve_order, top_k_frequent_first_tie, redact_words


@pytest.mark.parametrize(
    "words, expected",
    [
        (["a", "b", "a", "c", "b"], ["a", "b", "c"]),
        ([], []),
        (["x", "x", "x"], ["x"]),
        (["m", "n", "o"], ["m", "n", "o"]),
    ]
)
def test_unique_words_preserve_order(words, expected):
    assert unique_words_preserve_order(words) == expected


def test_top_k_frequent_first_tie_normal_case():
    words = ["x", "y", "x", "z", "y", "y", "x"]
    # counts: x=3, y=3, z=1; tie broken by first appearance (x before y)
    assert top_k_frequent_first_tie(words, 2) == ["x", "y"]


def test_top_k_frequent_first_tie_errors():
    words = ["a", "b", "a"]

    # k=0 → invalid
    with pytest.raises(ValueError):
        top_k_frequent_first_tie(words, 0)

    # k larger than unique count should still work
    assert top_k_frequent_first_tie(words, 10) == ["a", "b"]


@pytest.mark.parametrize(
    "words, redacts, expected",
    [
        (["alice", "bob", "alice", "carol"], ["alice"], ["***", "bob", "***", "carol"]),
        (["alice", "bob", "carol"], ["bob", "carol"], ["alice", "***", "***"]),
        (["x", "y", "z"], [], ["x", "y", "z"]),  # nothing redacted
        ([], ["anything"], []),  # empty input
    ]
)
def test_redact_words(words, redacts, expected):
    assert redact_words(words, redacts) == expected
