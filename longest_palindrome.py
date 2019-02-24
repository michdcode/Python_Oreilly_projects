import scrabble

# mathy solution
longest = ""
for word in scrabble.wordlist:
    is_palindrome = True
    for index in range(len(word)):
        if word[index] != word[-(index + 1)]:
            is_palindrome = False
    if is_palindrome and len(word) > len(longest):
        longest = word
print(longest)

# another option:
for word in scrabble.wordlist:
    if list(word) == list(reversed(word)) and len(word) > len(longest):
        longest = word
print(longest)

#most elegant - remember that ::-1 is just starting and end and going back by one
for word in scrabble.wordlist:
    if word == word[::-1] and len(word) > len(longest):
        longest = word
print(longest)

# can also do this as a list compehension - partially
[word for word in scrabble.wordlist if word == word[::-1 ]]