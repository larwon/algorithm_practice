# algo_46
# num = int(input("숫자를 입력해주세요:  "))
# count = 1
# sum = 0
# while count <= num:
#     sum = sum + count
#     count = count + 1
# print(sum)
    

# algo_47
# num = int(input("숫자를 입력해주세요:  "))
# i = 1
# while i < 10:
#     mul = num * i
#     i = i + 1
#     print(mul)


# algo_48
# num1 = int(input("첫번째 숫자를 입력해주세요:  "))
# num2 = int(input("두번째 숫자를 입력해주세요:  "))
# if num1 > num2:
#     i = num2
#     sum = 0
#     while i <= num1:
#         sum = sum + i
#         i = i + 1
#     print(sum)
# elif num1 == num2:
#     print(num1 + num2)
# else:
#     i = num1
#     sum = 0
#     while i <= num2:
#         sum = sum + i
#         i = i + 1
#     print(sum)


# algo_48-1      #파이썬만 작성
# num = int(input("숫자를 입력해주세요:  "))
# i = 1
# mul = 0
# while (i <= num):
#     i = i + 1
#     if (i % 3) != 0:
#         continue
#     mul = mul + i
# print(mul)


# algo_49
# i = 1
# sum = 0
# for i in range(1,101,2):
#     sum = sum + i
# print(sum)


# algo_50
# num = int(input("숫자를 입력해주세요:  "))
# i = 1
# sum = 0
# for i in range(num,1001,num):
#     sum = sum + i
# print(sum)