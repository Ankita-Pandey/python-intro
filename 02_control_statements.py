# -*- coding: utf-8 -*-
"""02_Control_Statements.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1smqbjBhp4ssbFDy0JoMFERGofXo_EMyI

#  Introduction to Python

##***Welcome to your second  iPython Notebook.***

![python](https://cognitiveclass.ai/wp-content/uploads/2016/10/Machine-Learning-with-Python.png)

## **About iPython Notebooks**

iPython Notebooks are interactive coding environments embedded in a webpage. You will be using iPython notebooks in this class. You only need to write code between the ### START CODE HERE ### and ### END CODE HERE ### comments. After writing your code, you can run the cell by either pressing "SHIFT"+"ENTER" or by clicking on "Run Cell" (denoted by a play symbol) in the left bar of the cell.


**In this notebook you will learn -**



* If else
* Loops

# Python If Else

**To understand If Else statement first you need to know the logic operators.**

  * Equals: **a == b**
  * Not Equals: **a != b**
  * Less than: **a < b**
  * Less than or equal to: **a <= b**
  * Greater than: **a > b**
  * Greater than or equal to: **a >= b**

![alt text](http://i.imgur.com/fqJOBUS.png)

**If statement:**

An "if statement" is written by using the if keyword.
"""

a = 33
b = 200
if b > a:
  print("b is greater than a")

"""**NOTE: ** As you can see in the above example unlike other languages, Python doesn't use curly brackets to define a block of code. Instead Python uses something called Identation. Identation is a particular length of whitespaces before a line of code.

**Exercise 2.1:** 

If **x** is greater than **y** print "Joker".
"""

### START CODE HERE ### 
x = 50
y = 49
                       

### END CODE HERE ###

"""**Expected Output:**

Joker

**Elif statement:**

The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".
"""

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

"""**Else:**

The else keyword catches anything which isn't caught by the preceding conditions.
"""

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

"""**Short Hand If:**
 
If you have only one statement to execute, you can put it on the same line as the if statement.
"""

if a > b: print("a is greater than b")

"""**Short Hand If Else:**

If you have only one statement to execute, one for if, and one for else, you can put it all on the same line.
"""

print("A") if a > b else print("B")

"""**And Operator:**

The **and** keyword is a logical operator, and is used to combine conditional statements.
"""

if a > b and c > a:
  print("Both conditions are True")         #Test if a is greater than b, AND if c is greater than a

"""**Or Operator**

The **or** keyword is a logical operator, and is used to combine conditional statements.
"""

if a > b or a > c:
  print("At least one of the conditions are True")         #Test if a is greater than b, OR if a is greater than c

"""**Exercise 2.2:**

Print if the number is positive or negative using If Else
"""

### START CODE HERE ### 

num = -6
                                      ##1 line of code                      
 print(num, "is a positive number.")
                                      ##1 line of code
 print(num, "is a negative number.")
  

### END CODE HERE ###

"""**Expected Output: **"-6 is a negative number.

# Python Loops

Lets say you want to print something multiple times. It is not efficient to use print statement again and again so there is a concept called **Loops**.

**Python has two primitive loop commands:**



*   **While** Loop
*   **For** Loop

##While Loop

With the while loop we can execute a set of statements as long as a condition is true.
"""

i = 1
while i < 6:
  print(i)              #Print i as long as i is less than 6
  i += 1                #Increment i after every loop

"""##The break Statement
With the break statement we can stop the loop even if the while condition is true.The break statement terminates the loop containing it. Control of the program flows to the statement immediately after the body of the loop. If break statement is inside a nested loop (loop inside another loop), break will terminate the innermost loop.
"""

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 
  if x == "banana":
    break                                #Exits the loop when x is "banana"

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)                              # Exits the loop when x is "banana", but this time the break comes before the print.

"""##The continue Statement
With the continue statement we can stop the current iteration, and continue with the next
"""

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana": 
    continue                                   #Do not print banana
  print(x)

"""**Exercise 2.3:**

Print "yo" twice using **while**  loop.
"""

### START CODE HERE ### (4 line of code)

i = 1
                    ##1 line of code
 print("yo")
                    ##1 line of code               

### END CODE HERE ###

"""**Expected Output: **"Hello World"

##For Loop

A **for** loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

![alt text](https://www.datamentor.io/wp-content/uploads/2017/11/r-for-loop.jpg)

Python’s for statement iterates over the items of any sequence (a list or a string), in the order that they appear in the sequence.
"""

fruits = ["apple", "banana", "cherry"]
for x in fruits:                            #Print each fruit in a fruit list
  print(x)

"""**Looping Through a String**

Even strings are iterable objects, they contain a sequence of characters
"""

for x in "banana":         #Loop through the letters in the word "banana"
  print(x)

"""** Measure some strings:**

words = ['cat', 'wind', 'python']
"""

words = ['cat', 'wind', 'python']
for w in words:
  print(w, len(w))

"""If you need to modify the sequence you are iterating over while inside the loop (for example to duplicate selected items), it is recommended that you first make a copy. Iterating over a sequence does not implicitly make a copy. The slice notation makes this especially convenient:"""

words = ['cat', 'wind', 'python']
  
  for w in words[:]:       # Loop over a slice copy of the entire list.
    if len(w) > 6:
       words.insert(0, w)

"""####The range() Function
While working with For Loop, it is important to know about **range()** function.

To loop through a set of code a specified number of times, we can use the **range()** function,
The **range()** function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
"""

for x in range(6):
  print(x)

"""**NOTE: ** The function range(6) is not the values of 0 to 6, but the values 0 to 5. The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6).

**Exercise 2.4:**

Write a program to print all the numbers from 0 to 10 that are divisible by 2 using **for** loop. 

Hint Use **if** function if necessary.
"""

### START CODE HERE ### (3 line of code)


               

### END CODE HERE ###

"""**Expected Output: **

0
2
4
6
8

# Great Job!
"""