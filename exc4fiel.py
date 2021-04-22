#https://rt-ed.co.il/articles/python-language-questions-and-answers/
#q5
import sys


def get_file(fname):
    # Using readline()
    file1 = open(fname, "r+")
    sum =0
    for line in file1:
        sum = sum+int(line)

    file1.write("{}n".format(sum))
    file1.close()

get_file('ftxt.txt')

