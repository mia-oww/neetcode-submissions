from typing import List

#defining helper functions for key
def word_length(word): 
    return len(word) # returns the length of the word
def absvalue(number):
    return abs(number) # returns the abs value of numbers


def sort_words(words: List[str]) -> List[str]:
    # sort based on word length
    words.sort(key=word_length, reverse=True) # sorting from greatest word length -> least
    return words


def sort_numbers(numbers: List[int]) -> List[int]:
    numbers.sort(key=absvalue)
    return numbers


# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))
