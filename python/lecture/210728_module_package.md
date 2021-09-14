# 210728_module_and_package





### 파이썬 표준 라이브러리

- 파이썬에 기본적으로 설치된 모듈과 패키지
- 예시) random





### 파이썬 패키지 관리자(pip)

- pythin package index 에 저장된 외부 패키지들을 설치하도록 도와주는 패키지 관리 시스템



### pip 명령어

- 패키지 설치 

  - 최신 버전/ 특정 버전 / 최소 버전 명시하여 설치

  - 이미 설치되어 있는 경우 알리고 아무것도 안 함

    $ pip install somepackage

    $ pip install somepackage==1.0.5

    $ pip install 'somepackage >= 1.0.4'

- 삭제

  - pip는 패키지를 업그레이드 하는 경우 과거 버전을 자동으로 지워줌

    $ pip uninstall SomePackage

- 패키지 목록 및 특정 패키지 정보

  - $ pip list
  - $ pip show <notebook> : 정보 확인하기

- 패키지 freeze
  -  $ pip freeze
  - 설치된 패키지의 비슷한 목록을 만들지만 pip install 에서 활용되는 형식으로 출력
  - 해당하는 목록을 requirements.txt(관습)으로 만들어 관리함 
  - git 에서 다운받을 때 환경 똑같이 맞추기 위해서 사용
  - $ pip freeze > requirements.txt  
  - $ pip install -r requirements.txt



### 가상환경

- 파이썬 표준 라이브러리가 아닌 외부 패키지와 모듈을 사용하는 경우 모두 pip를 통해 설치해야함.
- 복수의 프로젝트를 하는 경우 버전이 상이할 수 있음.
  - 과거 외주 프로젝트 2.0
  - 현재 프로젝트 3.0

### venv

- 파이썬 공식 
- 가상 환경을 만들고 관리되는데 사용되는 모듈(python 3.5부터)
- 특정 디렉토리에 가상 환경을 만들고, 고유한 파이썬 패키지 집합을 가질 수 있음
  - 특정 폴더에 가상환경이 있고
  - 실행 환경에서 가상 환경을 활성화 시켜
  - 해당 폴더에 있는 패키지를 관리/ 사용함



### 가상환경 생성

- 가상환경을 생성하면, 해당 디렉토리에 별도의 파이썬 패키지가 설치됨
  - **$ python -m venv <폴더명> : **폴더명 venv 로...(관습)



### 가상환경 활성화/비활성화

- 아래의 명령어를 통해 가상환경을 활성화

  - <venv>는 

  - **$ source venv/Scripts/activate**

  - (venv) 생김

  - **$ pip list :** 로 뭐 설치된건지 확인. 

    설치된 것 두 개 밖에 없음~~~

  - $ deactivate



### 주의할 것 

- my_dir 에서 venv 실행시킨 후 Desktop으로 나가도 venv 그대로 있음.
- 단순히 my_dir 에 국한되어있는 환경이 아님. 그냥 저기에서 활성화되어있을 뿐임...! 



### cmd 와 bash 환경에서 실습

1. 첫 번째 프로젝트 폴더 A

- $ python -m venv venv
- $ source venv/Scripts/activate : venv 활성화
- $ pip install requrests  : request 설치함
- $ pip list : 뭐 설치되어있는지 확인
- $ deactivate : 비활성화



2. 두 번째 프로젝트 폴더 B

- $ python -m venv venv
- $ source venv/Scripts/activate
- $ pip install django beautifulsoup4  : django와 beautifulsoup4 설치함
- $ pip list : 뭐 설치되어있는지 확인
- $ deactivate



3. 프로젝트 C 가 B 환경으로 되어야한다면:-

- B에서 $ pip freeze > requirements.txt 만들기

- C 만들어서 requirements.txt 복붙해주기.

- C에서 git bash 열기

- $ ls 

  requirements.txt

- $ source ../project_B/venv/Scripts/activate : B의 가상환경에 가서 하려면(권장 x)

- 같은 환경을 쓰더라도 다시 가상환경을 만들어 줌.

- $ python -m venv venv

- $  source venv/Scripts/activate

- $ pip list

- $ pip install -r requirements.txt : requirements파일 읽어서 install 하겠다

- B의 환경과 비교해보면 똑같은 list임을 알 수 있음~

- 단 venv를 github에 올리지 않음. requirements.txt 만 올림
- 폴더 경로 들어가므로 함부로 옮기지 않음.





# 모듈/ 패키지 활용하기

### 모듈 만들기 - check

- check.py 에 짝수를 판별하는 함수(even)과 홀수를 판별하는 (odd)를 만들고  check 모듈을 활용해보시오

1. check.py 라는 나만의 모듈 만들기

2. 사용 :

   ```python 
   import check 
   
   dir(check)
   # ['even', 'odd']
   
   check.even() 이런 식으로 사용 가능~
   ```

3.  모듈 중 일부만 가져오기

   ```python
   ```



### 패키지 만들기

- 수학과 통계 기능이 들어간 패키지를 아래와 같이 구성

  - math의 tools : e, pi, my_max

  - statistics의 tools: mean

  - 폴더 구조 : 모든 폴도에는 `__init__.py` 를 만들어 패키지로 인식.

    3.3 부터는 해당 파일 없어도 되지만 하위 버전 호환 때문에

    ```python
    my_package/
    math/
    	__init__.py
        tools.py
    statistics/
    	__init__.py
        tools.py
    ```



### 다양한 모듈 활용 사용하기...ㅎ (인강 다시 듣기)

 