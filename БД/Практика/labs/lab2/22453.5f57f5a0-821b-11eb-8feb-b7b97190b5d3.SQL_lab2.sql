--1
SELECT MAX(total), MIN(total)
FROM s_ord;
--2
SELECT title, MIN(salary), MAX(salary)
FROM s_emp
GROUP BY title
ORDER BY title ASC;
--3
SELECT COUNT(DISTINCT(manager_id))
FROM s_emp;
--4
SELECT ord_id, COUNT(*) "Number of items"
FROM S_ITEM
GROUP BY ord_id
ORDER BY 1,2 ASC;
--5
SELECT manager_id, MIN(salary)
FROM s_emp
WHERE manager_id IS NOT NULL
GROUP BY manager_id
HAVING MIN(salary) > 1000
ORDER BY MIN(salary) ASC;
--6
SELECT MAX(salary)-MIN(salary)
FROM S_EMP;
--7
SELECT product_id, COUNT(*) "Times Ordered"
FROM s_item
GROUP BY product_id
HAVING COUNT(*) >=3
ORDER BY 1 ASC;
--8
SELECT COUNT(s_dept.id) "Number of departments", s_region.id "Region ID"
FROM s_region, S_DEPT
WHERE s_dept.region_id = S_REGION.ID
GROUP BY s_region.id;
--9
SELECT s_customer.id "Customer ID", COUNT(s_ord.id) "Number of orders"
FROM s_customer, S_ORD
WHERE s_customer.id = s_ord.CUSTOMER_ID
GROUP BY s_customer.ID;
--10
SELECT TO_CHAR(start_date, 'yyyy') "Start date", COUNT(id) "Number of emloyees"
FROM s_emp
GROUP BY START_DATE