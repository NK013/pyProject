from operator import methodcaller

words = ["house", "apple", "car", "abort", "stop"]
a_words = filter(methodcaller("startswith", "a"), words)

for word in a_words:
    print(word)
