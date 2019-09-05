words = {}

string = input("Text:")
splitted_string = string.split()

for word in splitted_string:
    if word in words:
        words[word] += 1
    else:
        words[word] = 1

print(words)

sorted_words = list(words.keys())

max_word = 0

for word in sorted_words:
    if len(word) > max_word:
        word = max_word
    print("{:{}}  {}".format(word, max_word, words[word]))


print(sorted_words)
