# 첫번째 풀이
-- SELECT CONCAT('/home/grep/src/', BOARD_ID, '/', FILE_ID, FILE_NAME, FILE_EXT) AS
--        FILE_PATH
-- FROM   USED_GOODS_FILE
-- WHERE  BOARD_ID = (SELECT BOARD_ID
--                    FROM   USED_GOODS_BOARD
--                    ORDER  BY VIEWS DESC
--                    LIMIT  1)
-- ORDER  BY FILE_ID DESC 

# 두번째 풀이
-- SELECT CONCAT('/home/grep/src/', B.BOARD_ID, '/', F.FILE_ID, F.FILE_NAME,
--        F.FILE_EXT)
--        AS FILE_PATH
-- FROM   USED_GOODS_BOARD AS B
--        JOIN USED_GOODS_FILE AS F
--          ON B.BOARD_ID = F.BOARD_ID
-- WHERE  B.VIEWS = (SELECT Max(VIEWS)
--                   FROM   USED_GOODS_BOARD)
-- ORDER  BY F.FILE_ID DESC 

SELECT CONCAT('/home/grep/src/', RANKED.BOARD_ID, '/', RANKED.FILE_ID,
       RANKED.FILE_NAME, RANKED.FILE_EXT) AS FILE_PATH
FROM   (SELECT B.BOARD_ID,
               B.VIEWS,
               F.FILE_ID,
               F.FILE_NAME,
               F.FILE_EXT,
               RANK()
                 OVER (
                   ORDER BY B.VIEWS DESC) AS rnk
        FROM   USED_GOODS_BOARD AS B
               JOIN USED_GOODS_FILE F
                 ON B.BOARD_ID = F.BOARD_ID) AS RANKED
WHERE  RANKED.RNK = 1
ORDER  BY RANKED.FILE_ID DESC; 