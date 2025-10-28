SELECT F.CATEGORY,
       MAX_PRICE,
       PRODUCT_NAME
FROM   FOOD_PRODUCT AS F
       JOIN (SELECT CATEGORY,
                    Max(PRICE) AS MAX_PRICE
             FROM   FOOD_PRODUCT
             WHERE  CATEGORY IN ( '과자', '국', '김치', '식용유' )
             GROUP  BY CATEGORY) AS P
         ON F.CATEGORY = P.CATEGORY
            AND F.PRICE = P.MAX_PRICE
ORDER  BY MAX_PRICE DESC 