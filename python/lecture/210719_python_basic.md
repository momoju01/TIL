# Python 개발 환경

### Python 특징

- 인터프리터 언어
  - 컴퓨터 (0 ,1) <-----(컴파일/인터프리터)----프로그래밍 언어 <--- 사람
  - 컴파일러(번역) : 전체 다 하고 넘김 : 다 하고 넘기면 실행 속도 빠름
  - 인터프리터(통역) : 개발 빠름/ 한 줄씩 : 속도 느림

- 객체 지향 프로그래밍 

- 동적 타이핑 : 변수의 타입 지정 필요 없음

  ex) a = 3 으로 타입 지정 안 하고 씀 java는 int score 이런식으로 붙여줌

### Python Jupyter Lab

- 웹 브라우저 환경에서 코드를 작성할 수 있는 오픈소스
- https://abit.ly/ssafy-document 설치 (webex 시간에 하기)
- Google colab https://colab.research.google.com/?utm_source=scs-index



### Python 수업 

- 알고리즘 - Pycharm
- 코딩 
  - 파이썬 - Jupyter Notebook & Visual Studio Code
  - 웹 - Visual Studio Code
    - HTML/CSS, Django, Javascript, Vue 등 



# 기초 문법

### 코드 스타일 가이드

- 코드를 '어떻게 작성할지'에 대한 가이드라인
  - PEP8 - 파이썬에서 제안하는 스타일 가이드(공식)
  - Google Style Guide 등 

### 주석(Comment)

