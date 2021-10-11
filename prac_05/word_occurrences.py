"""Count word occurrences"""

word_list = {}
string = input("Enter string: ")
print(string)
words = string.split()
for word in words:
    occurrence = word_list.get(word, 0)
    word_list[word] = occurrence + 1

print_words = list(word_list.keys())
print_words.sort()

max_length = max((len(word) for word in print_words))
for word in print_words:
    print("{:{}} : {}".format(word, max_length, word_list[word]))
