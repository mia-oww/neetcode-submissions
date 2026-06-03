from typing import List

# new function sorted()
#sorted() returns a new list and does not modify the old list
def sort_words(words: List[str]) -> List[str]:
    # ascending order
    new_sorted_words = sorted(words, key=None, reverse=False)
    return new_sorted_words


def sort_numbers(numbers: List[int]) -> List[int]:
    # new list descending (greatest to least)
    new_sorted_numbers = sorted(numbers, key=lambda number: abs(number), reverse=True)
    return new_sorted_numbers


# do not modify below this line
original_words = ["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]

print(original_words)
print(sort_words(original_words))

original_numbers = [1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]

print(original_numbers)
print(sort_numbers(original_numbers))
