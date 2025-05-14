# 학점계산_202510894_박건우.py

print("평균 학점을 계산해드립니다.")

math = int(input("수학 점수 입력: "))
eng = int(input("영어 점수 입력: "))
kor = int(input("국어 점수 입력: "))
sci = int(input("과학 점수 입력: "))

print("평균 학점은", (math+eng+kor+sci)/4 , "입니다.")