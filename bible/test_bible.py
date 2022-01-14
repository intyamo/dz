from bible import most_freq_bible_words


def test_10_words():
    most_freq_words = [
        "the",
        "and",
        "of",
        "to",
        "that",
        "in",
        "he",
        "shall",
        "unto",
        "for",
    ]

    assert most_freq_bible_words(10) == most_freq_words
