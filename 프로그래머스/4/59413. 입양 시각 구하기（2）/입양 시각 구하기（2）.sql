-- 코드를 입력하세요
-- DATETIME에 없는 시간도 넣어야하기 때문에 재귀함수 이용
-- 0부터 23까지 숫자를 생성하는 재귀 테이블 정의
WITH RECURSIVE TIME_TABLE AS(
    SELECT 0 AS HOUR
    -- UNION은 중복을 제거 하므로, 애초에 중복 값이
    -- 발생하지 않는 상황인데 효율성에서 떨어짐
    -- UNION으로 인해 재귀적 연산이 멈추거나
    -- 오작동할 수 있다.
    UNION ALL
    SELECT HOUR+1 FROM TIME_TABLE WHERE HOUR<23
    )

--
SELECT T.HOUR AS HOUR,COUNT(HOUR(DATETIME))
FROM TIME_TABLE T LEFT JOIN ANIMAL_OUTS A
ON T.HOUR=HOUR(A.DATETIME)
GROUP BY HOUR
ORDER BY HOUR