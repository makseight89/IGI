class WordAnalyzer:
    def __init__(self, text: str):
        self.text = text
        self.words = text.split()

    def count_max_len_words(self) -> int:
        word_lengths = [len(word) for word in self.words]
        max_length = max(word_lengths)
        return sum(1 for length in word_lengths if length == max_length)

    def find_words_with_punctuation(self) -> list[str]:
        return [word for word in self.words if word[-1] in ['.', ',']]

    def find_longest_word_with_e(self) -> list[str]:
        words_with_e = [word for word in self.words if word.endswith('e')]
        max_length = max(len(word) for word in words_with_e)
        return [word for word in words_with_e if len(word) == max_length]


def Task4():
    test_str = ("So she was considering in her own mind, as well as she could, for the hot day made her feel very "
                "sleepy and stupid, whether the pleasure of making a daisy-chain would be worth the trouble of "
                "getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her.")
    analyzer = WordAnalyzer(test_str)

    max_len_count = analyzer.count_max_len_words()
    print(f"Number of words with maximum length: {max_len_count}")

    words_with_punctuation = analyzer.find_words_with_punctuation()
    print(f"Words ending with '.' or ',': {', '.join(words_with_punctuation)}")

    longest_word_with_e = analyzer.find_longest_word_with_e()
    print(f"Longest word ending with 'e': {', '.join(longest_word_with_e)}")

    return