- 한 줄 주석은 #으로 표현
- 여러 줄의 주석은 한 줄씩 #을 사용하거나 """ 또는 '''으로 표현한다.
- 다만 """ 또는 '''으로 표현하는 방법은 docstring을 위해 사용한다.
- 드래그 후 ctrl + / 

##### Docstring - 특수한 형태의 주석

- 함수/클래스의 설명을 작성 *함수에서 다룸
- 함수나 클래스에 대한 설명서/가이드라인

### 코드 라인

- 코드는 1줄에 1문장(statement)이 원칙
- 문장은 파이썬이 실행 가능(executable)한 최소한의 코드 단위
  - 기본적으로 파이썬에서는 세미콜론을 작성하지 않음

  - 한 줄로 표기할 때는 세미콜론을 작성하여 표기할 수 있음(권장 x)

  - 줄을 여러줄 작성할 때는 역슬래시`\`를 사용하여 아래와 같이 할 수 있다. 

    ```python
    print('hello\
    world')
    ```

    helloworld

  - PEP-8 가이드에 따르면 여러줄 문자열은 아래와 같이 쓰는 게 관례(convention)입니다.

    ```python
    print("""hello
    world""")
    ```

    hello

    world



# 변수와 식별자

### 변수 

<u>데이터/정보(변수)		행동(계산)</u> 

자료								함수

리스트							연산자

…									반복문

- 할당 연산자(=)를 통해 값을 할당(assignment)
- type () : 변수에 할당된 값의 타입 확인 가능
- id() : 변수에 할당된 값(객체)의 고유한 아이덴티티 값이며, 메모리 주소를 확인

### 할당 연산자(=)

- 같은 값을 동시에 할당할 수 있음 
  - ex) **x = y** = 1004 
- 다른 값을 동시에 할당할 수 있음(multiple assignment)
  - x, y = 1, 2 
  
  - **x, y = 1  -> 이건 안 됨**
  
  - **x, y = 1, 2, 3 -> 안 됨**
  
    

### 값 swap

- x = 10, y =20 일 때,

  각각 값을 바꿔서 저장한느 코드를 작성하시오.  [출력]20 10

  1. 임시 변수 temp 사용

     temp = x

     x = y

     y = temp

     print(x, y) 

  2. **Pythonic !** 

     x, y = y, x 

     print(x, y)

### 식별자(Identifiers)

**변수(박스)의 이름을 어떻게 지을 수 있을까?**

- 변수, 함수, 모듈, 클래스 등을 식별하는 데 사용하는 이름(name)

- 규칙 

  - 영문 알파벳, 언더스코어(_), 숫자로 구성
  - 첫 글자에 숫자가 올 수 없음 6a = 8 (안 됨)
  - 길이 제한이 없고, 대소문자를 구별
  - 다음의 키워드는 예약어(reserved words)로 사용할 수 없음

  ```python
  import keyword
  print(keyword.kwlist)
  ```

  | **and**      | **del**     | **global** | **nonlocal** | **while** |
  | ------------ | ----------- | ---------- | ------------ | --------- |
  | **as**       | **elif**    | **if**     | **not**      | **with**  |
  | **assert**   | **else**    | **import** | **or**       | **yield** |
  | **break**    | **except**  | **in**     | **pass**     | **False** |
  | **class**    | **finally** | **is**     | **raise**    | **True**  |
  | **continue** | **for**     | **lambda** | **return**   |           |
  | **def**      | **from**    | **None**   | **try**      |           |

- 내장함수나 모듈 등의 이름으로도 만들면 안 됨 (기존의 이름에 다른 값을 할당하게 되므로 더 이상 본래 기능 동작하지 않음)



# 데이터 타입

**무엇을 저장할까?**

- 데이터 타입 
  - 숫자(number)
    - int (정수, integer)
    - float (부동소수점, 실수, floating point number)
    - complex (복소수, complex number)

- 문자열(String)
- 참/거짓(Boolean)
- None

### 숫자 - int

- 모든 정수 타입은 int 
- 매우 큰 수를 나타낼 때 오버플로가 발생하지 않음
  - 오버플로 : 데이터 타입별로 사용할 수 있는 메모리의 크기를 넘어서는 상황
  - 임의 정밀도 산술(Arbitrary percision arithmetic)을 통해 고정된 형태의 메모리가 아닌 가용 메모리들을 활용하여 모든 수 표현에 활용

- 진수 표현

### 숫자 - float

- 정수가 아닌 모든 실수는 float 타입
- 부동소수점 
  - 실수를 컴퓨터가 표현하는 방법 -2진수(비트)로 숫자를 표현
  - 이 과정에서 floating point rounding error 가 발생하여 예상치 못한 결과 발생

### floating point rounding error

- 부동소수점에서 실수 연산 과정에서 발생 가능

  - 3.14 - 3.02 == 0.12 -> False

  - 3.14 - 3.02 = 0.120000000000001 임! 

  - 실수는 유한개의 비트를 사용하여 근사값으로 표현을 함.

  - <u>매우 작은 수바도 작은지를 확인하거나 math 모듈 활용</u>

    1. 임의의 작은 수

       ```python
       a = 0.1*3
       b = 0.3
       abs(a-b) <= le-10  #abs() 는 절대값 나타냄 # True
       ```

    2. system상의 machine epslion

       ```python
       import **sys**
       
       print(abs(a-b) <= **sys.float_info.epsilon**) # True
       print(sys.float_info.epsilon) # 2.220446049250313e-16
       ```
    
    3. Python 3.5 이상
    
       ```python
       import math
       
       math.iscolos(a, b) # True
       ```

### 숫자 - complex

- 실수부와 허수부로 구성된 복소수는 모두 complex 타입

  - 허수부를 j로 표현

    a = 3+4j
    
    ```python
    # 실수부
    a = 1+2j
    a.real #1
    ```
    
    ```python
    # 허수부
    a = 1+2j
    a.imag
    ```
    
    

### 문자열(String)

- 모든 문자는 str 타입
- 문자열은 작은 따옴표나 큰 따옴표를 활용하여 표기
  - 문자열을 묶을 때 동일한 문장부호를 활용
  - PEP8에서는 소스코드 내에서 하나의 문장부호를 선택하여 유지하도록 함

### 이스케이프 시퀀스(escape sequnce)

- 문자열 내에서 특정 문자나 조작을 위해 **역슬래시**를 활용하여 구분
  - print('철수\'안녕\' ')

### String Interpolation

- 변수의 값을 문자열의 자리 표시자(placeholder) 로 대체하는 방법

  1. %-formatting

  2. str.format()

     ```python
     print('Hello, {}! 성적은{}'.format(name, score))
     ```

  3. f-strings (python 3.6)

     ```python
     print(f'Hello, {name}! 성적은 {score}') 
     ```

     

- f- string 사용 예

  ```python
  import datetime
  today = datetime.datetime.now()
  print(today)
  
  #2021-07-19 21:18:57.557325
  ```

  ```python
  print(f'오늘은 {today:%y}년 {today:%m}월 {today:%d}일 {today:%A}')
  
  #오늘은 21년 07월 19일 Monday
  ```

  ```python
  # string interpolation을 통해 출력형식 지정 뿐만 아니라, 연산도 가능합니다.
  # pi = 3.141592 를 할당하고 
  # 원주율은 3.14. 반지를이 2일 때 원의 넓이는 12.566368 이라고 출력해봅시다.
  
  pi = 3.141592
  f'원주율은 {pi:.3}. 반지름이 2일때 원의 넓이는 {pi*2*2}'
  ```

  



### 참/ 거짓 Boolean

- True/ False 값을 가진 타입은 bool

- 비교/ 논리 연산을 수행하에 있어서 활용됨

- 다음은 모두 False로 변환

  0, 0.0, (), [], {}, None

### None

- 값이 없음을 표현하기 위한 None Type



# 타입 변환

### 자료형 변환/타입 변환(Type converson, Typecasting)

- 암시적 타입 변환(Implicit) : 사용자가 의도 x
- 명시적 타입 변환 (Explicit) : 사용자가 의도 o

### 암시적 타입 변환

​	True + 3 = 4

​	3 + 5.0 = 8.0

### 명시적 타입 변환

- int 
  - str*, float  => int

    단 형식에 맞는 문자열만 정수로 변환 가능

  - int('3') + 4  -> 7
- float
  - str*, int => float
  - '3.5' + 3.5 -> 암시적 타입변환 x
  - float('3.5') +3.5 = 7
- str
  - int, float, list, tuple, dic => str



# 연산자

1. 산술
2. 비교
3. 논리
4. 복합
5. 기타

### 산술 연산자

| 연산자 |           내용 |
| -----: | -------------: |
|      + |           덧셈 |
|      - |           뺄셈 |
|      * |           곱셈 |
|      / |         나눗셈 |
|     // |             몫 |
|      % | 나머지(modulo) |
|     ** |       거듭제곱 |

- 나눗셈은 항상 결과가 float

- divmod() : 앞에 것을 뒤에 것으로 나눈 몫과 나머지 

  print(divmod(5, 2))

  -> 2, 1

### 비교 연산자

|   연산자 |                   내용 |
| -------: | ---------------------: |
|      `<` |                   미만 |
|     `<=` |                   이하 |
|      `>` |                   초과 |
|     `>=` |                   이상 |
|     `==` |                   같음 |
|     `!=` |               같지않음 |
|     `is` |        객체 아이덴티티 |
| `is not` | 부정된 객체 아이덴티티 |

- 특정 변수가 비어있는지 확인하기 위해서는 X == None 아니라 X is None 쓰는 것을 권장 (OOP에서 추가 설명)

### 논리 연산자

|  연산자 |                         내용 |
| ------: | ---------------------------: |
| a and b |     a와 b 모두 True시만 True |
|  a or b |  a 와 b 모두 False시만 False |
|   not a | True -> False, False -> True |

print(not 'hi') 

False

##### 논리 연산자 - 단축평가

- and : 첫번째 값이 False 나오면 무조건 False -> 첫번째 값 반환
- or : 첫번째 값이 True 나오면 무조건 True -> 첫번째 값 반환

5 0 0 0 5 3 3 0

### 복합 연산자

|  연산자 |       내용 |
| ------: | ---------: |
|  a += b |  a = a + b |
|  a -= b |  a = a - b |
|  a *= b |  a = a * b |
|  a /= b |  a = a / b |
| a //= b | a = a // b |
|  a %= b |  a = a % b |
| a **= b | a = a ** b |

- 복합 연산자는 연산과 대입이 함께 이뤄짐

  ​	주로 반복문에서 사용됨

  - cnt = 100
  - count += 1
  - print (cnt)

### Concatenation

- +는 숫자가 아닌 자료형에서도 사용 가능함

  - 컨테이너, OOP에서 연산자의 다양한 활용을 확인

    'hello, ' + 'ssafy!' -> 'hello, ssafy!'

### Containment Test (포함 검사)

- 특정 요소가 속해 있는지 여부를 확인

  'a' in 'apple' -> True

### Identity

- is 연산자를 통해 동일한 객체(object)인지 확인 가능함

  ```python
  a = 3
  b = 3
  print(a is b)
  print(id(a), id(b)) # TRUE
  ```

  ```python
  c = 257
  d = 257
  print(c is d)
  print(id(c), id(d))
  False 
  # -5 ~256 까지는 메모리에 고정된 주소 있음. 값이 아닌 숫자들은 그 때 그 때마다 id 다르게 설정됨
  ```

### Indexing / Slicing

- []를 통해 값을 접근하고, [:]를 통해 슬라이싱 가능함 (컨테이너에서 추가 학습)
  - 'hello, ssafy!'[0] -> 'h'
  - 'hello, ssafy!'[1:5] -> 'ello'

### 연산자 우선순위

- ()
- Slicing
- Indexing
- **
- 단항 연산자(+,-) : 부호
- 산술 연산자(*, /,%)
- 산술 연산자(+,-)
- 비교 연산자, in, is 
- not
- and 
- or



# 표현식 / 문장

### 표현식, 식(expression)

- 표현식은 평가되고 값으로 변경
- 하나의 값으로 환원(reduce)될 수 있는 문장
- 하나의 값(value)도 표현식(expression)
  'hello'
- 식별자, 값, 연산자로 구성



### 문, 문장(statement)

- 파이썬이 실행 가능한 최소한의 코드 단위

- 하나의 값(value)도 문장(expression)
  'hello'
- 표현식(expression)도 문장이 될 수 있습니다.
  5 * 21 - 4 

