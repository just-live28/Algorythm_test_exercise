SELECT E.EMP_NO,
       EMP_NAME,
       GRADE,
       CASE
         WHEN GRADE = 'S' THEN SAL * 0.2
         WHEN GRADE = 'A' THEN SAL * 0.15
         WHEN GRADE = 'B' THEN SAL * 0.1
         ELSE 0
       END AS BONUS
FROM   HR_EMPLOYEES AS E
       JOIN (SELECT EMP_NO,
                    CASE
                      WHEN Avg(SCORE) >= 96 THEN 'S'
                      WHEN Avg(SCORE) >= 90 THEN 'A'
                      WHEN Avg(SCORE) >= 80 THEN 'B'
                      ELSE 'C'
                    END AS GRADE
             FROM   HR_GRADE
             GROUP  BY EMP_NO) AS G
         ON E.EMP_NO = G.EMP_NO
ORDER  BY EMP_NO 