# 가장 유명한 방식은 Python의 창시자 '귀도 반 로섬'이 제시한 코딩 스타일인 PEP-8

# C, Java와 달리 파이썬은 변수를 선언할 때 따로 자료형을 지정하지 않는다. 
# 내부적으론 자료형이 있으나 런타임에서 인터프리터가 추론한다.
 
# 파이썬은 객체 지향 언어이고 원시 자료형이 없기 때문에 모든 값은 반드시 객체로 간주된다. 
# 따라서 모든 데이터의 자료형은 그 데이터의 클래스이다. 
# type() 함수로 변수의 자료형을 확인할 수 있다.

class Value:
  pass

var = Value()
print(type(var)) # <class '__main__.Value'>

# Number (숫자)
# 정수(int)는 길이 제한이 없어 큰 수도 별도의 자료형을 지정하지 않고 작은 수와 똑같이 다룰 수 있는 편리함을 지닌다. 
# 실수는 8바이트로 제한된다.

a = 1234 # 정수형
b = 3.14 # 실수형
print(type(a), type(b)) # <class 'int'> <class 'float'>

# List Tuple 
# 리스트를 사용하면 사실상 스택(자료구조)을 사용할지 큐(자료구조)를 사용할지를 고민하지 않아도 되며, 
# 스택과 큐에서 사용 가능한 모든 연산을 동시에 제공한다. 
# 리스트는 객체로 되어 있는 모든 자료형을 포인터로 연결하는 구조로 되어 있다.

# 파이썬은 모든 것이 객체며, 파이썬의 리스트는 이들 객체에 대한 포인터 목록을 관리하는 형태로 구현되어 있다. 
# 사실상 연결 리스트에 대한 포인터 목록을 배열 형태로 관리하고 있으며, 
# 그 덕분에 파이썬의 리스트는 배열과 연결리스트를 모두 합친 듯이 강력한 기능과 문법을 제공한다.

# 리스트는 객체가 수정 가능하지만, 
# 튜플은 최초 생성 이후 수정이 불가능하다. 
# list()와 tuple() 함수를 통해 서로 형 변환이 가능하다. 
# 고차원 리스트도 가능하다.

l = [1, 2, 3] #일차원 리스트
t = tuple(l) #튜플로 변환
print(t) # (1, 2, 3)
li = list(t) #리스트로 변환
l = [[1, 2, 3], [1, 2, 3]] #이차원 리스트

# 리스트와 튜플의 값을 참조할 때에는 변수명[숫자]의 형태로 입력한다. 
# 아래는 각각 일차원 리스트, 이차원 리스트, 튜플의 값을 출력하는 코드이다.

li_one = [1, 2, 3] # 일차원 리스트
li_two = [[1, 2, 3], [4, 5, 6]] # 이차원 리스트
tu = (7, 8) # 튜플

print(li_one[0], li_two[0][1], tu[1]) # 1 2 8

# 리스트, 튜플에 없는 원소를 참조하기 때문에 오류가 발생한다
# Traceback (most recent call last):
#   File "[파일명]", line 1, in <module>
# IndexError: list index out of range\

# String 문자열

# 글자로 이루어진 변수, 따옴표를 이용하여 표기.
a = 'text'
# 따옴표를 이용하지 않으면 오류가 걸린다.

# a = text

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'text' is not defined

# 사용할 수 있는 따옴표로는 작은 따옴표('), 큰 따옴표("), 작은 따옴표 3개('''), 큰 따옴표 3개(""")가 있다
a = " ' 를 포함한 문장"
b = ''' " 을 포함한 문장'''

# Dictionary 딕셔너리

# 파이썬의 딕셔너리는 키/값 구조로 이뤄진 딕셔너리를 말한다. 
# 파이썬 3.7 이상에서는 입력 순서 또한 유지되며, 내부적으로는 해시 테이블(Hash Table)로 구현되어 있다. 
# 3.6 이하에서는 입력 순서를 보장하지 않으므로 유의해야 한다. 중괄호를 사용해서 선언

a = {}
# key1, key2는 초깃값으로 지정해 선언하거나 key3처럼 나중에 별도로 선언하여 
# value3라는 값을 할당할 수 있다.
a = {'key1':'value1', 'key2':'value2'} 
a['key3'] = 'value3'

# 키에는 해시가능한(hashable) 자료형만 가능하며, 
# 값에는 리스트 뿐만 아니라 집합 자료형 등 모든 자료형이 가능하다.

a = {'key1':[1, 2, 3], 'key2': (4, 5, 6)}

# Bool

