# **SQL Injection**

> 이용자의 입력값이 SQL 구문의 일부로 사용될 경우, 해커에 의해 **조작된 SQL 쿼리문이 데이터 베이스에 그대로 전달되어 비정상적 명령을 실행시키는 공격 기법**



## SQL Injection 공격 원리와 유형

SQL Injection은 데이터베이스 명령어인 SQL 쿼리문에 기반하여 공격을 수행한다. 공격에 이용되는 쿼리문은 문법적으로는 지극히 정상적인 SQL 구문이다. 다만 실행되지 말아야 할 쿼리문이 실행되어 공격에 이용되는 것이다.

### 조건

1. 웹 애플리케이션이 DB와 연동하고 있다.
2. 외부 입력값이 DB 쿼리문으로 사용된다.



## 공격 방법

### **1. 일반적인 SQL 인젝션**

#### **1-1. 쿼리 조건 무력화 (Where 구문 우회)**

Where 구문은 SQL에서 조건을 기술하는 구문이다. Where 조건에 기술된 구문이 ‘참(True)’이 되는 범위만 쿼리 결과로 반환한다. **SQL 구문에 주석(Comment)를 의도적으로 삽입**하여 Where 조건을 무력화시킬 수 있다.

예를 들어, 다음과 같이 로그인을 처리하는 동적 쿼리가 있다고 가정하자. 외부 입력값인 UserID 와 Password가 쿼리문의 일부로 사용되고 있다.

```sql
SQL = "Select * From Users"       
	+ " Where UserID = '"+ UserID +"' And Password = '" + Password + "'"
```



