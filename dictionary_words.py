"""read in the words file/ select random words from the file and store them in a data type/ number of words requested together into a sentence"""
import random
import sys

work_file = []
# looping through all the words and stipping them to get a space
f = open("/usr/share/dict/words", "r")
for line in f:
    work_file.append(line.strip())

def random_sentence(words, length):
    random_sentence = " "

    for _ in range(length):
        random_list = random.randint(0, len(words) - 1)
        random_sentence += " " + words[random_list]   
        words.remove(words[random_list])
    print(random_sentence)

if __name__ == "__main__":
    parameters = sys.argv[1:]
    number_words = int(parameters[0])
    if number_words < 2:
        print("You need more words to make a sentence")
    elif number_words == None:
        print("Enter something")
    else:
        random_sentence(work_file, number_words)
