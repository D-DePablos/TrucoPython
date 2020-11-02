"""
# Array Data Structures
- Fixed-size data records
- Allow elements to be located based on index
- Contiguous data structures (information stored in adjoining blocks of memory)
- Constant 0(1) access time for this case
"""

# %%
# LIST: mutable dynamic arrays
# Issues with storage space
import array
arr = ["one", "two", "three"]
del arr[1]
arr.append(23)
print(arr)


# %%
# TUPLE - immutable containers
# All elements in a tuple must be defined at creation time
# Also have flexibility wrt. data types contained
arr = ("one", "two", "three")

# arr[1] = "hello"  # TypeError: 'tuple' object does not support item assignment
# del arr[1]  # TypeError: Does not support item deletion

arr + (23, )


# %%
# ARRAY: Basic Types arrays
# Space efficient storage of data types like bytes, 32 bit int, floats, and so on
# Mutable and behave like lists, but are constrained to one data type
# Useful if you need to store many elements of the same type


arr = array.array("f", (1.0, 1.5, 2.0, 2.5))
arr.append(23)
arr

# %%
# STR - unicode characters, immutable arrays
# Python 3.x uses str objects to store textual data
# Space efficient because the yspecialize in a single data type
# Closest equivalent to mutable string is a storing individual characters in a list

"".join(list("abc"))

# Each of the characters within a string is another string

# %%
# BYTES - Immutable arrays of single bytes
# Integers 0 <= x <= 255
arr = bytes((0, 1, 2, 3))
arr[1]

# arr[1] = 23 # TypeError: 'bytes' object does not support item assignment


# %%

# BYTEARRAY - Mutable Arrays of Single Bytes
# Related to bytes byt can be modified freely

arr = bytearray((0, 1, 2, 3))
arr[1] = 23
print(arr)
arr.append(42)
print(arr)
# %%
# TAKEAWAYS

# Arbitrary objects, mixed data types -> Lists or Tuples
# Numeric data, tight pacling and performance -> array.array
# Unicode textual data -? str; otherwise list of characters
# bytes -> bytes

# Maybe start with a list and upgrade over time if performance becomes important
