# %%
# Lists: Manually sorted queue
from queue import PriorityQueue
import heapq
q = []

q.append((2, "code"))
q.append((1, "eat"))
q.append((3, "sleep"))

q.sort(reverse=True)

while q:
    next_item = q.pop()
    print(next_item)

# %%

# heapq - List-based binary heaps -> Integration and extraction of smallest element

q = []

heapq.heappush(q, (2, "code"))
heapq.heappush(q, (1, "eat"))
heapq.heappush(q, (3, "sleep"))

while q:
    next_item = heapq.heappop(q)
    print(next_item)
# %%
# queue.PriorityQueue -> Beautiful
# Synchronised and provides locking semantics for multiproc
# Might be useful or just slow down program

q = PriorityQueue()
q.put((2, "code"))
q.put((1, "eat"))
q.put((3, "sleep"))

while not q.empty():
    next_item = q.get()
    print(next_item)

# If you would like to avoid overhead from PriorityQ use heapq
