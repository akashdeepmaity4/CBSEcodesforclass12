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
        print(i,"is an even number. moving to the next number...")
        a.append(i)
    else:
        print(i,"is not an even number.moving to the next number...")
        print("all even numbers are",a)
        #WAP to count lines and words in a text file 

print("Enter/Paste your test (Press Enter on an empty line to finish):")
lines_list = []
while True:
    line = input()
    if line == "":  
        return "enter something"
    lines_list.append(line)
line_count = len(lines_list)
word_count = 0
for line in lines_list:
    words_in_line = line.split() 
    word_count += len(words_in_line)
print("\n--- Results ---")
print("Total number of lines:", line_count)
print("Total number of words:", word_count)

#WAP to print pyramid pattern using asterisks
for i in range(1,10):
    for j in range(1,i+1):
        print("*",end="")
    print()

#WAP to print Fibonacci series till n
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
n = int(input("Enter a number: "))
print(fib(n))

#WAP to print binary numbers
num = int(input("Enter a number: "))
while num > 0:
    num = num >> 1
    print(num%2,end=" ")
print()

#WAP to print an inverted triangle using asterisks
for i in range(1,10):
    for j in range(i,10):
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
for i in range(1,n+1):
    names = input("Enter the name of the book: ")
    if names.isinstance(str):
        books.append(names)
    else:
        return "enter a valid string"

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

# there is a program that accepts a list of numbers and a numeric value by which all the elements of the list are shifted to left
L = []
n = int(input("enter number of numbers you will input"))
for i in range(n):
    x = int(input("enter a number"))
    L.append(x)
shift = int(input("enter a number"))
for i in L:
    i = i << shift
    print(i)

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
print("all numbers in the list are",sum(L))

# Write a program to demonstrate string slicing
string = input("Enter a string: ")
print(string[0:5])
print(string[5:10])
print(string[10:15])

# #Write a program to create anddisplay tuple
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
"""delete from here """
#WAP to creaate database wuh python and mysql
import mysql.connector as m
mym = m.connect(host="localhost",user="root",passwd="root",database="python")
cursor = mym.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS students(id INT NOT NULL AUTO_INCREMENT,name VARCHAR(50),age INT,PRIMARY KEY(id))")
cursor.execute("INSERT INTO students(name,age) VALUES('John',25)")
cursor.execute("INSERT INTO students(name,age) VALUES('Tom',30)")
cursor.execute("INSERT INTO students(name,age) VALUES('Peter',35)")
cursor.execute("INSERT INTO students(name,age) VALUES('Sarah',40)")
cursor.execute("INSERT INTO students(name,age) VALUES('Michael',45)")
cursor.execute("INSERT INTO students(name,age) VALUES('Jenny',50)")
mym.commit()
mym.close()
rows = cursor.fetchall()
for row in rows:
    print(row)

#WAP to create employee database using mysql and input 5 employees' details
import mysql.connector as m
mym = m.connect(host="localhost",user="root",passwd="root",database="employee")
cursor = mym.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS employee(id INT NOT NULL AUTO_INCREMENT,name VARCHAR(50),salary INT,PRIMARY KEY(id))")
for i in range(5):
    name = input("Enter name of employee: ")
    salary = int(input("Enter salary of employee: "))
    cursor.execute("INSERT INTO employee(name,salary) VALUES(%s,%s)",(name,salary))
mym.commit()
mym.close()

#WAP to display the details of all employees using curcor
import mysql.connector as m
mym = m.connect(host="localhost",user="root",passwd="root",database="employee")
cursor = mym.cursor()
cursor.execute("SELECT * FROM employee")
rows = cursor.fetchall()
for row in rows:
    print(row)

#WAP to search employee using employee id entered by the user
import mysql.connector as m
mym = m.connect(host="localhost",user="root",passwd="root",database="employee")
cursor = mym.cursor()
id = int(input("Enter employee id: "))
cursor.execute("SELECT * FROM employee WHERE id=%s",(id))
rows = cursor.fetchall()
for row in rows:
    print(row)

#WAP to update employee salary using employee id entered by the user
import mysql.connector as m
mym = m.connect(host="localhost",user="root",passwd="root",database="employee")
cursor = mym.cursor()
id = int(input("Enter employee id: "))
salary = int(input("Enter new salary: "))
cursor.execute("UPDATE employee SET salary=%s WHERE id=%s",(salary,id))
mym.commit()
mym.close()