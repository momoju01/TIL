# 함수 

### 함수(행동/ 계산)

- 특벙한 기능을 하는 코드의 조각(묶음)

- 예 : login 기능 만드려고 하면

  : login 이라는 파일 안에, 일반, 카카오, 페이스북, 비번 확인, 비밀번호 변경 다 넣을 수 있으나 유지 보수 어려움.

  검색해서 갈 수 있도록 분리해서 쓰려고 함

- ex) print('hi')

  ex) x = -3

  ​	  y = abs(x)

  ex) sum=([1,2,3])

### 함수를 사용해야 하는 이유

- 표준 편차 계산 시.... 

  1. 초기값 설정
  2. 값에서 평균을 뺀 것의 제곱을 더한 것 : 분산 (얼마나 흩어져있는지 나타내는 값)
  3. 분산의 제곱근 => 표준 편차

  => 재사용 불가

- 내장함수 사용 (필기)

  ```python
  import math
  values = []
  cnt = len
  
  필기하기
  ```

- **pstdev  함수 (파이썬 표준 라이브러리 - statistics) >>> 추상화& 논리!!**

  ```python
  import statstics
  values = 
  statstics.pstdev(values)
  ```

  먼저 익숙해지는 게 중요. 이해했으면 위로 올라가도 ok

### 함수의 기본 구조

- 이름

- 매개변수(parameters) : **input-> 착즙기에 넣는 재료 : 야채만 넣으세요 하고 지정, 당근(넣는 것 : 인자)**

- 함수 바디

- 반환 값 **나오는 것 : 당근 주스**

  대파! (def 옆에 parameter)

  

### Docstring(Document String)

- 함수나 클래스의 설명

  ```pytho
  __doc__ : magic method
  ```

  

- jupyter notebook에서 함수에 커서 놓고 shift + tab

  ```python
  import statistics
  
  statistics.pstdev
  
  print(statistics.pstdev.__doc__)
  ```

- 파이썬 인터프리터에는 항상 사용할 수 있는 많은 함수와 형(type)이 내장되어 있음!

  불편할 때 찾으면 됨







### 내장 함수(Built in Fuction)

(필기)



### 함수의 선언

- **def**(define) 으로 선언
- 들여쓰기를 통해 **함수 body**(실행될 코드 블록) 작성
  - docstring은 선택적
- 함수는 **매개변수(parameter)**를 넘겨줄 수도 있음
- 함수는 동작 후에 return을 통해 결과값 전달함
  - <u>반드시 **하나**의 객체 반환</u>

### 함수의 호출(필기)

- `함수명()` 으로 호출

  - 매개 변수가 있는 경우, 함수명(값1, 값2…)로 호출

  ```python
  def foo():
      retrun True
      
  def add(x, y):		add(2, 3) 인자(=값 넣는 것임)
      return x + y	# 5
  
  
   max(????) > 뭘 넣어야 할 지 헷갈림. 리스트만 되는지, 문자열만 되는지 익혀야함
  ```

  

- 예시 : 등록하는 것과 실행하는 것!! 다르니까 주의

  ```python
  num1 = 0
  num2 = 1
  
  def func1(a, b):
      return a + b	#등록
  def func2(a, b):
      return a - c	#등록
  def func3(a, b):
      return func1(a, 5) + func2(5, b) #등록
  
  result = func3(num1, num2)	#실행
  print(result)	# 9
  ```



### 함수 실습 문제 - 세제곱 함수 (풀기)

Q1.

```python
def cube(number):
    return number ** 3

print(cube(2))
print(cube(100))
```









# 함수 output

### 함수의 리턴(return)

- 항상 반환되는 값이 있으며, 어떠한 객체라도 상관 없음

- **오직 한 개의 객체만 return 됨**

  - **복수의 객체를 return하는 경우?** : **<u>*튜플로 묶인 것 출력 됨!! *</u>**

    ```python
    def foo(a, b):
    	return a + b, a - b
    	
    foo(1, 2)
    
    -----
    (3, 1) #하나의 튜플로 리턴 됨. 무조건!!!
    ```

  - **명시적인 return 값이 없는 경우 : None 을 반환!! **

    : return(=결과물 나오면) 멈춘다

    ```python
    def greeting():
        print('hi')
        
    my_var = greeting()
    
    print(my_var)
    
    [결과]
    hi
    None 		#명시적인 리턴이 없어서. 
    # print 아니라 return 써야함..
    ```



