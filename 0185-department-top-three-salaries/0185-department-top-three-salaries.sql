WITH R AS (
    SELECT id
        , name
        , salary
        , departmentId
        , DENSE_RANK() OVER (
            PARTITION BY departmentId
            ORDER BY salary DESC
        ) AS salary_rank
    FROM Employee
),
P AS (
    SELECT DISTINCT departmentId
        , salary
        , name
    FROM R
    WHERE salary_rank <= 3
)

SELECT D.name Department
     , P.name Employee
     , P.salary Salary
FROM P
JOIN Department D
ON P.departmentId = D.id
ORDER BY P.salary DESC
;