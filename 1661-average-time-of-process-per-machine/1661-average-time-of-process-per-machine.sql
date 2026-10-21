WITH S AS (
    SELECT machine_id, process_id, timestamp
    FROM Activity
    WHERE activity_type = 'start'
), 
E AS (
    SELECT machine_id, process_id, timestamp
    FROM Activity
    WHERE activity_type = 'end'
),
T AS (
    SELECT S.machine_id
        , S.process_id
        , E.timestamp - S.timestamp timestamp
    FROM S
    JOIN E
    ON S.machine_id = E.machine_id AND S.process_id = E.process_id
)

SELECT machine_id
     , ROUND(AVG(timestamp), 3) processing_time
FROM T
GROUP BY machine_id
;