### 주의 - return vs print(필기)

- return은 함수 안에서만 사용되는 **키워드**
- print는 출력을 위해 사용되는 **함수**(확인용으로 쓰기!)



### 함수 실습 문제 - 사각형 넓이

- 너비와 높이를 입력하여 사각형의 넓이와 둘레를 tuple로 반환하는 함수 rectangle을 작성하시오.

  ```python
  def rectangle(width, height):
      area = width * height
      perimeter = 2 * (width + height)
      return area, perimeter
  
  print(rectangle(20, 30))
  ```









# 함수의 input

### 1.위치 인자(Positional Arguments)

- 기본적으로 함수 호출 시 인자는 위치에 따라 함수 내에 전달됨

  ``` python
  def add(x, y):		# add(2, 3)			def add(x, y):
      return x + y					  # x = 2; y = 3 
  									  # return = x + y
  ```

- 인자와 매개변수

  ```python
  # parameter(매개변수)
  # 함수에 입력으로 전달된 값을 받는 변수
  def my_func(a, b):
      pass
  
  # argument({전달}인자, 인수)
  # 함수를 호출할 때 함수에 전달하는 입력 값
  my_func(1, 2)
  ```



### <u>2. 기본 인자 값(Defalt Argumets Values) : 많이 씀</u>

- 기본값을 지정하여 함수 호출시 인자값을 설정하지 않도록 함.

  - 정의된 것보다 더 적은 개수의 인자들로 호출될 수 있음

  ``` python
  def add(x, y=0):		# add(2)만 넣으면 		def add(x, y=0):
      return x + y					  			# x = 2
  									  			# return = x + y
  ```

  - ex) <u>**print()**</u> 함수에서 :

    `print`(**objects*, *sep=' '*, *end='\n'*, *file=sys.stdout*, *flush=False*)

    기본 인자값 4개 : end='\n' 



### 3. 키워드 인자(Keyword Arguments)

- 직접 변수의 이름으로 특정 인자를 전달할 수 있음

- 키워드 인자 다음에 위치 인자를 사용할 수 없음(예시 뒤에)

  ```python
  def add(x, y):		# add(x=2, y=5) # 머가 들어가는지 알기 쉬움
      return x + y	# add(2, y=5)
  ```





## 정해지지 않은 여러 개의 인자 처리

print(*objects, sep' ', end='\n', files=sys.stdout, flush=False)

### 4. 가변 인자 리스트(Arbitary Argument Lists)

- 함수가 임의의 개수 인자로 호출될 수 있도록 지정

- 인자들은 **<u>튜플</u>**로 묶여(패킹) 처리되며, 매개변수에 *을 붙여 표현

  - *뒤 매개변수 이름은 **args**은 관습적으로 씀
  - 이걸 묶어서 agrs 하나로 받아온다는 의미해서 packing이라고 함

  ```python
  def add(*args):			# add(2) 			
      for arg in args:	# add(2, 3, 4, 5)  -> 이걸 묶어서 agrs 하나로 받아온다는 의미해서 packing이라고 함.
          print(arg)
  ```

  [보충]
  
  def = my_func(a, b, *args)
  
  -> 반드시 들어가야하는 인자 수는 2개! 
  
  print(my_func(1, 2))



### 5. 가변 키워드 인자(Arbitary Keywords Arguments)

- 함수가 임의의 개수 인자를 키워드 인자로 호출될 수 있도록 지정

- 인자들은 **<u>딕셔너리</u>**로 묶여 처리되며, 매개변수에 ******를 붙여 표현  ##두 번 묶는다.

  ```python
  def family(**kwargs):
      for key, value in kwargs:
          print(key, ":", value)
                  
  family(father='Jone', mother='Jane', me='John Jr') #key와 value 형태로 됨
  ```



## ※함수 정의 주의사항

