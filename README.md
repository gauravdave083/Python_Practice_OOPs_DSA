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

# Loops

In programming, a **loop** means repeating something multiple times.
There are different kinds of loops:

- [While loops](#while-loops) repeat something while a condition is true.
- [Until loops](#until-loops) repeat something while a condition is false.
- [For loops](#for-loops) repeat something for each element of something.

We'll talk about all of these in this tutorial.

## While loops

Now we know how if statements work.

```python
its_raining = True
if its_raining:
    print("Oh crap, it's raining!")
```

While loops are really similar to if statements.

```python
its_raining = True
while its_raining:
    print("Oh crap, it's raining!")
    # we'll jump back to the line with the word "while" from here
print("It's not raining anymore.")
```

If you're not familiar with while loops, the program's output may be a
bit surprising:

    Oh crap, it's raining!
    Oh crap, it's raining!
    Oh crap, it's raining!
    Oh crap, it's raining!
    Oh crap, it's raining!
    Oh crap, it's raining!
    Oh crap, it's raining!
    Oh crap, it's raining!
    Oh crap, it's raining!
    Oh crap, it's raining!
    Oh crap, it's raining!
    Oh crap, it's raining!
    Oh crap, it's raining!
    Oh crap, it's raining!
    Oh crap, it's raining!
    (much more raining)

Again, this program does not break your computer. It just prints the
same thing multiple times. We can interrupt it by pressing Ctrl+C.

In this example, `its_raining` was the **condition**. If something in
the while loop would have set `its_raining` to False, the loop would
have ended and the program would have printed `It's not raining anymore`.

Let's actually create a program that does just that:

```python
its_raining = True
while its_raining:
    print("It's raining!")
    answer = input("Or is it? (y=yes, n=no) ")
    if answer == 'y':
        print("Oh well...")
    elif answer == 'n':
        its_raining = False     # end the while loop
    else:
        print("Enter y or n next time.")
print("It's not raining anymore.")
```

Running the program may look like this:

    It's raining!
    Or is it? (y=yes, n=no) i dunno
    Enter y or n next time.
    It's raining!
    Or is it? (y=yes, n=no) y
    Oh well...
    It's raining!
    Or is it? (y=yes, n=no) n
    It's not raining anymore.

The while loop doesn't check the condition all the time, it only checks
it in the beginning.

```python
>>> its_raining = True
>>> while its_raining:
...     its_raining = False
...     print("It's not raining, but the while loop doesn't know it yet.")
...
It's not raining, but the while loop doesn't know it yet.
>>>
```

We can also interrupt a loop even if the condition is still true using
the `break` keyword. In this case, we'll set condition to True and rely
on nothing but `break` to end the loop.

```python
while True:
    answer = input("Is it raining? (y=yes, n=no) ")
    if answer == 'y':
        print("It's raining!")
    elif answer == 'n':
        print("It's not raining anymore.")
        break   # end the loop
    else:
        print("Enter y or n.")
```

The program works like this:

    Is it raining? (y=yes, n=no) who knows
    Enter y or n.
    Is it raining? (y=yes, n=no) y
    It's raining!
    Is it raining? (y=yes, n=no) n
    It's not raining anymore.

Unlike setting the condition to False, breaking the loop ends it
immediately.

```python
>>> while True:
...     break
...     print("This is never printed.")
...
>>>
```

## Until loops

Python doesn't have until loops. If we need an until loop, we can use
`while not`:

```python
raining = False
while not raining:
    print("It's not raining.")
    if input("Is it raining? (y/n) ") == 'y':
        raining = True
print("It's raining!")
```

## For loops

Let's say we have [a list](lists-and-tuples.md) of things we want to
print. To print each item in it, we could just do a bunch of prints:

```python
stuff = ['hello', 'hi', 'how are you doing', 'im fine', 'how about you']

print(stuff[0])
print(stuff[1])
print(stuff[2])
print(stuff[3])
print(stuff[4])
```

The output of the program is like this:

    hello
    hi
    how are you doing
    im fine
    how about you

But this is only going to print five items, so if we add something to
stuff, it's not going to be printed. Or if we remove something from
stuff, we'll get an error saying "list index out of range".

We could also create an index variable, and use a while loop:

```python
>>> stuff = ['hello', 'hi', 'how are you doing', 'im fine', 'how about you']
>>> length_of_stuff = len(stuff)
>>> index = 0
>>> while index < length_of_stuff:
...     print(stuff[index])
...     index += 1
...
hello
hi
how are you doing
im fine
how about you
>>>
```

But we have `len()` and an index variable we need to increment and a
while loop and many other things to worry about. That's a lot of work
just for printing each item.

This is when for loops come in:

```python
>>> for thing in stuff:
...     # this is repeated for each element of stuff, that is, first
...     # for stuff[0], then for stuff[1], etc.
...     print(thing)
...
hello
hi
how are you doing
im fine
how about you
>>>
```

Without the comments, that's only two simple lines, and one variable.
Much better than anything else we tried before.

```python
>>> for thing in stuff:
...     print(thing)
...
hello
hi
how are you doing
im fine
how about you
>>>
```

Note that `for thing in stuff:` is not same as `for (thing in stuff):`.
Here the `in` keyword is just a part of the for loop and it has a
different meaning than it would have if we had `thing in stuff` without
a `for`. Trying to do `for (thing in stuff):` creates an error.

Right now the while loop version might seem easier to understand for
you, but later you'll realize that for loops are much easier to work
with than while loops and index variables, especially in large projects.
For looping is also a little bit faster than while looping with an index
variable.

For loops are not actually limited to lists. We can for loop over many
other things also, including strings and
[tuples](lists-and-tuples.md#tuples). For looping over a tuple gives us
its items, and for looping over a string gives us its characters as
strings of length one.

```python
>>> for short_string in 'abc':
...     print(short_string)
...
a
b
c
>>> for item in (1, 2, 3):
...     print(item)
...
1
2
3
>>>
```

If we can for loop over something, then that something is **iterable**.
Lists, tuples and strings are all iterable.

There's only one big limitation with for looping over lists. We
shouldn't modify the list in the for loop. If we do, the results can
be surprising:

```python
>>> stuff = ['hello', 'hi', 'how are you doing', 'im fine', 'how about you']
>>> for thing in stuff:
...     stuff.remove(thing)
...
>>> stuff
['hi', 'im fine']
>>>
```

Instead, we can create a copy of stuff and loop over it.

```python
>>> stuff = ['hello', 'hi', 'how are you doing', 'im fine', 'how about you']
>>> for thing in stuff.copy():
...     stuff.remove(thing)
...
>>> stuff
[]
>>>
```

Or if we just want to clear a list, we can use the `clear`
[list method](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists):

```python
>>> stuff = ['hello', 'hi', 'how are you doing', 'im fine', 'how about you']
>>> stuff.clear()
>>> stuff
[]
>>>
```

## Summary

- A loop means repeating something multiple times.
- While loops repeat something as long as a condition is true, and
    they check the condition only in the beginning.
- For loops can be used for repeating something to each item in a list.
- An iterable is something that can be for looped over.
- The `break` keyword can be used to interrupt the innermost loop at
    any time.

## Examples

Repeat something an endless amount of times.

```python
message = input("What do you want me to say? ")
while True:
    print(message, "!!!")
```

Ask the user to enter five things and print them.

```python
things = []

print("Enter 5 things: ")
while len(things) < 5:
    thing = input("> ")
    things.append(thing)

print("You entered these things:")
for thing in things:
    print(thing)
```

Ask the user a bunch of questions.

```python
questions_and_answers = [
    # [question, answer], ...
    ["What is 2+4? ", "6"],
    ["What is 2-4? ", "-2"],
    ["What is 2*4? ", "8"],
    ["What is 2/4? ", "0.5"],
    # You could add more questions, but the code that asks them
    # wouldn't need to be changed in any way.
]

for qa in questions_and_answers:
    while True:
        if input(qa[0]) == qa[1]:
            print("Correct!")
            break
        else:
            print("That's not what I was thinking of... Try again.")
```

Store a list of names and let the user check if the program knows
the user.

```python
# You can add names here so the program will know them automatically
# when it starts.
namelist = []

print("Options:")
print("  0      Quit")
print("  1      Check if I know you")
print("  2      Introduce yourself to me")
print("  3      Make me forget you")
print("  4      Print a list of people I know")
print()     # print an empty line

while True:
    option = input("Choose an option: ")

    # Things like option == 0 don't work because option is a string
    # and it needs to be compared with a string:
    #   >>> 0 == 0
    #   True
    #   >>> '0' == '0'
    #   True
    #   >>> 0 == '0'
    #   False
    if option == '0':
        print("Bye!")
        break

    elif option == '1':
        name = input("Enter your name: ")
        if name in namelist:
            print("I know you! :D")
        else:
            print("I don't know you :/")

    elif option == '2':
        name = input("Enter your name: ")
        if name in namelist:
            print("I knew you already.")
        else:
            namelist.append(name)
            print("Now I know you!")

    elif option == '3':
        name = input("Enter your name: ")
        if name in namelist:
            namelist.remove(name)
            print("Now I don't know you.")
        else:
            print("I didn't know you to begin with.")

    elif option == '4':
        if namelist == []:
            print("I don't know anybody yet.")
        else:
            for name in namelist:
                print(f"I know {name}!")

    else:
        print("I don't understand :(")

    print()
```


