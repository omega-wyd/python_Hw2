#!/usr/bin/env python3

# Task: Count how many words are in a file
#getting file from the web with urlopen
from urllib.request import urlopen

with urlopen("http://icarus.cs.weber.edu/~hvalle/cs3030/data/snippet.txt") as story:  
    story_words = []
    for line in story:
        line_words = line.split()
        for words in line_words:
            story_words.append(words.decode("utf-8"))
            print(words.decode("utf-8"))

print(story_words)
print("Total count is ", len(story_words))



#exit(0)        
