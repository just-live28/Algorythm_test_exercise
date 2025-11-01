WITH RECURSIVE GEN AS
(
       SELECT ID,
              PARENT_ID,
              1 AS GENERATION
       FROM   ECOLI_DATA
       WHERE  PARENT_ID IS NULL
       UNION ALL
       SELECT E.ID,
              E.PARENT_ID,
              GEN.GENERATION+1
       FROM   ECOLI_DATA AS E
       JOIN   GEN
       ON     E.PARENT_ID=GEN.ID )
SELECT   COUNT(*) AS COUNT,
         GENERATION
FROM     GEN
WHERE    NOT EXISTS
         (
                SELECT 1
                FROM   ECOLI_DATA AS ED
                WHERE  GEN.ID=ED.PARENT_ID)
GROUP BY GENERATION
ORDER BY GENERATION