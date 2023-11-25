# Primitive
num_a = 5
num_b = num_a # copied by value
print(num_a, num_b)
num_a = num_a + 2
print(num_a, num_b)

# Complex
list_a = [ 2, 3, 4 ]
list_b = list_a # copied by reference
print(list_a, list_b)
list_a.append(5)
print(list_a, list_b)