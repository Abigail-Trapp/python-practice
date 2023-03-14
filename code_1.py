# "print" reveals the output in the console. 
print(2+3)
print(3-1)
print(4*2)

# Built-in functions that result in a floating point number
print(14/7)
# Use quotient // to get an integer
print(14//7)

print(+3)
print(+34)  # examples of unary plus
print(+3j)

# negation
print(-3)

# calculate the remainder when first number is divided by second
print(3 % 2)

# Exponentiation - raises first number to the power of the second number
print(2 ** 4)
print(pow(2,3))

# absolute value 
print(abs(-3.4))

# ask a user for input
print(input("Enter your age: "))

#determine the type
print(type(5))
print(type("5"))
print(type(5.0))

# Make number into an integer
print(int(5.1))

# Float converts a number or a number as a string into a floating point number.
print(float(5))
print(float("5"))

# String converts numbers or strings into a string. 
print(str(3))

# Produce length of a string
print(len("cat"))

# [i] shows what takes place at the "i" index
print("cat"[1])

#concatenation - ties together two entries
print("hot" + "dog")

# * repeated concatenation
print([3,4] * 2)

# Slice produces a substring from first position up to but not including the second position
print("hotdog"[2:5])

# outputs minimum number
print(min([4,3,6]))

# outputs maximum number
print(max([4,3,6]))

# Count shows number of times an input appears in a list. 
print([8,7,8,9].count(8))

# Achieve index in an input list.
print([1,2,3,4].index(2))

# Produce "True" or "False" if a value is found in a list
print(9 in [8,9,7])

# Produces input as a list of inputs that make up the input, input list does not change 
print(list("dog"))