sentence = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

vowels = ( "a", "e", "i", "o", "u" )

count_of_vowels = 0
count_of_consonants = 0
count_of_capitals = 0

for character in sentence: # L, o, r, e, m, space, i

    if (character in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ '): # False, False, False, False, False, True
        continue # executed

    if (character.isupper()): # character.upper() == character
        count_of_capitals += 1

    if (character.lower() in vowels): # False, True, False, True, False
        count_of_vowels += 1 # 1, 2
    else:
        count_of_consonants += 1 # 1, 2, 3


print(count_of_vowels)
print(count_of_consonants)
print(count_of_capitals)

sentence_without_space = ""
for character in sentence:
    if (character != " "):
        sentence_without_space += character

print(sentence_without_space)
print(sentence.replace(" ", "") == sentence_without_space)