SELECT ID,
       CASE RANK_TILE
         WHEN 1 THEN 'CRITICAL'
         WHEN 2 THEN 'HIGH'
         WHEN 3 THEN 'MEDIUM'
         WHEN 4 THEN 'LOW'
       END AS COLONY_NAME
FROM   (SELECT ID,
               NTILE(4)
                 OVER (
                   ORDER BY SIZE_OF_COLONY DESC) AS RANK_TILE
        FROM   ECOLI_DATA) AS T
ORDER  BY ID 