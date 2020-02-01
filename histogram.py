import sys



def open_file():
    f_histogram = open("book.txt", "r")
    file_content = []

    for line in f_histogram:
        # split creates another list, if you use append, you will create a list of lists; but with extend you create just 1
        file_content.extend(line.split())
    return file_content

def histogram():
    """ take a filename or content_file as
     a string and return histogram data
     that stores words with the number of times the word appears"""
     histogram = {}
     for word in file_content:

         if word in histogram:
            histogram[word] += 1
         else:
            histogram[word] = 1
    return histogram

def unique_words(histogram):
    """returns the total count of unique words"""
    pass

def frequency(word, histogram):
    """returns the number of times that word appears in the  text"""
    for key, value in histogram.items():
        if key == word:
            return value
