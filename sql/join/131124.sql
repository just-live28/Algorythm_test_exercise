WITH MAX_COUNT_MEMBERS
     AS (SELECT MEMBER_ID
         FROM   (SELECT MEMBER_ID,
                        RANK()
                          OVER (
                            ORDER BY Count(MEMBER_ID) DESC) AS RNK
                 FROM   REST_REVIEW
                 GROUP  BY MEMBER_ID) AS T
         WHERE  RNK = 1)
SELECT MEMBER_NAME,
       REVIEW_TEXT,
       DATE_FORMAT(REVIEW_DATE, '%Y-%m-%d') AS REVIEW_DATE
FROM   REST_REVIEW AS R
       JOIN MEMBER_PROFILE AS M
         ON R.MEMBER_ID = M.MEMBER_ID
WHERE  R.MEMBER_ID IN (SELECT *
                       FROM   MAX_COUNT_MEMBERS)
ORDER  BY REVIEW_DATE,
          REVIEW_TEXT 