- 기본 인자 값을 가지는 인자 다음에 기본값이 없는 인자로 정의할 수 없음

  ```python
  def greeting(name ='john doe', age):     # 기본 인자, 위치 인자
      
      
  greeting(40) #처음에 기본인자     
  ----
  SyntaxError: non-defalt argument follows default argument
  ```

- 키워드 인자 다음에 위치 인자를 활용할 수 없음

  ```python
  def add(x=3. 5):     # 기본 인자, 위치 인자
      
      
  add(40)     
  ----
  SyntaxError: positional argument follows keyword argument
  ```

- 가변 인자 리스트

  ```python
  
  ```
  
  










### 함수 호출 주의사항 (필기)

#

```python
add(*args, x )
add(1, 2, 3) ???
# 가변인자는 개수 지정 안 되었는데... 3 개를 넣어 버리면 x 는 처리가 안 됨
#가변인자 리스트가 위치 인자보다 앞쪽에 올 수 없음

TypeError: add() missing 1 required keyword-only argument: 'x'
```

```python
my_info(**kwargs, x)
my_info(name ='harry')
# 가변 키워드 인자가 위치 인자보다 앞쪽에 올 수 없음
# 필기
```

```python
my_info(x, y, *args, **kwargs)

위치인자와 *args, **kwargs 같이 사용했을 때 순서
```



### 함수 실습 문제 예시



fuct(?????) 여기에 어떤 식으로 넣을 것인가가 가장 중요



def get(url, params=None, **kwargs) 

[파이썬]https://github.com/psf/requests/blob/master/requests/api.py#L64

```python
def get(url, params=None, **kwargs):
    r"""Sends a GET request.
    :param url: URL for the new :class:`Request` object.
    :param params: (optional) Dictionary, list of tuples or bytes to send
        in the query string for the :class:`Request`.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    """

    return request('get', url, params=params, **kwargs)
```















# 함수 Scope

- 함수는 내부에 지역 스코프(**local scope**)를 생성
- 그외에는 전역 스코프(**global scope**)로 구분
- 스코프
  - 전역 스코프 : 코드 어디에서든 참조할 수 있는 공간
  - 지역 스코프 : 함수가 만든 스코프. 함수 내부에서만 참조 가능
- 변수
  - 전역 변수 : 전역 스코프에 정의된 변수
  - 지역 변수 : 지역 스코프에 정의된 변수

### 변수 수명 주기(lifecycle)

- 변수는 각자의 수명 주기가 존재

  - 빌트인 스코프 : 파이썬이 실행된 이후부터 영원히 유지

  - 전역 스코프 : 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지

    import ____ : 요 시점부터 끝날떼까지

  - 지역(함수) 스코프 :

    함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지

### 함수 스코프 예시

```python
def func():
    a = 20
    print('local', a) #local a
   
func() #호출되면 a 죽음
print('global', a) #global 환경에서 a는 존재 x
				   #바깥에서는 안을 찾을 수 없음

-------------------------------------
local 20 	#func() 까지는 실행 됨
Traceback (most recent call last):
  File "c:\Users\KimYunha\Desktop\test2.py", line 6, in <module>
    print('global', a)
NameError: name 'a' is not defined
PS C:\Users\KimYunha\Desktop> 
```

python tutor로 확인해보기



### 이름 검색 규칙(필기)

- 파이썬에서 사용되는 이름(식별자)들은 이름공간(namespace)에 저장되어 있음
- LEGB rule : 동생이 머리핀을 찾으러 가는 과정
  - Local Scope 	->히키코모리(사춘기 동생 : **'지방'**은 아무도 못들어가게 하고 남의 방 들어감) 
  - Enclosed Scope : 언니방! -> 내꺼 같으면 걍 갖다 씀
  - Global Scope : 온 집
  - Bulit-in Scope : 밖으로 나가서 쓰레기통 뒤지기 ㅋㅋ 

- 즉 함수 내에서는 바깥 스코프의 변수에 접근 가능하나 수정은 할 수 없음.

  ```python
  dict()
  dict = 'hi' 
  이런거 하면 안됨..
  ```



### LEGB 예시 1 # 인강 다시보기...ㅎㅎㅎ(필기)

