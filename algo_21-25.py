# algo_21
# num = int(input("숫자를 입력해주세요:  "))
# if num % 2 == 0:
#     print("짝수입니다")
# else:
#     print("홀수입니다")


# algo_22
# count = int(input("상품 개수를 입력해주세요:  "))
# price = int(input("돈을 입력해주세요:  "))
# if count >= 20:
#     discount1 = (price*count) - ((price*count)*0.2)
#     print(discount1)
# elif count >=10:
#     discount2 = (price*count) - ((price*count)*0.1)
#     print(discount2)
# else:
#     basic = price*count
#     print(basic)


# algo_23
# weight = int(input("몸무게를 입력하세요:  "))
# height = int(input("키를 입력하세요:  "))
# gender = input("남성(m)입니까> 여성(f)입니까?:  ")
# if gender == "m":
#     basic1 = height-100
#     if ((weight) >= (basic1 -5)) and ((weight) <= (basic1 +5)):
#         print("표준입니다")
#     elif ((weight) < (basic1+5)):
#         print("비만입니다")
#     else:
#         print("약체입니다")
# else:
#     basic2 = height-105
#     if ((weight) >= (basic2 -5)) and ((weight) <= (basic2 +5)):
#         print("표준입니다")
#     elif ((weight) > (basic2+5)):
#         print("비만입니다")
#     else:
#         print("약체입니다")


# algo_24
# grade = int(input("학년을 입력해주세요:  "))
# avg = float(input("학점을 입력해주세요:  "))
# if (grade == 4) and (avg >= 4.5):
#     print("A입니다")
# else:
#     print("죄송합니다")


# algo_25
# sub1 = int(input("첫번째 과목의 점수를 입력해주세요:  "))
# sub2 = int(input("두번째 과목의 점수를 입력해주세요:  "))
# if (sub1 >= 90) and (sub2 >= 90):
#     print("훌륭합니다")
# else:
#     print("분발하세요")