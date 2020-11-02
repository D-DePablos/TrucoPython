# %%
# Sets and multisets
# A set data structure is an unordered collection of objects without duplicates
# Good for test of membership to set, insert or delete values, and compute union or intersection

# Membership tests expected to be O(1). Union, intersection, etc. Are O(n)

from collections import Counter

vowels = {"a", "e", "i", "o", "u"}
squares = {x * x for x in range(10)}


# Set: your go to Set
"e" in vowels

letters = set("Alice")
print(letters.intersection(vowels))

vowels.add("x")


# %%
# Frozenset - Immutable sets
# Cannot be changed after having been constructed

vowels = frozenset({"a", "e", "i", "o", "u"})
vowels.add("p")

# Frozensets are hashable and can be used as dictionary keys
# %%
# Collections.Counter: "Bag" data structures
inventory = Counter()

loot = {"sword": 1, "bread": 3}
inventory.update(loot)
print(inventory)

loot_2 = {"sword": 1, "apple": 2}
inventory.update(loot_2)
print(inventory)

print(len(inventory), sum(inventory.values()))  # Unique items and total
