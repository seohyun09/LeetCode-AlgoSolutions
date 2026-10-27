WITH T AS (
    SELECT product_id
        , new_price
        , RANK() OVER (
            PARTITION BY product_id
            ORDER BY change_date DESC
        ) AS date_rank
        , change_date
    FROM Products
    WHERE change_date <= '2019-08-16'
),
R AS (
    SELECT P.product_id
        , IFNULL(T.new_price, 10) price
        , IFNULL(T.date_rank, 1) date_rank
    FROM (
        SELECT DISTINCT product_id
        FROM Products
    ) P
    LEFT JOIN T
    ON P.product_id = T.product_id
)

SELECT product_id
     , price
FROM R
WHERE date_rank = 1
;