```python
a = 0
b = 1
def enclosed():
    a = 10
    c = 3
    def local(c):
        print(a, b, c) #첫번째 : 부모 함수 enclosed()에서 c 값 찾아감. c= 300
    local(300)
    print(a, b, c)
enclosed()
print(a,b)

---------
10 1 300
10 1 3
0 1
```

(필기)



### LEGB 예시 2

```python
print(sum)
print(sum(range(2)))
sum = 5
print(sum)
print(sum(range(2))) #여기서 말하는 sum을 5로 생각하는 중. 5(range(2))

# Global scope 이름 공간의 sum 변수에 값 5가 할당됨.
# 이후 global scope에서 sum은 LEGB에 의해 Built-in scope의 내장 함수보다 5가 먼저 탐색됨...
```



### global

- 현재 코드 블록 전체에 적용되며, 나열된 식별자(이름)들이 전역변수임을 나타냄
  - global.a 



### global 예시

local scope 안에서 global 변수 변경할 수도 있음... ㅎ.... 그냥 a는 안됨

되도록이면 사용 x 

```python
#함수 내부에서 글로벌 변수 변경하기
a = 10
def func1():
    global a
    a = 3
    
print(a)
func()
print(a)
print(a)
----
10
3
3
```



### global 관련 에러

1. 같은 코드 블록에서 global 앞에 등장할 수 없음

2. 인자로서 들어오면 안됨

(필기)







### nonlocal

- 전역을 제외하고 가장 가까운(둘러 싸고 있는) 스코프의 변수를 연결하도록 함.
- global (필기..)

```python
```



### nonlocal, global 비교(필기)

```python
# global
# 선언된 적 없는 변수의 활용 가능
def func1():
    global out
    out = 3
    


# nonlocal 
# 선언된 적 없는 변수의 활용 불가
```





### 주의



언패킹,,,





# 재귀 함수



### 팩토리얼

[예시]

```python
# 반복
def fact(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result
        
print(fact(3)) #6

# 재귀
def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)
    
print(factorial(5))
```

- 두 코드 모두 원리는 같습니다!

1. 반복문 코드
   - n이 1보다 큰 경우 반복문을 돌며, n은 1씩 감소합니다.
   - 마지막에 n이 1이면 더 이상 반복문을 돌지 않습니다.
2. 재귀 함수 코드
   - 재귀 함수를 호출하며, n은 1씩 감소합니다.
   - 마지막에 n이 1이면 더 이상 추가 함수를 호출하지 않습니다.

- 재귀함수는 기본적으로 같은 문제이지만 점점 범위가 줄어드는 문제
- 재귀함수를 작성시에는 **반드시, `base case`가 존재 하여야 함**
- `**base case`:** 점점 범위가 줄어들어 반복되지 않는 최종적으로 도달하는 곳
- 재귀를 이용한 팩토리얼 계산에서의 base case는 **n이 1일때, 함수가 아닌 정수 반환하는 것**





### 3. 피보나치 수열

```python
# 몇 번째 항의 값이 몇이냐 ?

#재귀
def fib(n):
    # base case (종료)
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

print(fib(4))

# 반복문
def fib_loop(n):
    if n < 2:
        return n
    
    result = [0, 1]
    for i in range(2, n+1): # list에 0의 값이 포함되어 있기 때문에 자리를 차지해서 +1만큼 계산을 더함.
        result.append(result[i-1] + result[i-2])
        # result.append(result[len(result)-1] + result[len(result)-2])
    return result[-1] # list 의 마지막 값 출력


# 반복문 2)
#이 코드는 잠시만 보여주자. 중점은 list에 다 차곡 차곡 쌓을 필요가 없다는 것
def fib_loop_2(n):
    if n < 2: 
        return n
    
    a, b = 0, 1
    # 우리가 0번째 값 a 와 첫 번째 값 b 를 계속 반복하면서 원하는 값을 만들텐데, 
    # n 이 2일 때는 단 한 번(n-1)만 계산하면 원하는 값을 만들 수 있기 때문
    for i in range(n-1):
        a, b = b, a+b # 새로 만든 b 에 이전의 a, b 값을 더해 새로운 피보나치 값을 만들어 나간다.
    return b


# while 문을 이용한 피보나치 (https://www.python.org/)
# Fibonacci series up to n
def fib_while(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    return b
    
fib_while(30)
```









