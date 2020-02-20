from flask import Flask
from histogram import histogram, histogram, frequency
from sample import stochastic, words_in_total


app = Flask(__name__)

@app.route('/')
def generate_words():
    my_file = open("./book.txt", "r")
    lines = my_file.readlines()
    my_histogram = histogram(lines)
    print(my_histogram)

    sentence = ""
    num_words = 10
    for i in range(num_words):
        word = stochastic(my_histogram, words_in_total)
        sentence += " " + str(word)

    return sentence


    # word = weighted_sample(histogram)

if __name__ == '__main__':
    app.run(debug=True)
