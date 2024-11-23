import re

text = input('Введите текст: ')
text = text.lower()

# punctuation = ['.', ',', '!', '?']
# for symb in punctuation:
#     text = text.replace(symb, '')
text = re.sub(r'[^\w\s]', '', text)

words = text.split()

word_frequency = {}

print('Количество разных слов:', len(set(words)))
print('Частота слов: ')

for word in words:
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1

for word, frequency in word_frequency.items():
    print(f'{word}: {frequency}')




