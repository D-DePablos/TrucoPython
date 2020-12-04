# %% get method that allows for a fallback value

name_for_userid = {
    382: "Alice",
    950: "Bob",
}


def greeting(userid):

    if userid in name_for_userid:
        return "Hi %s" % name_for_userid[userid]

    else:
        return "Hi there"


print(greeting(382))
print(greeting(20000))

"""
This approach is inneficient: Queries dict twice!
It is verbose
Not even Pythonic: Ask for forgiveness not permission
"""


def improved_greeting(userid):
    """
    Avoids the key in dict check
    Easier ask forgiveness than permission
    """
    try:
        return f"Hi {name_for_userid[userid]}"
    except KeyError:
        return "Hi there"
