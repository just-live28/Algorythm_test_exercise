SELECT warehouse_id,
       warehouse_name,
       address,
       Ifnull(freezer_yn, 'N') AS FREEZER_YN
FROM   food_warehouse
WHERE  address LIKE '경기도%' 