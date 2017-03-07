#!/usr/bin/env python3
import sys
# Task: Count how many words are in a file
#getting file from the web with urlopen
from urllib.request import urlopen


def fetch_words(url):
    """
    Fetch a list of words from a URL
    ARGS:
        url -> The URL of a UTF-8 text document
    Return:
        A list of strings containg the words from the document
    """
    with urlopen(url) as story:  
        story_words = []    #set empty array
        for line in story: # iterate over file (lines) 
            line_words = line.split()   #split record into a list
            for words in line_words:    # iterate over list(words)
                story_words.append(words.decode("utf-8"))   #words are encoded
    return story_words          
          

def print_items(items):
    """
    Print items one per line
    ARGS:
        An iterable series of printable items
    Returns:
        Nothing
    """
    for item in items:
        print(item)

def main():
    """
    Print each word from a text document from a URL
    Usage:
        python3 words.py <URL>
    """
    #url = "http://icarus.cs.weber.edu/~hvalle/cs3030/data/snippet.txt"
    url = sys.argv[1]
    words = fetch_words(url)
    print_items(words)

if __name__== '__main__':
    main()
    exit(0)
    
