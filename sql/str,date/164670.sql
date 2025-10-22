# 첫번째 풀이
-- SELECT USER_ID,
--        NICKNAME,
--        CONCAT(CITY, ' ', STREET_ADDRESS1, ' ', STREET_ADDRESS2) 전체주소,
--        CONCAT(SUBSTR(TLNO, 1, 3), '-', SUBSTR(TLNO, 4, 4), '-',
--        SUBSTR(TLNO, 8, 4))
--        전화번호
-- FROM   USED_GOODS_USER
-- WHERE  USER_ID IN (SELECT WRITER_ID
--                    FROM   USED_GOODS_BOARD
--                    GROUP  BY WRITER_ID
--                    HAVING Count(WRITER_ID) >= 3)
-- ORDER  BY USER_ID DESC 

SELECT U.USER_ID,
       U.NICKNAME,
       CONCAT(U.CITY, ' ', U.STREET_ADDRESS1, ' ', U.STREET_ADDRESS2) AS
       전체주소,
       CONCAT(SUBSTR(U.TLNO, 1, 3), '-', SUBSTR(U.TLNO, 4, 4), '-',
       SUBSTR(U.TLNO, 8, 4))                                          AS
       전화번호
FROM   USED_GOODS_USER AS U
       JOIN USED_GOODS_BOARD AS B
         ON U.USER_ID = B.WRITER_ID
GROUP  BY B.WRITER_ID
HAVING Count(B.WRITER_ID) >= 3
ORDER  BY U.USER_ID DESC 