# 첫번째 풀이
-- SELECT DATE_FORMAT(SALES_DATE, '%Y-%m-%d') AS SALES_DATE,
--        PRODUCT_ID,
--        USER_ID,
--        Sum(SALES_AMOUNT)                   AS SALES_AMOUNT
-- FROM   (SELECT USER_ID,
--                PRODUCT_ID,
--                SALES_AMOUNT,
--                SALES_DATE
--         FROM   ONLINE_SALE
--         UNION
--         SELECT NULL AS USER_ID,
--                PRODUCT_ID,
--                SALES_AMOUNT,
--                SALES_DATE
--         FROM   OFFLINE_SALE) AS T
-- WHERE  SALES_DATE BETWEEN '2022-03-01' AND '2022-03-31'
-- GROUP  BY SALES_DATE,
--           PRODUCT_ID,
--           USER_ID
-- ORDER  BY SALES_DATE,
--           PRODUCT_ID,
--           USER_ID

SELECT DATE_FORMAT(SALES_DATE, '%Y-%m-%d') AS SALES_DATE,
       PRODUCT_ID,
       USER_ID,
       SALES_AMOUNT
FROM   ONLINE_SALE
WHERE  SALES_DATE BETWEEN '2022-03-01' AND '2022-03-31'
UNION
SELECT DATE_FORMAT(SALES_DATE, '%Y-%m-%d') AS SALES_DATE,
       PRODUCT_ID,
       NULL                                AS USER_ID,
       SALES_AMOUNT
FROM   OFFLINE_SALE
WHERE  SALES_DATE BETWEEN '2022-03-01' AND '2022-03-31'
ORDER  BY 1,
          2,
          3 