# Factorial

# 6! = 6 * 5 * 4 * 3 * 2 * 1

num = 5
factorial_value = 1

for i in range(1, num + 1): # 1, 2, 3, 4, 5
    factorial_value *= i # 1 * 1 = 1, 1 * 2 = 2, 2 * 3 = 6, 6 * 4 = 24, 24 * 5 = 120

print(factorial_value)