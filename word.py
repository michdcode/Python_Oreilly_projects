import scrabble
import string

# # fin words that have "uu" in them 
for word in scrabble.wordlist:
    if "uu" in word:
        print(word)
# can also do this as a list comprehension:
[word for word in scrabble.wordlist if "uu" in word]


# letters that never appear double in a word
for letter in string.ascii_lowercase:
    exists = False
    for word in scrabble.wordlist:
        if letter * 2 in word:
            exists = True
            break
    if not exists:
        print("No English words with a double of " + letter)

# find word that uses all of the vowels
vowels = "aeiou"

def has_all_vowels(word):
    for vowel in vowels:
        if vowel not in word:
            return False
    return True    

for word in scrabble.wordlist:
    if has_all_vowels(word):
        print(word)

