# Given a list of words, use list comprehension to find words that contain the letter "a".

words = ["apple", "banana", "cherry", "date", "grape"]
words_with_a = [x for x in words if x in ['a']]
print(words_with_a)  # Expected output: ['apple', 'banana', 'date', 'grape']


# Expected output: ['apple', 'banana', 'date', 'grape']
 