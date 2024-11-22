text = input('Введите текст: ')
text = text.lower()

punctuation = [".", ",", "!", "?"]
for symb in punctuation:
    text = text.replace(symb, '')

words = text.split()
print(words)

