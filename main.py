from stats import word_count
from stats import char_count
from stats import sort_dic
from stats import report
import sys


def get_book_text(filepath):
    with open (filepath) as f:
        file_contents =f.read()
        return file_contents

def main():
    if len(sys.argv) !=2:
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path =sys.argv[1]
    text = get_book_text(path)
    wc= word_count(text)
    charc= char_count(text)
    ch= sort_dic(charc)
    report(path,wc,ch)


main()

