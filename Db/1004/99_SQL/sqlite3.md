```sql
-- $ sqlite3 tutorial.sqlite3
-- .database
-- .mode csv
-- .import hellodb.csv examples :hellodb.csv 가져와서 examples라는 tables생성
-- .tables : 테이블 조회


-- 터미널 view 변경:
-- .heders on
-- .mode column 


-- 특정 테이블의 schema 조회:
-- .schema classmates



-- 데이터 전체 조회 SELECT(DML) 
SELECT * FROM examples;  


--(DDL)
-- 테이블 생성 CREATE
CREATE TABLE classmates (
id INTEGER PRIMARY KEY,
name TEXT
);

CREATE TABLE classmates (
name TEXT NOT NULL,
age INT NOT NULL,
address TEXT NOT NULL
);



-- 테이블 삭제 DROP
DROP TABLE classmates;


-- (DML)
-- 데이터 입력 INSERT
INSERT INTO classmates (name, age) VALUES ('홍길동', 23);
INSERT INTO classmates VALUES ('홍길동', 30, '서울');
INSERT INTO classmates VALUES (1, '홍길동', 30, '서울');
INSERT INTO classmates (name, age, address) VALUES ('홍길동', 30, '서울');
INSERT INTO classmates VALUES 
('홍길동', 30, '서울'),
('김철수', 30, '대전'),
('이싸피', 26, '광주'),
('박삼성', 29, '구미'),
('최전자', 28, '부산');


-- 데이터 조회 with rowid
SELECT rowid, * FROM classmates;


-- 데이터 조회 SELECT
SELECT rowid, name FROM classmates;
SELECT rowid, name FROM classmates LIMIT 1;
SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;
SELECT rowid, name FROM classmates WHERE address='서울';
SELECT DISTINCT age FROM classmates ;


-- 데이터 삭제
DELETE FROM classmates WHERE rowid=5;

-- pk 중복되지 않게 테이블 생성 AUTOINCREMENT
CREATE TABLE classmates (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
age INT NOT NULL,
address TEXT NOT NULL
);


-- 데이터 수정 UPDATE
UPDATE classmates SET 
name='홍길동', 
address='제주도'
WHERE rowid=5;



-- users 테이블 생성: first_name, last_name age country phone balance
-- 조건 상세 설정 WHERE
SELECT * FROM users WHERE age >= 30;
SELECT name FROM users WHERE age >= 30;
SELECT age, last_name FROM users WHERE age >= 30 AND last_nam='김';

```

