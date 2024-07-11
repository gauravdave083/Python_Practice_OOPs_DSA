# Python DSA and OOP

Welcome to the **Python DSA and OOP** repository! This repository is a comprehensive collection of Python implementations for various Data Structures and Algorithms (DSA) as well as Object-Oriented Programming (OOP) concepts. It is designed to serve as a resource for students, developers, and anyone interested in strengthening their understanding and skills in these fundamental areas of computer science.

## Overview

In this repository, you will find:

- **Data Structures**: Implementations of common data structures such as arrays, linked lists, stacks, queues, trees, and more.
- **Object-Oriented Programming**: Examples and explanations of OOP principles such as classes, objects, inheritance, polymorphism, encapsulation, and abstraction.
- **Practical Examples**: Real-world examples and problem-solving techniques using DSA and OOP principles.

## Structure

The repository is organized into the following directories:

- `data_structures/`: Contains implementation of various data structures.
- `oop_concepts/`: Demonstrates OOP concepts with examples and explanations.
- `examples/`: Contains practical examples and problem-solving scenarios.

## Getting Started

To get started with this repository, clone it to your local machine:

```bash
git clone https://github.com/your-username/python-dsa-oop.git
cd python-dsa-oop
```

## Syntax Of Print Statement
```bash
print("Hello World")
```

Comments in Python are written with a special character, which one?
```bash
YES , "#".
FOR MULTILINE COMMENT WE USE THIS """  
                                     statements
                                  """
```

<br>

## Variable Declaration 

## Data Types

In programming, data type is an important concept.
Variables can store data of different types, and different types can do different things.
Python has the following data types built-in by default, in these categories:

```bash
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
```
<br>

### Question : The following code example would print the data type of x, what data type would that be?

```bash
x = ["apple", "banana", "cherry"]
print(type(x))
print(x)
```
### Answer : List[].
<br>
<br>

### Question: The following code example would print the data type of x, what data type would that be?

```bash
x = ("apple", "banana", "cherry")
print(type(x))
print(x)
```
### Answer: Tuple().

<br>
<br>

### Question: The following code example would print the data type of x, what data type would that be?

```bash
x = {"name" : "John", "age" : 36}
print(type(x))
print(x)
```
### Answer: Dictionary{}.

<br>
There are three numeric types in Python:

1. int
2. float
3. complex

<br>

## Numbers
Variables of numeric types are created when you assign a value to them:

```bash
x = 1    # int
y = 2.8  # float
z = 1j   # complex
```

<br>

You can convert from one type to another with the int(), float(), and complex() methods:
```bash
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
```

<br>

Import the random module, and display a random number between 1 and 9:
```bash
import random

print(random.randrange(1, 10))
```

<br>


### Question: <br>Use the len function to print the length of the string.

```bash
x = "Hello World"
print(len(x))
```

<br>

### Question: <br>Get the first character of the string txt.

```bash
txt = "Hello World"
x = txt[0]
```
<br>

### Question: <br>Get the characters from index 2 to index 4 (llo).

```bash
txt = "Hello World"
x = txt[2:5]
```

<br>

### Question : <br>Return the string without any whitespace at the beginning or the end.

```bash
txt = " Hello World "
x = txt.strip()
```

<br>

### Question : <br>Convert the value of txt to upper case & lower case.

```bash
txt = "Hello World"
txt = txt.upper()

txt = "Hello World"
txt = txt.lower()
```

<br>

### Question: <br>Replace the character H with a J.

```bash
txt = "Hello World"
txt = txt.replace("H", "J")
```

<br>

### Question: <br>Insert the correct syntax to add a placeholder for the age parameter.

```bash
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
```

<br>

## Operators
Python divides the operators in the following groups:

Arithmetic operators
Assignment operators
Comparison operators
Logical operators
Identity operators
Membership operators
Bitwise operators

<br>

### Arithmetic Operators
Arithmetic operators are used with numeric values to perform common mathematical operations:

![alt text](assets/Images/operators_arithmetic.png)

### Assignment Operators
Assignment operators are used to assign values to variables:

![alt text](assets/Images/assign_operators.png)

### Comparison Operators
Comparison operators are used to compare values:

