#  a lambda function to find the length of each word in a li

words = ["Python", "Lambda", "Function"]
lengths = list(map( lambda x: len(x), words))
print(lengths)  

# Expected output: [6, 6, 8]