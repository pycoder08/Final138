# Filename: finalSection1.py
# Author: Muhammad Conn
# Description: A graphical spellcheck program that compares words from an input file 
# against a dictionary file and identifies potentially misspelled words.

# Algorithm: 
# 1. Create a GUI window with text entry fields for input file and dictionary file paths
# 2. When user clicks "Next", read both files and split into word lists
# 3. For each word in the input file:
#    a. Clean the word by removing punctuation and converting to lowercase
#    b. Use binary search to check if the word exists in the dictionary
#    c. If not found, print the word as potentially incorrect
# 4. Binary search implementation:
#    a. Sort the dictionary list
#    b. Compare cleaned input word with middle element of sorted dictionary
#    c. Narrow search range based on alphabetical comparison until word found or range exhausted

from graphics import *
from button import *
import string

def main():
    win = GraphWin("Spellcheck", 600, 600)
    in_text = Text(Point(300, 100), "Enter the path to your input file:")
    in_box = Entry(Point(300, 200), 10)
    didct_text = Text(Point(300, 300), "Enter the path to your dictionary file:")
    dict_box = Entry(Point(300, 400), 10)
    next_button = Button(win, Point(300, 550), 50, 50, "Next")

    in_text.draw(win)
    in_box.draw(win)
    didct_text.draw(win)
    dict_box.draw(win)
    next_button.activate()

    while True:
        click = win.getMouse()
        if next_button.clicked(click):
            in_path = in_box.getText()
            dict_path = dict_box.getText()
            
            in_file = open(in_path, "r")
            dict_file = open(dict_path, "r")

            in_words = in_file.read().split()
            dict_words = dict_file.read().split()

            in_file.close()
            dict_file.close()

            print("Potentially incorrect words:")
            for word in in_words:
                if not (bin_word_search(word, dict_words)):
                    print(word)
            break

    
    

def bin_word_search(word, list):
    list.sort()
    left = 0
    right = len(list) - 1
    word_lower = word.strip(string.punctuation).lower()
    
    while left <= right:
        mid = (left + right) // 2
        mid_word = list[mid]

        if mid_word == word_lower:
            return True

        if mid_word < word_lower:
            left = mid + 1
        else:
            right = mid - 1

    return False


main()