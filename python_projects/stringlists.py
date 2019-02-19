string = raw_input("Enter a word: ")
str.lower(string)
if string == string[::-1]:
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")
