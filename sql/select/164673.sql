SELECT a.title,
       a.board_id,
       b.reply_id,
       b.writer_id,
       b.contents,
       Date_format(b.created_date, '%Y-%m-%d') CREATED_DATE
FROM   (SELECT *
        FROM   used_goods_board
        WHERE  Year(created_date) = 2022
               AND Month(created_date) = 10) AS a
       JOIN used_goods_reply AS b
         ON a.board_id = b.board_id
ORDER  BY b.created_date,
          a.title 