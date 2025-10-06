SELECT a.flavor
FROM   first_half AS a
       INNER JOIN icecream_info AS b
               ON a.flavor = b.flavor
WHERE  a.total_order > 3000
       AND b.ingredient_type = 'fruit_based'
ORDER  BY a.total_order DESC 