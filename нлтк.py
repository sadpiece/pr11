import nltk
import matplotlib.pyplot as plt
from nltk.corpus import *
from nltk.probability import FreqDist
import string


print(gutenberg.fileids())

blake = nltk.corpus.gutenberg.words('blake-poems.txt')
print( "кількість слів у тексті: ", len(blake))

fdist = FreqDist(blake)
top_ten = fdist.most_common(10)
print("10 найбільш вживаних слів у тексті: ")
print(top_ten)

words = [item[0] for item in top_ten]
chastota = [item[1] for item in top_ten]


plt.figure(figsize=(12, 6))
plt.bar(words, chastota, color="blue")
plt.title('10 найбільш вживаних слів у тексті', fontsize=15)
plt.xlabel('Слова')
plt.ylabel('Частота')

stop_words = set(stopwords.words("english"))
without_stop_words = [word for word in blake if not word in stop_words]
print("текст без стоп слів: ")
print(without_stop_words)



fdist = FreqDist(without_stop_words)
top_ten = fdist.most_common(10)
print("10 найбільш вживаних слів у тексті без стоп слів: ")
print(top_ten)



table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in without_stop_words]
fdist = FreqDist(stripped)
top_ten = fdist.most_common(10)
print("10 найбільш вживаних слів у тексті без стоп слів та пунктуації: ")
print(top_ten)


words = [item[0] for item in top_ten]
chastota = [item[1] for item in top_ten]


plt.figure(figsize=(12, 6))
plt.bar(words, chastota, color="blue")
plt.title('10 найбільш вживаних слів у тексті без стоп слів та пунктуації', fontsize=15)
plt.xlabel('Слова')
plt.ylabel('Частота')

plt.show()


