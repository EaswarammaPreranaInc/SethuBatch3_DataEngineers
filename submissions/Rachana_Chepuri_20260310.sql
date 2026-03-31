-- 1. Display employee name and department name using an INNER JOIN
SELECT e.emp_name, d.dept_name 
FROM employees_demo e 
INNER JOIN departments_demo d ON e.dept_id = d.dept_id;

-- 2. Display all employees and department names, even if the department does not exist (LEFT JOIN)
SELECT e.emp_name, d.dept_name 
FROM employees_demo e 
LEFT JOIN departments_demo d ON e.dept_id = d.dept_id;

-- 3. Display all departments and employees working in them (RIGHT JOIN)
SELECT d.dept_name, e.emp_name 
FROM employees_demo e 
RIGHT JOIN departments_demo d ON e.dept_id = d.dept_id;

-- 4. Display all employees and departments including unmatched rows (FULL JOIN using UNION)
SELECT e.emp_name, d.dept_name FROM employees_demo e LEFT JOIN departments_demo d ON e.dept_id = d.dept_id
UNION
SELECT e.emp_name, d.dept_name FROM employees_demo e RIGHT JOIN departments_demo d ON e.dept_id = d.dept_id;

-- 5. Display employee id, employee name, and department name sorted by employee name
SELECT e.emp_id, e.emp_name, d.dept_name 
FROM employees_demo e 
JOIN departments_demo d ON e.dept_id = d.dept_id 
ORDER BY e.emp_name;

-- 6. Display employees who belong to the IT department
SELECT e.emp_name 
FROM employees_demo e 
JOIN departments_demo d ON e.dept_id = d.dept_id 
WHERE d.dept_name = 'IT';

-- 7. Display employees who do not have a matching department (NULL values)
SELECT e.emp_name 
FROM employees_demo e 
LEFT JOIN departments_demo d ON e.dept_id = d.dept_id 
WHERE d.dept_id IS NULL;

-- 8. Display departments that do not have any employees
SELECT d.dept_name 
FROM departments_demo d 
LEFT JOIN employees_demo e ON d.dept_id = e.dept_id 
WHERE e.emp_id IS NULL;

-- 9. Display all possible combinations of employee names and department names
SELECT e.emp_name, d.dept_name 
FROM employees_demo e 
CROSS JOIN departments_demo d;

-- 10. Count how many rows are produced by the CROSS JOIN
SELECT COUNT(*) 
FROM employees_demo 
CROSS JOIN departments_demo;

-- 11. Display department id and number of employees in each department
SELECT dept_id, COUNT(*) AS emp_count 
FROM employees_demo 
GROUP BY dept_id;

-- 12. Display department name and number of employees working in each (JOIN + GROUP BY)
SELECT d.dept_name, COUNT(e.emp_id) AS emp_count 
FROM departments_demo d 
LEFT JOIN employees_demo e ON d.dept_id = e.dept_id 
GROUP BY d.dept_name;

-- 13. Display departments with more than one employee (HAVING)
SELECT dept_id, COUNT(*) 
FROM employees_demo 
GROUP BY dept_id 
HAVING COUNT(*) > 1;

-- 14. Display departments with exactly two employees
SELECT dept_id, COUNT(*) 
FROM employees_demo 
GROUP BY dept_id 
HAVING COUNT(*) = 2;

-- 15. Display departments where employee count is greater than 1
SELECT dept_id FROM employees_demo GROUP BY dept_id HAVING COUNT(*) > 1;

-- 16. Display departments where employee count is less than 2
SELECT dept_id FROM employees_demo GROUP BY dept_id HAVING COUNT(*) < 2;

-- 17. Display employees and departments ordered by department name
SELECT e.emp_name, d.dept_name 
FROM employees_demo e 
JOIN departments_demo d ON e.dept_id = d.dept_id 
ORDER BY d.dept_name;

-- 18. Display employees ordered by department id descending
SELECT * FROM employees_demo ORDER BY dept_id DESC;

-- 19. Display departments with employee count ordered by highest count first
SELECT dept_id, COUNT(*) as cnt 
FROM employees_demo 
GROUP BY dept_id 
ORDER BY cnt DESC;

-- 20. Display first 5 employees
SELECT * FROM employees_demo LIMIT 5;

-- 21. Display employees from row 6 to row 10 (LIMIT + OFFSET)
SELECT * FROM employees_demo LIMIT 5 OFFSET 5;

-- 22. Display 3 employees starting from the 4th row
SELECT * FROM employees_demo LIMIT 3 OFFSET 3;

-- 23. Display department-wise employee list but show only first 3 rows
SELECT e.emp_name, d.dept_name 
FROM employees_demo e 
JOIN departments_demo d ON e.dept_id = d.dept_id 
LIMIT 3;

-- 24. Display employee name and their manager name
SELECT e.emp_name AS Employee, m.emp_name AS Manager 
FROM employees_selfjoin e 
JOIN employees_selfjoin m ON e.manager_id = m.emp_id;

-- 25. Display employees who report to John
SELECT e.emp_name 
FROM employees_selfjoin e 
JOIN employees_selfjoin m ON e.manager_id = m.emp_id 
WHERE m.emp_name = 'John';

-- 26. Display employees who do not have a manager
SELECT emp_name 
FROM employees_selfjoin 
WHERE manager_id IS NULL;

-- 27. Display manager name and number of employees reporting to them
SELECT m.emp_name AS Manager, COUNT(e.emp_id) AS Direct_Reports 
FROM employees_selfjoin e 
JOIN employees_selfjoin m ON e.manager_id = m.emp_id 
GROUP BY m.emp_name;