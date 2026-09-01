# Tuples and Lists

# In Python, tuples can contain different types (strings, ints, floats), 
# but the variable itself is of type tuple.
tuple1 = ('disco', 10, 1, 2)
print(type(tuple1))  # Outputs: <class 'tuple'>

# Indexing
tuple1 = ("disco", 10, 1, 2)
# tuple1[0] -> "disco"
# tuple1[-3] -> 10

# Tuple Concatenation
tuple2 = tuple1 + ("hard rock", 10)
# Result: ("disco", 10, 1, 2, "hard rock", 10)

# Slicing
# tuple2[0:3] -> ('disco', 10, 1)

# Tuple Length & Sorting
# Tuples are immutable (cannot be modified in-place)
Ratings = (10, 9, 6, 5, 10, 8, 9)
RatingsSorted = sorted(Ratings)  # sorted() returns a new sorted list

# Converting string to list via split()
split_list = "hard rock".split()
print(split_list)  # Outputs: ['hard', 'rock']