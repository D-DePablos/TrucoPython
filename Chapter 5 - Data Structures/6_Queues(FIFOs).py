# %%
""" 
A queue is a collection of objects that supports fast first in first-out 
inserts and deletes. ENqueue and DEqueue are usually the names for these operations

Think of it as a pipe. New items are put at one end and push the other end to come out

Similar to stacks but you remove the item least recently added in (first in)

Should take O(1) time for any inserts / deletes    
"""

# %%
# List: very slow queues

from multiprocessing import Queue
from queue import Queue
from collections import deque
q = []
q.append("eat")
q.append("sleep")
q.append("code")

q

q.pop(0)

# %%
# collections.deque : Fast and robust double ended queues

q = deque()

q.append("eat")
q.append("sleep")
q.append("code")

print(q.popleft())
print(q.popleft())
print(q.popleft())
print(q.popleft())
# %%
# queue.Queue -> Locking semantics for parallel computing

"""
This queue implementation is synchronised and provides locking semantics 
to support multiple concurrent producers / consumers
"""

q = Queue()

q.put("eat")
q.put("sleep")
q.put("code")

print(q.get())
print(q.get())
print(q.get())
# q.get_nowait()  # If getting ~ last element, necessary for no crash

# %%
# multiprocessing.Queue - Shared job queues

# Can store and transfer any pickle-able object across process boundaries

q = Queue()

q.put("eat")
q.put("sleep")
q.put("code")

print(q.get())
print(q.get())
print(q.get())
# %%
"""
If not looking for parallel processing support, collections.deque is good
Otherwise multiprocessing or queue
"""
