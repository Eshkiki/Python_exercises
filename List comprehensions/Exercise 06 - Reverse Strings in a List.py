# Given a list of words, use list comprehension to reverse each word.
words = ["hello", "world", "python"]
reversed_words =  [ x[::-1] for x in words]
print(reversed_words)  

# Expected output: ['olleh', 'dlrow', 'nohtyp']