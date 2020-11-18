# %%
# Extension of square-brackets syntax

lst = [i for i in range(1, 6)]
print(lst)

# lst[start:end:step]
lst[1:3:1]

# %%
# Create a sublist that contains every other element

lst[::2]
# : the sushi operator
# %%
lst[::-1]  # Reverse
# %%
# Use the Sushi operator to delete all elements within the list without deleting object itself
lst = [1, 2, 3, 4, 5]
del lst[:]
lst

# %%
original_lst = lst
lst[:] = [7, 8, 9]
lst

# original_lst
# %%
copied_lst = lst[:]
copied_lst is lst  # False: Is a shallow copy
