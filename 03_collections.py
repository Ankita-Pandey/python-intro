# -*- coding: utf-8 -*-
"""03_Collections.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MHsStV6GHNr9Ayn9q-kZXS86Razjd53E

#  Introduction to Python

##***Welcome to your Third iPython Notebook.***

![python](https://cognitiveclass.ai/wp-content/uploads/2016/10/Machine-Learning-with-Python.png)

## **About iPython Notebooks**

iPython Notebooks are interactive coding environments embedded in a webpage. You will be using iPython notebooks in this class. You only need to write code between the ### START CODE HERE ### and ### END CODE HERE ### comments. After writing your code, you can run the cell by either pressing "SHIFT"+"ENTER" or by clicking on "Run Cell" (denoted by a play symbol) in the left bar of the cell.


**In this notebook you will learn -** 
* Collection

#Python Collections

Python Collections (Arrays)
There are four collection data types in the Python programming language:




*  ** List** is a collection which is ordered and changeable. Allows duplicate members.
*  **Tuple** is a collection which is ordered and unchangeable. Allows duplicate members.
*  ** Set** is a collection which is unordered and unindexed. No duplicate members.
*  ** Dictionary** is a collection which is unordered, changeable and indexed. No duplicate members.

When choosing a collection type, it is useful to understand the properties of that type. Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.

##List
A list is a collection which is **ordered** and **changeable**. In Python lists are written with square brackets.

**Create a List:**
"""

thislist = ["apple", "banana", "cherry"]
print(thislist)

"""**Access Items :** 

You access the list items by referring to the index number
"""

thislist = ["apple", "banana", "cherry"]
print(thislist[1])                                   # Prints the second item of the list

"""**Change Item Value :**

To change the value of a specific item, refer to the index number
"""

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)                                      # Changes the second item

"""**Loop Through a List :**

You can loop through the list items by using a **for** loop
"""

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)                                            # Prints all items in the list, one by one

"""**Check if Item Exists:** 

To determine if a specified item is present in a list use the 'in'  keyword.
"""

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")         # Checks if "apple" is present in the list

"""**List Length :** 

To determine how many items a list have, use the len() method
"""

thislist = ["apple", "banana", "cherry"]
print(len(thislist))                                   # Prints the number of items in the list

"""**Add Items :** 

To add an item to the end of the list, use the append() method.
"""

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

"""To add an item at the specified index, use the insert() method"""

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")                            # Inserts an item as the second position
print(thislist)

"""**Remove Item :**

There are several methods to remove items from a list

**The remove() method :** 
The remove() method removes the specified item
"""

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

"""**The pop() method :**
The pop() method removes the specified index, (or the last item if index is not specified)
"""

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

"""**The del keyword :**
The del keyword removes the specified index.
"""

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

"""The del keyword can also delete the list completely:"""

thislist = ["apple", "banana", "cherry"]
del thislist
print(thislist)                      #this will cause an error because "thislist" no longer exists.

"""**The clear() method :**
The clear() method empties the list
"""

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

"""**The list() Constructor :**

It is also possible to use the list() constructor to make a list.
"""

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

"""**Exercise 3.1:**

Create a list named BestOfTv add the following items in it Breakin Bad,Game of Thrones and Mr Robot. Then perform the following actions on the list:

*   Remove Game Of Thrones from it.
*   Add Friends to the list at 0 index. 
*  Check if Game Of Thrones is in the list if it is print("GOT is in BestOfTv") otherwise print("GOT is not in BestOfTv")
"""

### START CODE HERE ##
                                  ##Create list
print(BestOfTv)
                                  ##Remove Game Of Thrones
print(BestOfTv)
                                  ##Add Friends at index 0 
print(BestOfTv)
                                  ##Check if Game Of Thrones is in the list  



### END CODE HERE ###

"""**Expected Output:**

['Breaking Bad', 'Game Of Thrones', 'Mr Robot']

['Breaking Bad', 'Mr Robot']

['Friends', 'Breaking Bad', 'Mr Robot']

GOT is not in BestOfTv

##Tuples
A tuple is a collection which is **ordered** and **unchangeable**. In Python tuples are written with round brackets.

**Create a Tuple:**
"""

thistuple = ("apple", "banana", "cherry")          # Creates a tuple
print(thistuple)

"""**Access Tuple Items:**

You can access tuple items by referring to the index number.
"""

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])                                # Return the item in position 1

"""**Change Tuple Values:**

 You cannot change values in a tuple. Tuples are **unchangeable**. The values will remain the same.
"""

thistuple = ("apple", "banana", "cherry")          
thistuple[1] = "mango"                             # This will raise an error
print(thistuple)

"""**Tuple Length:**

To determine how many items a list have, use the len() method.
"""

thistuple = ("apple", "banana", "cherry")          # This will print the number of items in the tuple.
print(len(thistuple))

"""**Add Items:**

Once a tuple is created, you cannot add items to it. Tuples are** unchangeable**.
"""

thistuple = ("apple", "banana", "cherry")         
thistuple[3] = "orange"                            # This will raise an error
print(thistuple)

"""**Remove Items:**

 Tuples are unchangeable, so you cannot remove items from it, but you can delete the tuple completely.
"""

thistuple = ("apple", "banana", "cherry")          #The del keyword can delete the tuple completely
del thistuple
print(thistuple)                                   # This will raise an error because the tuple no longer exists

