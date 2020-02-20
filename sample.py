import random
from histogram import open_file, histogram, frequency


def words_in_total(histogram):
    total = 0
    for value in histogram.values():
        total += value
    return total

    # total number of words in the file(values)


histogram = (histogram(open_file('book.txt')))

total_words = words_in_total(histogram)
# print(total_words)

def stochastic(dict, total_words):  #ask cao why dic
    random_number = random.randint(1, total_words)
    total_value = 0
    for word, value in dict.items():
        if random_number - value - total_value <= 0:
            return word
        else:
            total_value += value


# when you run this for loop, it prints one random word of test.txt 1000 times
# for i in range(1000):
#     print(stochastic(histogram, total_words))
