from graphics import *

def main():
    win = GraphWin("Spellcheck, 600, 600")
    in_text = Text(Point(300, 100), "Enter the path to your input file:")
    in_box = Entry(Point(300, 200), 10)
    didct_text = Text(Point(300, 300), "Enter the path tp your dictionary file:")
    dict_box = Entry(Point(300, 400), 10)
    
    in_text.draw()
    in_box.draw()
    didct_text.draw()
    dict_box.draw()

    in_file = open(in_box.getText(), "r")
    dict_file = open(dict_box.getText(), "r")

    in_words = in_file.read()
    dict_words = dict_file.read()

    print("Potentially incorrect words:")
    for word in in_words:
        if not (bin_word_search(word, dict_words)):
            print(word)
    



main()

def abc_score(word):
    score = 0
    for letter in word:
        score += ord(letter.lower()) - ord("a")

def bin_word_search(word, list):
    score = abc_score(word)
    while left <= right:
        mid = (left + right) // 2

        if list[mid] == score:
            return True

        if list[mid] < score:
            left = mid + 1
        else:
            right = mid - 1

    return False