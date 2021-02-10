# algo_61
# def input_data():
#     num1 = int(input("첫번째 숫자를 입력해주세요:  "))
#     num2 = int(input("두번째 숫자를 입력해주세요:  "))
#     output_data(num1, num2)

# def output_data(x, y):
#     print(x + y)
#     print(x - y)
#     print(x * y)
#     print(x / y)

# input_data()


# algo_62
# def findPrime(x, y):
#     print(x, y)
#     count = 0

#     for i in range(x, y+1):
#         for j in range(2, int(x/2)):
        
#             if (i % j == 0):
#                 break
#         else:
#             print(i)
#             count = count + 1
#     else:
#         print()
#     return count

# num1 = int(input("첫번째 숫자를 입력해주세요:  "))
# num2 = int(input("두번째 숫자를 입력해주세요:  "))
# count = findPrime(num1, num2)
# print(count)