from flask import Flask
from histogram import histogram
# from sample import weighted_sample


app = Flask(__name__)

@app.route('/')
def generate_words():
    my_file = open("./book.txt", "r")
    lines = my_file.readlines()
    my_histogram = histogram(lines)

    # word = weighted_sample(histogram)

if __name__ == '__main__':
    app.run(debug=True)
