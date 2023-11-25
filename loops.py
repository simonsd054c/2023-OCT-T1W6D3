# print(1)
# print(2)
# print(3)
# print(4)
# print(5)

# # While loop
# number = 1
# while number <= 5:
#     print(number)
#     number += 1 # number = number + 1        number++



login_attempts = 5
while login_attempts > 0:
    password = input("Enter password: ")
    if (password != "hello"):
        print("Wrong Password!!!!")
        login_attempts -= 1
        print(f"Remaining attempts: {login_attempts}")
    else:
        print("Right Password!!")
        break # it breaks the loop when it is executed