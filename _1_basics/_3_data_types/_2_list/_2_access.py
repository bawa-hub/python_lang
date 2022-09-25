# List Index

my_list = ['p', 'r', 'o', 'b', 'e']
# first item
print(my_list[0])  # p
# third item
print(my_list[2])  # o
# fifth item
print(my_list[4])  # e
# Error! Only integer can be used for indexing
print(my_list[4.0])

# Nested List
n_list = ["Happy", [2, 0, 1, 5]]
# Nested indexing
print(n_list[0][1])
print(n_list[1][3])


# Negative indexing

# last item
print(my_list[-1]) # e
# fifth last item
print(my_list[-5]) # p