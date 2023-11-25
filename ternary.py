# If the given number is divisible by 3 or 5, we print True, else we print False

num = int(input("Enter your number: "))

if num == 0:
    print(False)
else:
    if ((num % 3 == 0) or (num % 5 == 0)):
        print(True)
    else:
        print(False)


print(False if num == 0 else True if ((num % 3 == 0) or (num % 5 == 0)) else False)

print(num != 0 and ((num % 3 == 0) or (num % 5 == 0)))
# 0      False and something = False
# 7      True  and (False or False) = True and False = False
# 25     True  and (False or True) = True and True = True