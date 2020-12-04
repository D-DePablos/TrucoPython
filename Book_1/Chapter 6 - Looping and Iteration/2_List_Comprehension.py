# %%
# Just for-loops with terse and compact syntax

squares = [x * x for x in range(10)]
print(squares)

# values = [expression for item in collection]

even_squares = [x*x for x in range(10) if x % 2 == 0]
print(even_squares)

# %%
# Set comprehension

{x * x for x in range(-9, 10)}
# %%
# They are actually just syntactic sugar for simple for loops
