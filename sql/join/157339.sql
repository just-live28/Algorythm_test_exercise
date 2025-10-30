WITH C
     AS (SELECT CAR.CAR_ID,
                CAR.CAR_TYPE,
                TRUNCATE(CAR.DAILY_FEE * 30 * ( 100 - PLAN.DISCOUNT_RATE ) / 100
                , 0)
                AS
                   FEE
         FROM   CAR_RENTAL_COMPANY_CAR AS CAR
                JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN AS PLAN
                  ON CAR.CAR_TYPE = PLAN.CAR_TYPE
                     AND DURATION_TYPE = '30일 이상'
         WHERE  CAR.CAR_TYPE IN ( '세단', 'SUV' ))
         
SELECT *
FROM   C
WHERE  NOT EXISTS (SELECT 1
                   FROM   CAR_RENTAL_COMPANY_RENTAL_HISTORY AS H
                   WHERE  H.CAR_ID = C.CAR_ID
                          AND H.START_DATE <= '2022-11-30'
                          AND H.END_DATE >= '2022-11-01')
       AND FEE BETWEEN 500000 AND 1999999
ORDER  BY FEE DESC,
          CAR_TYPE ASC,
          CAR_ID DESC 