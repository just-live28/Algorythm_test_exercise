WITH FE AS
(
       SELECT Sum(CODE) AS CODE
       FROM   SKILLCODES
       WHERE  CATEGORY='Front End'), PY AS
(
       SELECT CODE
       FROM   SKILLCODES
       WHERE  NAME='Python'), CS AS
(
       SELECT CODE
       FROM   SKILLCODES
       WHERE  NAME='C#')

SELECT
         CASE
                  WHEN SKILL_CODE & FE.CODE > 0
                  AND      SKILL_CODE & PY.CODE > 0 THEN 'A'
                  WHEN SKILL_CODE & CS.CODE > 0 THEN 'B'
                  WHEN SKILL_CODE & FE.CODE > 0 THEN 'C'
         END AS GRADE,
         ID,
         EMAIL
FROM     DEVELOPERS AS D
JOIN     FE
JOIN     PY
JOIN     CS
HAVING   GRADE IS NOT NULL
ORDER BY GRADE,
         ID