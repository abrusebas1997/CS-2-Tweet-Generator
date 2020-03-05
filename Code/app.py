from flask import Flask, render_template, request, url_for
import random
from histogram import open_file, histogram, frequency
from sample import stochastic, words_in_total
from markov_chain_order import Markov

app = Flask(__name__)

text_title = "Dr. Jekyll and Mr. Hyde, The Story of the Door"
file_content = open_file("book.txt")
markov_chain = Markov(file_content, 2)


@app.route('/')
def index():

    num = request.args.get('length')

    if num:
        sentence = markov_chain.get_sentence(int(num))
        return render_template("base.html", word=sentence, title=text_title)
    else:
        sentence = markov_chain.get_sentence(10)
        return render_template("base.html", word=sentence, title=text_title)


if __name__ == '__main__':
    app.run(debug=True)
