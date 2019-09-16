### 자료형 ###

# 정수형
a = 123
a = -178
a = 0
print(a)

# 실수형
b = 1.2
b = -3.45
print(b)

# 지수 표현 방식(e나 E모두 상관없음)
c = 4.24E10
print(c)
d = 4.24e-10 * 10
print(d)

# 8진수 : 0o 또는 0O로 시작
e = 0o177
print(e) # 출력결과 : 127 

# 16진수 : 0x로 시작
f = 0x8ff
print(f) # 출력결과 : 2303
f = 0xABC
print(f) # 출력결과 : 2748

# 복소수 : j 또는 J 사용
a = 1 + 2j
print(a) # 출력결과 : (1+2j)
# 복소수 내장 함수
#  .real : 실수부분 리턴
a.real
#  .imag : 허수부분 리턴
a.imag
#  .conjugate() : 켤레복소수 리턴
a.conjugate() 
#  abs(복소수) : 복소수 절대값 리턴
abs(a)

"""
사칙연산
"""

# 사칙연산( + , - , * , / )
a = 3
b = 4
print(a/b) #출력결과 : 0.75 ----> 자바와 달리 소수점까지 출력(python 2.7ver. 경우 정수만 출력)

# ** 연산자
a ** b #결과 : 81 (3의 4제곱)

# // 연산자 : 나눗셈 후 소수점 아랫자리 버린 결과
7 // 4 #결과 : 1


"""
문자열
"""

#문자열 만드는 방법 4가지
# 1. 큰따옴표 이용("")
# 2. 작은따옴표 이용('')
# 3. 큰따옴표 3개 연속으로 써서 양쪽 둘러싸기 (""" """)
# 4. 작은따옴표 3개 연속(''' ''')

# 여러 줄인 문자열을 변수에 대입하고 싶을 경우
# \n 이용
multiline = "Life is too short\nYou need Python"
print(multiline)

multiline = """
Life is too short
You need Python
"""
print(multiline)


a = "haha\a"
print(a)
# 문자열 인덱싱
a[3]
  # a[0] 과 a[-0]은 동일 결과
a[0] 
a[-0]

# 문자열 슬라이싱
a = "Life is too short, You need Python"
b = a[0] + a[5] + a[10]
print(b)
  # 끝 번호 미 포함. 끝 번호 비 명기시 끝까지 포함
  a[0:4]
  a[1:]
