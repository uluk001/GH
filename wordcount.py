#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.
You can use small.txt and alice.txt files to test your functions with.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once.Instead identify just a first milestone,
e.g. "well the first step is to extract the list of words." Write the code to
get to that milestone, and just print your data structures at that point, and
then you can do a sys.exit(0) so the program does not run ahead into its
not-done parts. Once the milestone code is working, you can work on code for
the next milestone. Being able to look at the printout of your variables at one
state can help you think about how you need to transform those variables to get
to the next state. Python is very quick with this pattern, allowing you to make
a little change and run the program to see how it works.
Take advantage of that quick turnaround to build your program in little steps.
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.


def build_word_count_dict(filename):
    """Reads a file and returns a dictionary with word counts.
    All words are converted to lowercase."""
    word_count = {}

    with open(filename, "r") as f:
        for line in f:
            words = line.split()
            for word in words:
                word = word.lower()
                word_count[word] = word_count.get(word, 0) + 1

    return word_count


def print_words(filename):
    """Prints all words and their counts, sorted alphabetically by word."""
    word_count = build_word_count_dict(filename)

    # Sort by word (key) alphabetically
    for word in sorted(word_count.keys()):
        print(word, word_count[word])


def print_top(filename):
    """
    Prints the top 20 most common words,
    sorted by frequency (most common first).
    """
    word_count = build_word_count_dict(filename)

    # Sort by count (value) in descending order, then by word alphabetically
    # We create a list of (word, count) tuples and sort by count (descending)
    items = sorted(word_count.items(), key=lambda item: item[1], reverse=True)

    # Print only the top 20
    for word, count in items[:20]:
        print(word, count)


###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
    if len(sys.argv) != 3:
        print("usage: ./wordcount.py {--count | --topcount} file")
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == "--count":
        print_words(filename)
    elif option == "--topcount":
        print_top(filename)
    else:
        print("unknown option: " + option)
        sys.exit(1)


if __name__ == "__main__":
    main()
