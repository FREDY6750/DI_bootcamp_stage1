word = input("Enter a word: ")

# Create an empty dictionary
letter_indexes = {}

# Iterate through the word
for i, letter in enumerate(word):
    # If the letter is not already in the dictionary, add it as a key
    # and set its value to an empty list
    if letter not in letter_indexes:
        letter_indexes[letter] = []
    # Add the current index to the list of indexes for the letter
    letter_indexes[letter].append(i)

print(letter_indexes)