#  대문자를 쓴다는 점이 다른 프로그래밍 언어와 독특하게 구분된다. 
# 소문자로 쓰면 예약어로서 기능하지 않다.

a == 1

# a가 1이라면 'True', 그 외의 것이라면 'False'가 출력
# 변수로 만들 수 있다.

c = True
if a > 10:
    c = False

# 직접 True or False 값을 할당시켜 쓸 수 있다.
# while True:
#     print('hello')
# 하지만 이건 무한루프를 돌게 된다.

# 대소문자가 달라지면 에러가 발생한다.
# isntTrue = true

# Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
# NameError: name 'true' is not defined.

# Truthy/Falsy
# 파이썬도 특정 값이나 객체에 참 또는 거짓의 논리를 부여할 수 있다.

# 예를 들어 문자열이 유효한지 검사할 때
str = ''
if len(str) > 0: ...
# 이렇게 해야 할 것을

str = ''
if str: ...
# 와 같이 변경 할 수 있다.

# Truthy: True, 0이 아닌 수, 유효한 문자열(비지 않은 문자열), 유효한 리스트, 유효한 튜플
# Falsy: False, None, 0, 빈 문자열, 빈 리스트, 빈 튜플 등

# 자체적으로 선언한 객체에 bool 논리를 부여해 주려면 __bool__ 메소드를 사용하면 된다. 
# __bool__ 메소드가 없는데 __len__ 메소드가 있다면 해당 메소드에 따라 길이가 0이면 False, 
# 0보다 크면 True로 간주하고, __bool__, __len__ 둘 다 없으면 무조건 True로 취급한다.

class Value:
    def __init__(self):
        self.valid = False
    def __bool__(self):
        return self.valid
    def setValidity(self, validity):
        self.valid = validity

var = Value()
print(bool(var))  # False
var.setValidity(True)
print(bool(var))  # True

class Stack:
    def __init__(self):
        self.stack = list()
    def __len__(self):
        return len(self.stack)
    def push(self, x):
        self.stack.append(x)
    def pop(self):
        return self.stack.pop()

stack = Stack()
print(len(stack))   # 0
print(bool(stack))  # False

stack.push(100)     # 100 입력
print(len(stack))   # 1
print(bool(stack))  # True

stack.pop()         # 100 출력
print(len(stack))   # 0
print(bool(stack))  # False

# 자료형 변환 Data Type
# 자료형(바꿀 변수)의 형태로 아주 간단하게 변경 가능하다.

str() 
  # float형이나 int형을 문자열로 변환할 때 사용한다. 제일 기본적으로 쓰인다.
int() 
  # 정수형으로 바꾼다. 양의 실수와 음의 실수 모두 소수점을 버린다.
float() 
  # 실수형으로 바꾼다.
complex() 
  # 복소수형으로 바꾼다. 허수는 i가 아니라 j로 표기한다.
list() 
  # 리스트로 바꾼다. tuple과 형변환에 자주 사용된다.
tuple() 
  # 튜플로 바꾼다. list와의 형변환에 자주 사용된다.
set() 
  # 세트형(집합형)으로 바꾼다. 리스트나 튜플은 중복 원소를 허용하지만 세트는 중복을 허용하지 않으므로, 
  # 임의의 리스트나 튜플을 세트형으로 변환시키면 중복이 자동으로 제거되는 유용함을 지닌다.

# 입출력

# Hello, world! 문자열 출력 
print("Hello, world!")

a = 10
b = 20

# 10 , 20 출력

# 1. 인자 여러개로 주기
print(a, "," , b)

# 2. c 스타일 
print("%d , %d" % (a,b))

# 3. format 함수
print("{} , {}".format(a, b))

# 4. f-string
print(f"{a} , {b}")

# print()에 인자를 여러개 준 경우 각각의 문자열이 한 칸 공백을 두고 출력된다. 
# 주의할 점은, c 스타일은 권장되지 않는 문법이다.

# input()은 기본적으로 str 형태로 값을 받으며, 특정 자료형 함수를 이용하면 다른 형으로 값을 받을 수 있다. 
# 만약 그 형으로 값이 나오지 않으면 예외 오류가 일어난다.

a = input("input")
b = int(input("input"))
c = float(input("input"))

# 입력에서 걸리는 시간을 줄이려면 sys 모듈의 stdin.readline()을 이용하면 좋다. 
# 다만, 이 경우는 input()과는 달리 입력받는 기능만을 할 수 있다.

from sys import stdin
# import sys

a = stdin.readline()
b = int(stdin.readline())
c = float(stdin.readline())