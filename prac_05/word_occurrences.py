"""
CP1404/CP5632 Practical - Suggested Solution
Count word occurrences in a string
This example is in the lecture notes 3 different ways
"""

word_to_count = {}
sentence = input("Sentence: ")
words = sentence.split()
for word in words:
    frequency = word_to_count.get(word, 0)
    word_to_count[word] = frequency + 1
words = list(word_to_count.keys())
words.sort()
max_length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_length, word_to_count[word]))