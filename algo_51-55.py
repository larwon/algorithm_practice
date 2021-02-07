# algo_51
# num = int(input("숫자를 입력해주세요:  "))
# for i in range(1,10):
#     mul = num * i
#     print(mul)


# algo_52
# num = int(input("숫자를 입력해주세요:  "))
# sum = 1
# for i in range(num,0,-1):
#     sum = sum * i
# print(sum)


# algo_53
# i = 2
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i * j)
#         j = j + 1
#     i = i + 1


# algo_53-1      #파이썬 작성
# i = 2
# j = 1
# for i in range(2,10):
#     for j in range(1,10):
#         print(i * j)
#         j = j + 1
#     i = i + 1


#algo_53-2      #파이썬 작성 
# i = 2
# j = 1
# while i < 10:
#     for j in range(1,10):
#         print(i * j)
#         j = j + 1
#     i = i + 1


# algo_54
# for i in range(1,6):
#     for j in range(1,6):
#         print((i*10 + j), end="")
#     print()   


# algo_55
# num = int(input("숫자를 입력해주세요:  "))
# i = 1
# while i <= num:
#     j = i * "*"
#     print(j)
#     i = i + 1