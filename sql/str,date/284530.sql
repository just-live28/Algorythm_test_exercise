SELECT Year(YM)               AS YEAR,
       Round(Avg(PM_VAL1), 2) AS PM10,
       Round(Avg(PM_VAL2), 2) AS 'PM2.5'
FROM   AIR_POLLUTION
WHERE  LOCATION2 = '수원'
GROUP  BY YEAR
ORDER  BY YEAR 