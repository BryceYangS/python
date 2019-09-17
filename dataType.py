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


a= "20190917Sunny"
date = a[:8]
weather = a[8:]
print(date)
print(weather)

# 문자열 포매팅
#  1. 숫자 바로 대입
"I eat %d apples" %3
#  2. 문자열 바로 대입
"I eat %s apples" %"five"
#  3. 변수 대입
number = 9
"I eat %d apples" %number
#  4. 2개 이상 값 표출
number = 10
day = "three"
"I ate %d apples. so I was sick for %s days." %(number, day)
##########
# %s : 문자열 / %c : 문자 / %d : 정수 / %f : 부동 소수 / %o : 8진수 / %x : 16진수 / %% : literal %(문자 '%' 자체)
##########

# 1. 정렬과 공백
"%10s" %"hi" #공백 8 , hi 2
"%-10sjane" %"hi"
# 2. 소수점
"%.4f" %3.23136 # 소수점 6부터 올림


"""
문자열 관련 함수
"""
# count : 문자 개수 세기
a = "hobby"
a.count('b')
# find : 문자 인덱스 (해당 문자가 여러개일 경우, 맨 처음 나오는 인덱스 리턴 / 문자열에 해당 문자가 없을 경우 -1 리턴)
a.find('b')
# index : 문자 인덱스 (find와 다른 점 : 해당 문자가 없을 경우 에러 발생!!)
a.index('i')
# join : 문자열의 각 문자 사이에 삽입
a.join(',,') # 결과 : ',hobby,'
# upper : 대문자 변환 <-> lower : 소문자 변환
# lstrip : 왼쪽 공백 제거 <-> rstrip : 오른쪽 공백 제거
a = "   a h bc"
a.lstrip()
# strip : 양쪽 공백 제거
a = " af ssgsg awf   "
a.strip()
# replace : 문자열 바꾸기
a.replace("a", "Yang")
# split : 문자열 나누기
a.split() # 공백 기준(스페이스, 탭, 엔터)
a = "f,faaf,feafef,fwefa"
a.split(',') # 나누는 기준 ',' 설정