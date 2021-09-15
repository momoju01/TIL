-- 주석
/* SQL 구문은 대소문자 구분x (중요)
  스타일가이드
  기본 문법(변하지 않는 부분 - 대문자)
  변하는 부분 - 소문자
 */
-- 데이터 전체 조회 SELECT

SELECT * FROM examples;  
select * from examples;

-- 테이블 생성
CREATE TABLE classmates (
id INTEGER PRIMARY KEY,
name TEXT
);

-- 테이블 삭제
DROP TABLE classmates;

-- 테이블 생성 실습
CREATE TABLE  classmates (
name TEXT NOT NULL,
age INT NOT NULL,
address TEXT NOT NULL
);

-- 데이터 입력
INSERT INTO classmates(name, age, address) VALUES ('홍길동', 23, '서울');
INSERT INTO classmates VALUES 
('홍길동', 30, '서울'),
('김철수', 30, '대전'),
('이싸피', 25, '광주'),
('박삼성', 26, '구미'),
('최전자', 24, '부산');
INSERT INTO classmates(name, age, address) VALUES ('최전자', 24, '부산');

SELECT * FROM classmates;
SELECT rowid, * FROM classmates;
SELECT rowid, name FROM classmates;
SELECT rowid, name FROM classmates LIMIT 1;
SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;
SELECT rowid, name FROM classmates WHERE address='서울';
SELECT DISTINCT age FROM classmates;

-- 테이블 삭제
DROP TABLE classmates;

-- 데이터 삭제
DELETE FROM classmates WHERE rowid=5;

-- 데이터 수정(update)
UPDATE classmates SET 
name='홍길동', 
address='제주도' 
WHERE rowid=5;

CREATE TABLE users (
first_name TEXT NOT NULL,
last_name TEXT NOT NULL,
age INTEGER NOT NULL,
country TEXT NOT NULL,
phone TEXT NOT NULL,
balance INTEGER NOT NULL
);

SELECT * FROM users WHERE age >=30;
SELECT first_name FROM users WHERE age >=30;
SELECT age, last_name FROM users WHERE age >= 30 AND last_name == '김';


SELECT COUNT(*) FROM users;
SELECT AVG(age) FROM users WHERE age >= 30;

SELECT first_name, MAX(balance) FROM users;