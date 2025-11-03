def count_words(sentence: str) -> dict:
    word_count_dictionary: dict = {}
    words: list[str] = sentence.lower().split()

    for word in words:
        if word in word_count_dictionary:
            word_count_dictionary[word] += 1
        else:
            word_count_dictionary[word] = 1

    return word_count_dictionary


user_sentence = input("Enter a sentence: ")
word_occurrences = count_words(user_sentence)

print(f"Word occurrences: {word_occurrences}")
