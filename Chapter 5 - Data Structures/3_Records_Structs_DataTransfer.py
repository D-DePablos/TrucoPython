# Record data structures provide a fixed number of fields.
# Each field may have a name and a different type

# Best Named Tuples
from types import SimpleNamespace
from struct import Struct
from typing import NamedTuple
from collections import namedtuple

# %%
# Dictionaries: Simple data objects
"""
    - Arbitrary # of Objects
    - Often called maps or associative arrays
    - Lookup, insertion, deletion of obj with a given key
"""

car1 = {
    "color": "red",
    "mileage": 3800,
    "automatic": True,
}

car2 = {
    "color": "blue",
    "mileage": 1700,
    "automatic": False,
}

car2["mileage"] = 12

# Issues with typos ...
car3 = {
    "colr": "blue",
    "mileage": 1700,
    "windshield": "broken",
}

# %%
# Tuples - Immutable groups of Objects
# Cannot be modified once created
# Take up slightly less memory than lists in Cpython
# Faster to construct than lists

# Downside: Must access through index

# Fields: color, mileage, automatic
car1 = ("red", 2800, True)
car2 = ("blue", 2+3, True)
# No protection against missing or extra fields
car3 = (4534, "green", True, "silver")

# %%
# Writing a Custom class
# More work, more control

# Use as blueprints for data objects


class Car:
    def __init__(self, color, mileage, automatic):
        """
        :param color, mileage, automatic
        """
        self.color = color
        self.mileage = mileage
        self.automatic = automatic

    def __repr__(self) -> str:
        return(f"{self.color.capitalize()} car, {self.mileage} km")


car1 = Car("red", 1200, True)
car1

# %%
# collections.namedtuple -> Convenient Data Objects
p1 = namedtuple(
    "Point", "x y z"
)
p1(1, 2, 3)

# Much more useful representation
Car = namedtuple("Car", "color mileage automatic")
car1 = Car("blue", 1200, True)
car1

# %%
# typing.NamedTuple - Improved Namedtuples
# FAR BETTER


class Car(NamedTuple):
    color: str
    mileage: float
    automatic: bool


car1 = Car("red", 3800, True)
car1

# %%
# struct.Struct - Serialized C Structs
# Can be used to handle binary data stored in files or from network connections
# Normally used as data exchange formats


MyStruct = Struct("i?f")
data = MyStruct.pack(23, False, 42.0)

print(data)

print(MyStruct.unpack(data))

# %%
# types.SimpleNamespace -> Fancy attribute access
# Glorified dictionary with access and nice prints

car1 = SimpleNamespace(color="red", mileage=3812.4, automatic=True)
car1
car1.mileage
del car1.automatic
car1
# %%
# KEY TAKEAWAYS
# Decision depends on use case

"""
    - Only 2/3 fields: plain tuple
    - Immutable fields necessary: typing.NamedTuple
    - Lock down field names to avoid typos: typic.NamedTuple
    - Simple: Simple dictionary ~ JSON
    - Full control over data structure: Class with @property setters and getters
    - Need methods on the object: Custom class, extend typing.NamedTuple
    - To pack data tightly and send to disk or over the network: struct.Struct
"""
