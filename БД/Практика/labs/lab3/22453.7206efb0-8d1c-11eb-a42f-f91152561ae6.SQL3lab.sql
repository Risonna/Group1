--1.1
SELECT employee.last_name, employee.dept_id, dept.name
FROM s_emp employee, S_DEPT dept
WHERE employee.dept_id = dept.ID;
--1.2
SELECT employee.last_name, dept.name, region.name, employee.COMMISSION_PCT
FROM s_emp employee, S_DEPT dept, s_region region
WHERE employee.dept_id = dept.ID AND dept.region_id = region.id AND employee.COMMISSION_PCT IS NOT NULL;
--2
SELECT employee.last_name, dept.name
FROM S_EMP employee, s_dept dept
WHERE employee.LAST_NAME like 'Smith' AND employee.DEPT_ID = dept.ID;
--3
SELECT product.name, product.ID, item.QUANTITY
FROM S_PRODUCT product, s_item item
WHERE item.ord_id = 106 AND item.product_id = product.id;
--4
SELECT customer.id "Customer ID", customer.name, ord.id "Order ID"
FROM s_customer customer, s_ord ord
WHERE customer.id = ord.customer_id(+);
--5
SELECT worker.last_name "Worker's Last Name", worker.id, manager.last_name "Manager's Last Name", manager.id
FROM s_emp worker, s_emp manager
WHERE worker.manager_id = manager.id;
--6
SELECT cust.name, ord.id, sum(item.quantity) "amount of products ordered"
FROM s_ord ord, s_customer cust, s_item item
WHERE ord.customer_id = cust.id AND item.ord_id = ord.id AND ord.total > 100000
GROUP BY cust.name, ord.id;
--7
SELECT region.id, region.name
FROM s_region region, s_dept dept
WHERE dept.region_id = region.id;
--8
SELECT cust.name "Customer's name", COUNT(ord.id)
FROM s_customer cust, s_ord ord
WHERE ord.customer_id = cust.id
GROUP BY cust.name;
--9
SELECT product.name, COUNT(ord.id)
FROM s_product product, s_item item, s_ord ord
WHERE ord.id = item.ord_id AND item.product_id = product.id
GROUP BY product.name
HAVING COUNT(ord.id) > 2;
--10
SELECT ord.id, SUM(item.quantity)
FROM s_item item, s_ord ord
WHERE item.ord_id = ord.id
GROUP BY ord.id
HAVING SUM(item.quantity) >= 100;