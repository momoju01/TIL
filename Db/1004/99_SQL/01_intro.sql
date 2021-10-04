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


-- 데이터 조회 SELECT - LIMIT, OFFSET
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



-- users 테이블 생성: 
CREATE TABLE users(
first_name TEXT NOT NULL,
last_name TEXT NOT NULL, 
age INTEGER NOT NULL,
country TEXT NOT NULL,
phone TEXT NOT NULL, 
balance INTEGER NOT NULL
);

-- 조건 상세 설정 WHERE
SELECT * FROM users WHERE age >= 30;
SELECT name FROM users WHERE age >= 30;
SELECT age, last_name FROM users WHERE age >= 30 AND last_nam='김';







-- 107.page Sqlite Functions
-- 레코드의 개수 조회 : 1000
SELECT COUNT(*) FROM users;

-- Q. 30살 이상인 사람들의 평균 나이? : 35.1763285024155
SELECT AVG(age) FROM users WHERE age >=30;

-- Q. 계좌 잔액이 가장 높은 사람과 그 액수 : "순옥",1000000
SELECT first_name, MAX(balance) FROM users;

-- Q. 나이가 30 이상인 사람의 계좌 평균 잔액 : 153541.425120773
SELECT AVG(balance) FROM users WHERE age >= 30;



-- LIKE
-- % : 0개 이상
-- _ : 임의의 단일 문자
-- Q. users 테이블에서 나이가 20대인 사람만 조회
SELECT * FROM users WHERE age LIKE '2_';
-- Q. users 테이블에서 지역번호가 02인 사람만 조회
SELECT COUNT(*) FROM users WHERE phone LIKE '02%';
SELECT * FROM users WHERE first_name LIKE '%준';
SELECT * FROM users WHERE phone LIKE '%5114%';


-- ORDER BY : ASC, DESC
SELECT * FROM users ORDER BY age ASC;
SELECT age, balance FROM users ORDER BY age, balance DESC;  --age는 ASC(기본값), balance DESC
SELECT * FROM users ORDER BY age ASC LIMIT 10;
SELECT * FROM users ORDER BY age ASC, last_name ASC LIMIT 10;
SELECT last_name, first_name FROM users ORDER BY balance DESC LIMIT 10;


-- GROUP BY :
SELECT last_name, COUNT(*) FROM users GROUP BY last_name;
SELECT last_name, COUNT(*) AS name_count FROM users GROUP BY last_name;


-- -----------------------------------

-- ALTER TABLE 
CREATE TABLE articles (
title TEXT NOT NULL,
content TEXT NOT NULL
);

INSERT INTO articles VALUES ('1번 제목', '1번 내용');

ALTER TABLE articles RENAME TO news;
ALTER TABLE news ADD COLUMN created_at TEXT NOT NULL;
/* 에러 발생 : 테이블에 있던 기존 레코드들에는 
새로 추가할 필드에 대한 정보가 없다.
그렇기 때문에 NOT NULL 형태의 컬럼은 추가가 불가능하다
해결 방법 2 가지
1. NOT NULL 설정 없이 추가하기 
2. 기본값(DEFAULT) 설정하기
*/

--1. NOT NULL 설정 없이 추가하기 
ALTER TABLE news ADD COLUMN created_at TEXT;
INSERT INTO news VALUES ('제목', '내용', datetime('now'));

--2. 기본값(DEFAULT) 설정하기
ALTER TABLE news ADD COLUMN subtitle TEXT NOT NULL DEFAULT '임시제목';