다음과 같이 UserID 값에 주석을 삽입하면 주석 이하의 구문은 실행되지 않게 되어 admin 이라는 계정의 패스워드를 몰라도 인증을 통과하게 된다. (admin이라는 ID는 이미 알고 있다고 가정. 그리고  - - 는 MS SQL Server의 주석이다. MySQL의 경우는 #을 사용해야 한다.)

```
[ 외부 입력값 ]
UserID: admin'--
Password: 아무거나
```

```sql
[ 실행되는 쿼리문 ]
Select * From Users Where UserID = 'admin'-- And Password = '아무거나'
```



또한 **항상 참이 되도록 Boolean 식을 구성**하여 Where 조건을 무력화 시킬 수 있다.

다음과 같이 Password 값에 참(true)인 조건이 or 로 연결되도록 삽입하면 or 조건으로 인해 쿼리의 결과가 무조건 참이 되어 없는 계정과 다른 패스워드라 할지라도 (예시의 test 라는 계정은 실제 db에 없는 계정임) 인증을 통과하게 된다.

```
[ 외부 입력값 ]
UserID: test
Password: 1234' or '1'='1
```

```sql
[ 실행되는 쿼리문 ]
Select * From Users Where UserID = 'test' And Password='1234' or '1'='1'
```



**직접 데이터베이스 내용을 조작**할 수도 있다.

다음과 같이**;(콜론)으로 명령어를 연결**하면 한 줄로 된 두 개이상의 명령어를 연속해서 기입할 수 있는데 여기에 **테이블을 삭제하거나 수정하는 조작된 쿼리문을 삽입할 수 있다.**

```
[ 외부 입력값 ]
UserID: admin' ; DELETE From Users--
Password: 아무거나
```

```sql
[ 실행되는 쿼리문 ]
Select * From Users Where UserID = 'admin' ; DELETE From Users -- And Password='아무거나'
```



#### **1-2. 고의적 에러 유발 후 정보 획득**

시스템에서 발생하는 에러 메시지를 이용해 공격하는 방법이다. **GET 방식으로 동작하는 URL 쿼리 스트링을 추가하여 에러를 발생**시킨다. 이에 해당하는 오류가 발생하면, 이를 통해 해당 웹앱의 데이터베이스 구조를 유추할 수 있고 해킹에 활용한다.

SQL 쿼리문에서 **UNION 은 두 테이블의 결과를 합치는 명령어이다.** UNION으로 합쳐지는 두 테이블은 **컬럼 갯수가 일치**해야만 오류가 나지 않는다. 아래와 같이 **컬럼 1개**만 가진 대상 테이블을 가정하여 UNION 구문을 삽입한다.

```
[ 외부 입력값 ]
UserID: test'UNION SELECT 1 --
Password:아무거나
```

```sql
[실행되는쿼리문 ]
Select * From Users Where UserID = 'test' UNION SELECT 1 -- And Password='아무거나'
```

테스트용 Users 테이블은 **4개의 컬럼**으로 구성되어 있다. 따라서 위의 쿼리문이 실행되면 다음과 같은 오류가 발생하여 브라우저에 노출된다.

*"UNION, INTERSECT 또는 EXCEPT 연산자를 사용하여 결합된 모든 쿼리의 대상 목록에는 동일한 개수의 식이 있어야 합니다." (SQL Server 기준)*

컬럼 수를 늘리면서 입력을 반복해서 시도하다 마침 4개의 UNION SELECT를 하는 순간 오류가 발생하지 않음을 알고 이 기능의 원본 쿼리가 반환하는 컬럼의 수가 4개인 것을 알게 된다. (MS SQL Server에서는 UNION 되는 컬럼끼리 데이터 타입이 충돌나면 타입 오류를 발싱시키므로 컬럼 타입을 맞출 필요가 있다.)

```
[ 외부 입력값 ]
UserID:test'UNION SELECT 1,1,1,1 --
Password:아무거나
```

```SQl
[실행되는쿼리문 ]
Select * From Users Where UserID = 'test'UNION SELECT 1,1,1,1 -- And Password='아무거나'
```

이렇게 알아낸 컬럼 수를 기반으로 다음과 같이 시스템 테이블의 정보를 조회해 볼 수 있다.

다음의 쿼리가 실행되도록 SQL 구문을 주입하면 현재 데이터베이스에 존재하는 모든 테이블 목록을 볼 수 있다. (아래 쿼리는 SQL Server 기준.)

```sql
Select * From Users Where UserID = 'test'UNION SELECT name, object, 1,1 FROM sys.tables -- And Password='아무거나'
```

위와 같이 테이블 리스트 조회에 성공했다면, 테이블을 선택해서 그 테이블에 저장된 데이터를 획득할 수 있다.



#### 1-3. 시스템 명령어 실행

MS SQL Server의 경우 시스템 명령을 실행할 수 있는 확장 프로시저를 제공한다. xp_cmdshell 프로시저를 이용한다. 다음과 같이 UserID 값에 **;(콜론)으로 xp_cmdshell 실행 구문을 연결**하고 이후 구문은 주석처리 되도록 하여 윈도우 C 드라이버를 탐색하는 명령을 보낸다. 이 계정에 유효한 권한이 주어져 있다면 어떤 시스템 명령도 내릴 수 있게 된다.

```
[ 외부 입력값 ]
UserID: admin' ; EXEC master.dbo.xp_cmdshell 'cmd.exe dir c:'--
Password:아무거나
```

```sql
[ 생성된 쿼리문 ]
Select * From Users Where UserID = 'admin' ;EXEC master.dbo.xp_cmdshell 'cmd.exe dir c:'-- And Password='아무거나'
```



### 2. Blind SQL 인젝션

공격하는 대상 웹페이지가 어떠한 오류도 출력하지 않고 쿼리 결과 리스트도 제공하지 않을 때  Blind SQL 인젝션이 사용된다.

Blind SQL 인젝션은 쿼리 결과의 참/거짓으로부터 DB값을 유출해 내는 기법이다. 이 공격을 수행하려면, 먼저 웹 애플리케이션에서 쿼리 결과에 대해 참/거짓을 반환하는 요소를 찾아야 한다. 예를 들어 'ID 찾기'나 '게시판 검색'과 같은 기능에서 참/거짓을 판별하는 요소를 찾을 수 있다.



#### 2-1. Boolean-based Blind 공격

가령 어느 웹사이트가 게시판 검색이라는 기능을 제공할 경우, 게시판 검색 기능을 참/거짓을 반환하는 요소로 사용할 수 있다. 여기에 AND 조건으로 해커가 알고 싶은 쿼리 조건을 삽입해서 그 결과로부터 정보유출이 가능한 것이 Blind SQL 인젝션 공격 기법이며 이중에서도 **AND 조건에 논리식을 대입하여 참/거짓 여부를 알아내는 방식**이다.

```
[ 외부 입력값 ]
제목검색:hello' AND 1=1--(유효한 검색단어와 항상 참이되는 조건 부여)

[결과]
게시판 검색됨  -->참(true)이으로 간주---
```

#### 2-2. Time-based Blind 공격

응답의 결과가 항상 동일하여 응답결과만으로는 참/거짓을 판별할 수 없는 경우 시간을 지연시키는 쿼리를 주입하여 응답 시간의 차이로 참/거짓 여부를 판별할 수 있다.





## **방어 방법**

**1. input 값을 받을 때, 특수문자 여부 검사하기**

로그인 전, 검증 로직을 추가하여 미리 설정한 특수문자들이 들어왔을 때 요청을 막아낸다.

**2. SQL 서버 오류 발생 시, 해당하는 에러 메시지 감추기**

view를 활용하여 원본 데이터베이스 테이블에는 접근 권한을 높인다. 일반 사용자는 view로만 접근하여 에러를 볼 수 없도록 만든다.

**3. preparestatement 사용하기**

preparestatement를 사용하면, 특수문자를 자동으로 escaping 해준다. (statement와는 다르게 쿼리문에서 전달인자 값을 ?로 받는 것) 이를 활용해 서버 측에서 필터링 과정을 통해서 공격을 방어한다.



### 참고 자료

[[웹보안\] SQL Injection](https://m.mkexdev.net/427)

[SQL Injection | 👨🏻‍💻 Tech Interview](https://gyoogle.dev/blog/computer-science/data-base/SQL Injection.html)