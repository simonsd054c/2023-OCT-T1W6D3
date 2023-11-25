# HCF = Highest Common Factor
# GCD = Greatest Common Divisor

# hcf of 12 and 8

# 12 = 2, 3 , 4, 5*, 6 , 7*, 8*
# 8  = 2, 3*, 4, 5*, 6*, 7*, 8

# hcf = 4

num1 = 12
num2 = 24

hcf = 1

smaller_num = num1 # 12

if(num2 < num1): # 8 < 12 = True
    smaller_num = num2 # 8

for i in range(2, smaller_num + 1):
    if (num1 % i == 0) and (num2 % i == 0):
        hcf = i

print(hcf)
