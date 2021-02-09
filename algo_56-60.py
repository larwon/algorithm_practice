# algo_56
# num = 1
# sum = 0
# while num < 101:
#     if (num % 2 == 0):
#         sum = sum + num
#     num = num + 1
# print(sum)


# algo_57
# sub = 1
# sum = 0
# while sub < 6:
#     score = int(input("점수를 입력해주세요:  "))
#     if (0 <= score) and (score <= 100):
#         sum = sum + score
#         sub = sub + 1
#         print(score)
#     else:
#         print("sorry")
# print(sum)
# print(sum/5)


# algo_58
# sum = 0
# count = 0
# while True:
#     num = int(input("숫자를 입력해주세요:  "))
#     if sum <= 1000:
#         sum = sum + num
#         count = count + 1
#     else:
#         break
# print(sum)
# print(sum/count)


# algo_59
# num = int(input("숫자를 입력해주세요:  "))
# for i in range(2,int(num/2)):
#     if num % i == 0:
#         print("소수가 아닙니다")
#         break
# else:
#     print("소수입니다")


# algo_60
# def findmax(a, b, c):
#     if a > b:
#         big = a
#     else:
#         big = b
#     if big < c:
#         big = c
#     return big


# a = int(input("첫번째 숫자를 입력해주세요:  "))
# b = int(input("두번째 숫자를 입력해주세요:  "))
# c = int(input("세번째 숫자를 입력해주세요:  "))
# big = findmax(a, b, c)
# print(big)