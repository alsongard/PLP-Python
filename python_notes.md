# data structures in python
there are 2 types of datastructures in python which are:
built in data structures: lists, tuples, dictionaries, set
user-defined data structures: stack, tree, linked list, graphs, stack, hash table, queue


built data structures are refered to as non-primitive data structures, they're classified as objects
### lists
1. accessing elements using indexing and slicing
indexing
```
numbers = [10, 20, 30, 40, 50]
print(numbers[0]) # prints index 0

>>> print(numbers[-1]) # takes the last value
50
```
slicing: in slicing the last value is exclusive(taken)
```
>>> print(numbers[1:3])
[20, 30]

>>> print(numbers[:]) # prints everything
[10, 20, 30, 40, 50]
```

2. appending method
the ``append()`` method is used to append data to a list.  it takes only one argument.
```
numbers.append(70)
```

3. extend method
the ``extend()`` method is used to add items/values in one list to another
```
squares=[4,9,16,25,36,49,64]
numbers.extend(squares)
print(numbers)
```

4. mutability
python list are mutable/their values can be changed.
```
numbers[1] == 100
print(numbers)
```

5. delete
```
languages=["Python", "C++", "C#"]
print(languages)

del languages[1]
```

6. remove()
the ``remove()`` method is used to remove an item from list

```
numbers.remove(64)
```

7. list comprehensions
```
myList = [numbers * numbers for number in range(1,6)]
```


### tuples
``tuples()`` 

tuples are immutable data structures. 
### dictionary
``{key: value}``



``print(dictionary_name)``

to reassign a value we use
``dictionary_name[key] = "value"``

to delete a vlaue in a dictionary use:
``del dictionary_name[key]``

| methods |  use |
| --- | --- |
| any(dictionary) | all(dictionary) | check the truthiness of the keys of a dictionary  |
| len() | returns the length of the number of items in a list |
| sorted() | returns a new sorted dictionary based on the keys |
| clear() | removes all items in the dictionary |
| keys() | returns a new object containing all the keys of the dictionary |
| values() | returns all values in the dictionary | 



in ``all(dictionary)``  returns true if all keys evaluate to true otherwise false
in ``any(dictionary)`` returns true if atleast one key evaluates to true otherwise false.

to delete an entire dictionary use:
```
del dictionary_name
```

### set
a set is a collection of unique values with no order. since items stored in a set have no order, accessing values using an index. 

use the ``set()`` function to create an empty set. 

1. ``add()``
use the ``add()`` function to add a value to a set.
```
value={12,20,24,30}
value.add(34)
print(value)
```

2. ``update()``
the update() method is used to add values from another collection data structure(list) to the tuple.
```
tech_companies=("apple","microsoft","google")
new_tech_companies={"linux","tesla"}
new_tech_companies.update(tech_companies)
new_tech_companies
{'tesla', 'microsoft', 'linux', 'apple', 'google'}
```

3. ``discard()``
to remove an element from a set use the ``discard()``
```
new_tech_companies.discard("linux")
new_tech_companies
{'tesla', 'microsoft', 'apple', 'google'}
```

4. ``enumerate()``
the ``enumerate()`` function is used to return a counter value/index value together with an item/value of iterable data type(list, dictionary)

in dictionaries we use enumerate as follows:
```
my_new_dictionary={1: 'Mercury', 2: 'Venus', 3: 'Earth', 4: 'Mars', 5: 'Jupiter', 6: 'Saturn', 7: 'Uranus'}
>>> for index,(item_index, item_value) in enumerate(my_new_dictionary.items()):
...     print(index,item_value)
...     
0 Mercury
1 Venus
2 Earth
3 Mars
4 Jupiter
5 Saturn
6 Uranus
```

When using ``enumerate()`` function one can set the index value to begin at a certain number.
```
for index,item in enumerate(my_new_dictionary.items(), start=1):
```

5. python set Operations:
python provides built methods  to perform mathematical set operations like union, intersection, subtraction, and symmetric difference.

**union**  
union includes all elements of set A and B
```
myset_a= {10, 2, 3, 4}
myset_b = {10, 20, 30, 40}
new_set = myset_a | myset_b
print(new_set)  # {2, 3, 4, 40, 10, 20, 30}

print(myset_a.union(myset_b))
```

**intersection**  
The intersection of 2 sets, only selects common elements.
```
myset_b={2,4,5,11}
print(myset_b & myset_a) # {2, 5}

# or

print(myset_b.difference(myset_a))
```

d