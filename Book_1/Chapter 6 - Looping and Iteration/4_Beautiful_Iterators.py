# %%
#
numbers = [1, 2, 3]
for n in numbers:
    print(n)

# %%
# Writing classes that support the iterator protocol to serve as non-magical examples
# Iterating forever


class Repeater:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return RepeaterIterator(self)


class RepeaterIterator:
    """
    In the init method each RepeaterIterator instance points to a Repeater object
    that created it, holding onto source object. 

    In the __next__ methd we reach back into source and return the value associated 
    with the Repeater
    """

    def __init__(self, source):
        self.source = source

    def __next__(self):
        return self.source.value


repeater = Repeater("Hello")

# %%
# Infinite loop
for item in repeater:
    print(item)


# %%
# Get more info from the class loop

iterator = repeater.__iter__()
for i in range(10):
    item = iterator.__next__()
    print(item)

# Similar to database cursors, we initialize the cursor and prepare for reading
# Never more than one element in-flight so highly memory efficient

# iterator = iter(repeater)
# iter(iterator)
# next(iterator)
# can use iter(iterator)
# %%
# A simple Iterator class


class Repeater:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return self

    def __next__(self):
        return self.value


repeater = Repeater("Hello")

for item in repeater:
    print(item)

# %%
my_list = [1, 2, 3]
iterator = iter(my_list)
print(next(iterator))
print(next(iterator))
print(next(iterator))
next(iterator)  # Raises StopIteration signal as out of values

# %%
# A bounded repeater that raises the exception


class BoundedRepeater:
    def __init__(self, value, max_repeats):
        self.value = value
        self.max_repeats = max_repeats
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.max_repeats:
            raise StopIteration
        self.count += 1
        return self.value


repeater = BoundedRepeater("Hello", 3)
for item in repeater:
    print(item)


# %%
# Iterators provide sequence interface to Python objects
# It's memory efficient and Pythonic (for-in loop)

# To support iteration it needs __iter__ and __next__
