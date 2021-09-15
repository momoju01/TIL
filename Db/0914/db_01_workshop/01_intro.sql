CREATE TABLE countries (
room_num TEXT,
check_in TEXT,
check_out TEXT,
grade TEXT,
price INTEGER
);

INSERT INTO countries VALUES 
('B203', '2019-12-31', '2020-01-03', 'suite', 900),
('1102', '2020-01-04', '2020-01-08', 'suite', 850),
('303', '2020-01-01', '2020-01-03', 'deluxe', 500),
('807', '2020-01-04', '2020-01-07', 'superior', 300)
;

SELECT * FROM countries;

--테이블 이름 변경
ALTER TABLE countries RENAME TO hotels;

--내림차순 조회
SELECT room_num, price FROM hotels ORDER BY price DESC LIMIT 2;

--GROUP 후 ORDER
SELECT grade, COUNT(*) FROM hotels GROUP BY grade ORDER BY COUNT(*) DESC;

--OR 
SELECT * FROM hotels WHERE room_num LIKE 'B%' OR grade='deluxe';

--AND
SELECT * FROM hotels WHERE room_num NOT LIKE 'B%' AND check_in = '2020-01-04';



-- 2. sql orm 비교