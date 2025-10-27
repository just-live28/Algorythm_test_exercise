SELECT H.HISTORY_ID,
       TRUNCATE(C.DAILY_FEE * H.TOTAL_DAY * ( 100 - IFNULL(P.DISCOUNT_RATE, 0) )
                / 100,
       0) AS FEE
FROM   (SELECT HISTORY_ID,
               CAR_ID,
               TIMESTAMPDIFF(DAY, START_DATE, END_DATE) + 1 AS TOTAL_DAY,
               CASE
                 WHEN TIMESTAMPDIFF(DAY, START_DATE, END_DATE) + 1 >= 90 THEN
                 '90일 이상'
                 WHEN TIMESTAMPDIFF(DAY, START_DATE, END_DATE) + 1 >= 30 THEN
                 '30일 이상'
                 WHEN TIMESTAMPDIFF(DAY, START_DATE, END_DATE) + 1 >= 7 THEN
                 '7일 이상'
                 ELSE NULL
               END                                          AS DURATION
        FROM   CAR_RENTAL_COMPANY_RENTAL_HISTORY) AS H
       JOIN CAR_RENTAL_COMPANY_CAR AS C
         ON H.CAR_ID = C.CAR_ID
       LEFT JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN AS P
              ON C.CAR_TYPE = P.CAR_TYPE
                 AND DURATION = P.DURATION_TYPE
WHERE  C.CAR_TYPE = '트럭'
ORDER  BY FEE DESC,
          H.HISTORY_ID DESC 