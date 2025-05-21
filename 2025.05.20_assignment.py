# 영화관_202510894_박건우.py

age = int(input("나이를 입력하시오:"))
ticket = input("영화표를 구매하셨나요? (Y/N)")
if age >= 16 and ticket == 'Y':
    print("영화관 입장 도와드리겠습니다.")
elif age >= 16 and ticket == 'N':
    price = 20000
    price *= int(input("구매할 티켓의 개수를 입력하세요"))
    print(f"총 금액 {price} 입니다. \n영화관 입장 도와드리겠습니다.")
else: 
    print("영화관 입장이 불가능합니다.")