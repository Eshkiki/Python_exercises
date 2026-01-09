# Given a list of words, use list comprehension to extract maximum number.


maximum =  lambda x,y: (((x-y)>0) * x) + ( ((y-x) >0) * y)+ ((x == y) * x)
print(maximum(10, 20))  

# Expected output: 20
