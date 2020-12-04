# %%  Generator expression base
iterator = ("Hello" for i in range(3))
for x in iterator:
    print(x)

# %% Generator Expressions versus List Comprehensions
listcomp = ["Hello" for i in range(3)]
genexpr = ("Hello" for i in range(3))

# One can be easily printed out
print(listcomp)
print(genexpr)
# Can make a generator expression into a list but lose efficiency
print(list(genexpr))
# genexpr = (expression for item in collection)

# %% Filtering values
# genexpr = (expression for item in collection if condition)
even_squares = (x*x for x in range(10) if x % 2 == 0)
list(even_squares)

# %% In-line generation expressions
for x in ("Bom dia" for i in range(3)):  # Returns a BOM dia
    print(x)

print(sum(x*2 for x in range(10)))

# %% Too much of a good thing?
"""
Don't write deeply nested generator expressions
"""

# %% Takeaways
"""
- Generator expressions ~ List comprehensions
- Once a generator expression has been consumed, it can't be restarted or reused
- Are best for "ad hoc" iterators. 
- For complex iterators, use class-based iterations!
"""
