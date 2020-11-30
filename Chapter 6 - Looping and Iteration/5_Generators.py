# %%
# Generators are simplified Iterators

def bounded_repeater(value, max_repeats):
    for i in range(max_repeats):
        yield value


for x in bounded_repeater("Hi", 4):
    print(x)
# Yield statement allows you to suspend execution of a generator function
# to pass back values from it.
