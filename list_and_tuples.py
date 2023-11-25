# Primitive Data Types - can hold a single piece of data
# Numbers (int, float), String, Boolean
# a = 501
# a = "String"
# a = True

# Complex Data Types - can multiple pieces of data
# List - Array - collection of data - mutable (changed) - indexed
# numbers = [ 15, 2, 23, 98, 56 ]
# #           0   1  2    3   4
# print(numbers)
# print(numbers[2])
# numbers[2] = 10
# print(numbers)
# # List methods
# print(len(numbers))
# numbers.append(42)
# print(numbers)
# numbers.insert(2, 72)
# print(numbers)
# numbers.pop()
# print(numbers)
# numbers.remove(98)
# print(numbers)
# numbers.pop(1)
# print(numbers)
# numbers.sort()
# print(numbers)
# numbers.reverse()
# print(numbers)

# new_numbers = [ 13, 45, 62, 13, 45, 13 ]

# print(new_numbers.count(13))
# print(new_numbers.index(62))
# print(new_numbers.index(45))

# print(numbers + new_numbers)



# Tuples - similar to list - collection of data - indexed - immutable
names = ( "John", "Jane", "Mike" )
#           0        1       2
print(names)
print(type(names))

# names.append("One more name") - Cannot do this because append in mutating method
# but tuple is immutable

print(names.count("John"))
print(names.index("Mike"))
print(len(names))
print(names[2])
# names[2] = "Changed Mike" - Cannot do this

# Use cases
days_of_the_week = ("Monday", "Tuesday", "Wednesday")
months = ( "January", "February", "March" )
coordinate_of_my_house = (-67.23, 72.12)