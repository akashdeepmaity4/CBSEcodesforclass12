#WAP to find largest and smallest number among 10 numbers
L = []
for i in range(10):
    n = int(input("enter a number"))
    L.append(n)
print("the largest number is",max(L))
print("the smallest number is",min(L))

#WAP using functions to find factorials and check prime number
import math
def get_factorial(n):
    if n < 0:
        return "Undefined for negative numbers"
    return math.factorial(n)
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
num = int(input("Enter a number: "))
fact = get_factorial(num)
print(f"The factorial of {num} is: {fact}")
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

 #WAP to count vowels and consonanants
text = input("Enter a string: ")
vowels_count = 0
consonants_count = 0
vowels = "aeiouAEIOU"
for char in text:
    if char.isalpha():
        if char in vowels:
            vowels_count += 1
        else:
            consonants_count += 1
print("Number of vowels:", vowels_count)
print("Number of consonants:", consonants_count)

#WAP using lists to display even numbers
L = []
a = []
n = int(input("enter number of numbers you will input"))
for i in range(n):
    x = int(input("enter a number"))
    L.append(x)
for i in L:
    if(i%2 == 0):
        print(i,"is an even number")
        a.append(i)
    else:
        print(i,"is not an even number")
        print("all even numbers are",a)
        
#WAP to count words in a text file
'''add .txt file support using os module...'''
source = str(input("Enter the source text"))
tokens = source.split()
num_words = len(tokens)
print(f"the number of words in your source text is {num_words}")

#WAP to print pyramid pattern using asterisks
n = int(input("enter the bottoms rows' number"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end="")
    print()

#WAP to print Fibonacci series till n
'''This bit is not working,fix...'''

'''n = int(input("Enter till which number you want to print fibonacci series"))
def fib(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()'''

#WAP to print binary numbers
num = int(input("Enter a number to print binary numbers: "))
while num > 0:
    num = num >> 1
    print(num%2,end=" ")
print()

#WAP to print an inverted triangle using asterisks
n = int(input("enter the bottoms rows' number"))
for i in range(1,n+1):
    for j in range(i,n+1):
        print("*",end="")
    print()

#WAP to check if a number is odd or even
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(num,"is an even number")
else:
    print(num,"is an odd number")

#WAP to display the names of books in uppercase of those books which name start with consonant
books = []
books_final = []
n = int(input("Enter the number of books: "))
for i in range(n):
    names = input("Enter the name of the book")
    if names.isalpha():
        books.append(names)
    else:
        print("enter a valid string")

for i in books:
    if i[0] in "aeiouAEIOU":
        books_final.append(i.upper())
    else:
        books_final.append(i)

print(f"The books which name start with consonant are: {books_final}")

#WAP that prints the count of occurrences of searched word ""SCARCE" in the string
text = input("Enter a string: ")
word = input("Enter a word: ")
count = 0
for i in text:
    if i == word:
        count += 1
print(f"The word {word} occurs {count} times in the string")

# WAP that accepts a list of numbers and a numeric value by which all the elements of the list are shifted to left
# WAP that accepts a list of numbers and a numeric value by which all the elements of the list are shifted to left
def left_shift(arr, n):
    if not arr:
        return arr
    
    n = n % len(arr)
    
    return arr[n:] + arr[:n]
user_input = input("Enter numbers separated by spaces: ")
numbers = [int(x) for x in user_input.split()]

shift_by = int(input("Enter the number of positions to shift left: "))

result = left_shift(numbers, shift_by)
print(f"\nOriginal list: {numbers}")
print(f"Left-shifted list: {result}")

# Write a Python program to calculate the length of the string entered by the user and print the result
string = input("Enter a string: ")
length = len(string)
print(f"The length of the string is {length}")

#WAP to display some of all items in a list
L = []
n = int(input("enter number of numbers you will input"))
for i in range(n):
    x = int(input("enter a number"))
    L.append(x)
print("the sum of all numbers in the list are",sum(L))

# Write a program to demonstrate string slicing
string = input("Enter a string: ")
print(string[0:5])
print(string[5:10])
print(string[10:15])

# #Write a program to create and display tuple
tuple = ("apple","banana","cherry")
print(tuple)

# Write a program to perform tuple slicing
tuple = ("apple","banana","cherry")
print(tuple[0:2])
print(tuple[1:3])

# Write a program to find the maximum value in a tuple
tuple = ("apple","banana","cherry")
max_value = max(tuple)
print(max_value)

# Write a program to sort elements of a tuple
tuple = ("apple","banana","cherry")
sorted_tuple = sorted(tuple)
print(sorted_tuple)

# Write a program to create and display a dictionary
dict = {"name":"John","age":25,"city":"New York"}
print(dict)

# Write a program to update elements in a dictionary
dict = {"name":"John","age":25,"city":"New York"}
updated_dict = dict.update({"age":26})
print(updated_dict)