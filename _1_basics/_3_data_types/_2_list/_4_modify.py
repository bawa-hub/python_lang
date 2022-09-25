# Correcting mistake values in a list
odd = [2, 4, 6, 8]

# change the 1st item    
odd[0] = 1       

print(odd) # [1, 4, 6, 8]

# change 2nd to 4th items
odd[1:4] = [3, 5, 7]  

print(odd) # [1, 3, 5, 7]          


# add one item to a list using the append() method 
# or add several items using the extend() method.

# Appending and Extending lists in Python
odd = [1, 3, 5]

odd.append(7)

print(odd) # [1, 3, 5, 7]

odd.extend([9, 11, 13])

print(odd) # [1, 3, 5, 7, 9, 11, 13]


# Concatenating and repeating lists
odd = [1, 3, 5]
print(odd + [9, 7, 5]) # [1, 3, 5, 9, 7, 5]
print(["re"] * 3) # ['re', 're', 're']


# Demonstration of list insert() method
odd = [1, 9]
odd.insert(1,3)

print(odd) # [1, 3, 9]

odd[2:2] = [5, 7]

print(odd) # [1, 3, 5, 7, 9]