![alt text](assets/Images/operators-comparison.png)

### Logical Operators
Logical operators are used to combine conditional statements:

![alt text](assets/Images/operators-logical.png)

<br>

## Lists

Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

Lists are created using square brackets:

```bash
thislist = ["apple", "banana", "cherry"]
print(thislist)
```

### List Items
List items are ordered, changeable, and allow duplicate values.

List items are indexed, the first item has index [0], the second item has index [1] etc.

### Example
Lists allow duplicate values:

```bash
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
```

<br>

### Question:
Print the number of items in the list:

```bash
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
```

### Question:
Print the number of items in the list:

```bash
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
```

### Question:
String, int and boolean data types:

```bash
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
```

### Question:
Use the insert method to add "lemon" as the second item in the fruits list.

```bash
fruits = ["apple", "banana", "cherry"]
fruits.insert(1,"lemon")
```

### Question:
Use the remove method to remove "banana" from the fruits list.

```bash
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
```

<br>
<br>
<br>

## Tuple () 

Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets.

### Example: 
Use the correct syntax to print the first item in the fruits tuple.

```bash
fruits = ("apple", "banana", "cherry")
print(fruits[0])
```

### Tuple Items
Tuple items are ordered, unchangeable, and allow duplicate values.

Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

*Ordered:<br>
When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

*Unchangeable:<br>
Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

*Allow Duplicates:<br>
Since tuples are indexed, they can have items with the same value:

### Example:
Tuples allow duplicate values:

```bash
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
ADVERTISEMENT
```

### Question;
Print the number of items in the tuple:

```bash
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
```

<br>

To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.

### Example
One item tuple, remember the comma:

```bash
thistuple = ("apple",)
print(type(thistuple))
```

```bash
#NOT a tuple
thistuple = ("apple")
print(type(thistuple))
```

### Tuple Items - Data Types

Tuple items can be of any data type:

### Example
String, int and boolean data types:

```bash
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
```

A tuple can contain different data types:

### Example;
A tuple with strings, integers and boolean values:

tuple1 = ("abc", 34, True, 40, "male")
type()
From Python's perspective, tuples are defined as objects with the data type 'tuple':

### Question:
Using the tuple() method to make a tuple:

```bash
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
```

<br>
<br>
<br>

## Set
Sets are used to store multiple items in a single variable.

Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

A set is a collection which is unordered, unchangeable*, and unindexed.

<br>

* Note: Set items are unchangeable, but you can remove items and add new items.

Sets are written with curly brackets.

### Example

Create a Set:

<br>

```bash
thisset = {"apple", "banana", "cherry"}
print(thisset)
```
Note:<br>
Sets are unordered, so you cannot be sure in which order the items will appear.

Set Items: <br>
Set items are unordered, unchangeable, and do not allow duplicate values.

Unordered: <br>
Unordered means that the items in a set do not have a defined order.

Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

Unchangeable: <br>
Set items are unchangeable, meaning that we cannot change the items after the set has been created.

Once a set is created, you cannot change its items, but you can remove items and add new items.

Duplicates Not Allowed:<br>
Sets cannot have two items with the same value.
<br>

### Example:<br>
Duplicate values will be ignored:

```bash
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
```
Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:

### Example:<br>
True and 1 is considered the same value:

```bash
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)
```

Note: <br>
The values False and 0 are considered the same value in sets, and are treated as duplicates:
<br>

### Example: <br>
False and 0 is considered the same value:

```bash
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)
```

### Example: <br>
String, int and boolean data types:

```bash
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
```

<br>

A set can contain different data types:
<br>

### Example: <br>
A set with strings, integers and boolean values:

```bash
set1 = {"abc", 34, True, 40, "male"}
type()
```
<br>

From Python's perspective, sets are defined as objects with the data type 'set':

### Example: <br>
What is the data type of a set?

```bash
myset = {"apple", "banana", "cherry"}
print(type(myset))
```

<br>
<br>

### The set() Constructor
It is also possible to use the set() constructor to make a set.

<br>

### Example: <br>
Using the set() constructor to make a set:

```bash
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
```
<br>

### Question: <br>
Use the correct method to add multiple items (more_fruits) to the fruits set.

```bash
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
```