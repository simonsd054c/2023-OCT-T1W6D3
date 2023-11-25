# palindrome

# string reversed is also the same as original string

# simon = nomis # not a palindrome
# anna = anna # a palindrome

original_string = "racecar"

reversed_string = ""

for character in original_string: # h, e, l, l, o
    reversed_string = character + reversed_string # h, eh, leh, lleh, olleh

print(reversed_string)

if(reversed_string == original_string):
    print("Palindrome")
else:
    print("Not a palindrome")


# string[start:end:step]

if (original_string[::-1] == original_string):
    print("Palindrome")
else:
    print("Not a palindrome")

print("Palindrome") if original_string[::-1] == original_string else print("Not a palindrome")

print(original_string[::-1] == original_string)