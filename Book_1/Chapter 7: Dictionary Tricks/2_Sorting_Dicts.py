# %%

xs = {"a": 1, "b": 3, "c": 2}
sorted(xs.items(), key=lambda x: x[1], reverse=True)

# When creating sorted views of dictionaries you can
# influence the sort order with a key function!
