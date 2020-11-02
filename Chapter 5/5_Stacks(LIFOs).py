# %%
# Last-in, First-out semantics for inserts and deletes
# Don't allow for random access to contents

from queue import LifoQueue  # Last in first out
from collections import deque

# %%
# list - Simple, Built-In Stacks
# Caveat: To get O(1) performance on inserts and deletes,
# New items must be added with append()

s = []
s.append("eat")
s.append("sleep")
s.append("code")

print(s)
s.pop()
print(s)
# %%
# collections.deque - Fast and Robust stacks
# Double ended queue that supports element addition / deletion from either end
# Doubly-linked lists O(n) performance if middle of stack

s = deque()

s.append("eat")
s.append("sleep")
s.append("code")

s
s.pop()

# %%
# queue().LifoQueue - Locking Semantics for Parallel computing

s = LifoQueue()
s.put("eat")
s.put("sleep")
s.put("code")
s.get()

# %%
# Choice comes down to list or collections.deque
# Lists have good O(1) on append and pop, and better O(n) for random access

# collections.deque best choice to implement LIFO queue in Python
# safe and fast general purpose stack
# Could e.g., use a deque to extract data from either side
