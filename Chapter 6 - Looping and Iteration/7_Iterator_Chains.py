# %% Iterators generate a stream of values over their lifetime

def integers():
    for i in range(1, 9):
        yield i


chain = integers()
list(chain)

# %% Chaining


def squared(seq):
    for i in seq:
        yield i*i


chain = squared(integers())
list(chain)
"""
This architecture is similar to UNIX. We chain a sequence of processes 
such that the output of each one feeds the next
"""

# %% Negate values


def negated(seq):
    for i in seq:
        yield -i


chain = negated(squared(integers()))
list(chain)


# %% Alternative using generator expressions

integers = range(8)
squared = (i*i for i in integers)
negated = (-i for i in squared)

list(negated)

# Downside is they can only be used once, compared to generator functions

# %% Key Takeaways
"""
- Generators chained together to form efficient + Maintainable data processing pipelines
- Chained generators process each element individually
- Generator expressions are more concise which can be good if readable
"""
