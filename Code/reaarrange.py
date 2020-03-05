import random
import sys

def rearrange(sentence):
    words = sentence.split(" ")
    random_sentence = []

    while len(words) > 0:
        for _ in range(len(words)):
            random_list = random.randint(0, len(words) - 1)
            random_sentence.append(words[random_list])
            words.remove(words[random_list])



if __name__=="__main__":
    sentence = " ".join(sys.argv[1:])
    rearrange(sentence)
