"""
Word Occurrences
Estimate: 20 minutes
Actual: 52 minutes
"""

word_to_count = {}

text = input("Text: ").split()
for word in text:
    word_to_count[word] = word_to_count.get(word, 0) + 1

for word in sorted(word_to_count):
    width, number_of_words = 10, word_to_count[word]
    print(f"{word:{width}} = {number_of_words}")

