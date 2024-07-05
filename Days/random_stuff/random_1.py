word = input("Enter a word! ").strip()
print(f'wordlength is {len(word)}')

sentence = input("Enter a sentence! ").strip().split()
word_count = 0
char_count = 0

for word in sentence:
    word_count += 1
    char_count += len(word)

print(f'{word_count} words')
print(f'{char_count} chars') 