"""**The tuple() Constructor:**

It is also possible to use the tuple() constructor to make a tuple.
"""

thistuple = tuple(("apple", "banana", "cherry"))    # note the double round-brackets
print(thistuple)

"""**Loop Through a Tuple:**

You can loop through the tuple items by using a for loop.
"""

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

"""**Exercise 3.2:**

Perform the following action on the tuple



*   Display the length of the tuple
*   Display the item in third position
"""

### START CODE HERE ###

food = ("pizaa", "burger", "cake") 
                                    ##Display the length
                                    ##Display the item

### END CODE HERE ###

"""**Expected Output: **

3

cake

## Sets
A set is a collection which is **unordered** and **unindexed**. In Python sets are written with curly brackets.

**Create a Set:**
"""

thisset = {"apple", "banana", "cherry"}
print(thisset)

"""**Note:** Sets are unordered, so the items will appear in a random order.

**Access Items:**

You cannot access items in a set by referring to an index, since sets are unordered the items has no index.

But you can loop through the set items using a for loop.
"""

thisset = {"apple", "banana", "cherry"}

for x in thisset:                                    #Loops through the set, and print the values              
  print(x)

"""**Change Items:**

Once a set is created, you cannot change its items, but you can add new items.

**Add Items:**
To add one item to a set use the add() method.
"""

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

"""**Update Items:** To add more than one item to a set use the update() method."""

thisset = {"apple", "banana", "cherry"}

thisset.update(["orange", "mango", "grapes"])

print(thisset)

"""**Get the Length of a Set:**

To determine how many items a set have, use the len() method.
"""

thisset = {"apple", "banana", "cherry"}

print(len(thisset))

"""**Remove Item:**

To remove an item in a set, use the remove(), or the discard() method.
"""

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)                                            # Note: If the item to remove does not exist, discard() will NOT raise an error.

"""**The set() Constructor:**

It is also possible to use the set() constructor to make a set.
"""

thisset = set(("apple", "banana", "cherry"))              # note the double round-brackets
print(thisset)

"""**clear() method :**

The clear() method empties the set.
"""

thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

"""**Exercise 3.3:**

Write a Python script to perform the following actions on a **set**.



*   Create a set called games with items witcher,cs,fortnite.
*   Add pubg to the set
*   Remove fortnite from the set
*   Empty the set
"""

### START CODE HERE 
games = {"witcher", "cs", "fortnite"}
print(games)
games.add("pubg")
print(games)
games.remove("fortnite")
print(games)
games.clear()
print(games)
### END CODE HERE ###

"""**Expected output**: 

{'witcher', 'fortnite', 'cs'}
{'witcher', 'fortnite', 'cs', 'pubg'}
{'witcher', 'cs', 'pubg'}
set()

## Dictionary

A dictionary is a collection which is** unordered**, **changeable** and **indexed**. In Python dictionaries are written with curly brackets, and they have keys and values.

**Create a dictionary:**
"""

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)                                        # prints the dictionary.

"""**Accessing Items:**

You can access the items of a dictionary by referring to its key name
"""

x = thisdict["model"]                                  # Gets the value of the "model" key
print(x)

"""There is also a method called get() that will give you the same result:"""

x = thisdict.get("model")                              # Gets the value of the "model" key
print(x)

"""**Change Values:**

You can change the value of a specific item by referring to its key name.
"""

#Change the "year" to 2018:

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018                                # Changes the "year" to 2018
print(thisdict)

"""**Loop Through a Dictionary:**

You can loop through a dictionary by using a for loop.

When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.
"""

for x in thisdict:
  print(x)                                            # Prints all key names in the dictionary, one by one.

"""You can also use the values() function to return values of a dictionary:"""

for x in thisdict.values():                     
  print(x)                                            # Prints all values in the dictionary, one by one.

"""Loop through both keys and values, by using the items() function:"""

for x, y in thisdict.items():
  print(x, y)                                          # Prints both keys and values, in the dictionary, one by one.

"""**Check if Key Exists:**

To determine if a specified key is present in a dictionary use the ' in'  keyword.
"""

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
} 
if "model" in thisdict:                                 # Checks if "model" is present in the dictionary
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

"""**Dictionary Length:**

To determine how many items (key-value pairs) a dictionary have, use the len() method.
"""

print(len(thisdict))

"""**Adding Items :**

Adding an item to the dictionary is done by using a new index key and assigning a value to it.
"""

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

"""**Removing Items :**

There are several methods to remove items from a dictionary

**The pop() method :**

The pop() method removes the item with the specified key name
"""

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

"""**The popitem() method :**

The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead)
"""

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

"""**The del keyword :**

The del keyword removes the item with the specified key name
"""

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

"""The del keyword can also delete the dictionary completely"""

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
print(thisdict)                           #this will cause an error because "thisdict" no longer exists.

"""**Exercise 3.4:**

Write a Python script to perform the following actions to a dictionary.


*    Create a dictionary with items 0:10,1:20
*   Add 2:30 to the following dictionary
"""

### START CODE HERE ### (1 line of code)

d = {0:10, 1:20}
print(d)
d.update({2:30})
print(d)                

### END CODE HERE ###

"""**Expected Output: **{0: 10, 1: 20, 2: 30}

# Great Job!
"""