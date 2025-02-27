# Given a string, use list comprehension to extract all vowels from it.

text = "hEllo wOrld"
vowels = [x for x in text if x.lower()  in ['a', 'e', 'u' ,'i', 'o' ] ]
print(vowels)  

# Expected output: ['E', 'o', 'O']