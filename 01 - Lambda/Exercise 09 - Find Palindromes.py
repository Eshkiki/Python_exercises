# a lambda function to filter out words that are palindromes from a list.

words = ["madam", "hello", "racecar", "world", "level"]
palindromes = list(filter( lambda x : x[::-1] == x , words))
print(palindromes) 

# Expected output: ['madam', 'racecar', 'level'] 