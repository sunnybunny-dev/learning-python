# Day 2: Tuples, Lists, & Basic Methods

## 1. Tuples
Tuples are **ordered** and **immutable** (cannot be changed after creation) sequences in Python.

### Creating & Checking Type
In python
tuple1 = ("disco", 10, 1, 2)
print(type(tuple1))  

Indexing & Slicing
Zero-based Indexing: tuple1[0]"disco"
Negative Indexing: tuple1[-1] 2 (last element)
Slicing: sequence[start:stop] (includes start, excludes stop)
tuple1[0:2]("disco", 10)

Operations & Methods

tuple2 = tuple1 + ("hard rock", 10)

Length (len()): Returns the number of items.
len(tuple1)  # 4

Sorting (sorted()): Returns a new sorted list (does not modify the original tuple).
ratings = (10, 9, 6, 5, 8)
ratings_sorted = sorted(ratings)  # [5, 8, 9, 10]

2. Lists
Lists are ordered and mutable (can be changed) sequences in Python.

list1 = [1, 2, ["a", "b"], 3]
append(item): Adds the argument as a single element at the end.
A = [1]
A.append([2, 3])  # A becomes [1, [2, 3]] -> len(A) is 2
extend(iterable): Concatenates each element of the argument individually.
A = [1]
A.extend([2, 3])  # A becomes [1, 2, 3] -> len(A) is 3

3. String Methods
.split(separator): Splits a string into a list of substrings.

"hard rock".split()  # ['hard', 'rock']
"A,B,C,D".split(",")  # ['A', 'B', 'C', 'D']