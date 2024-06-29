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
x = 
txt[2:5]
```