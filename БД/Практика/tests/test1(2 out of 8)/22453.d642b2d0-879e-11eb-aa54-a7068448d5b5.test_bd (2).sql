--1 "в указанном отделе - в dept.name like '%' вместо % нужно указать требуемый отдел.
SELECT emp.id "Saler's ID", emp.last_name "Last Name", emp.FIRST_NAME "Name", emp.SALARY "Salary", emp.COMMISSION_PCT "Commision PCT", dept.name "Department Name"
FROM s_emp emp, s_dept dept
WHERE dept.name LIKE '%' AND emp.DEPT_ID = dept.id AND emp.title LIKE '%er%';
--2
SELECT emp.id "Saler's ID", emp.last_name "Last Name", emp.dept_id "Dept ID", TO_CHAR(emp.start_date, 'dd.mm.yyyy') "Start Date"
FROM s_emp emp
--WHERE emp.title LIKE 'Sales Representative' or emp.title LIKE 'VP, Sales'
order BY to_char(emp.start_date, 'D');
--3
SELECT ord.id "Order ID", ord.CUSTOMER_ID "Customer ID"
FROM s_ord ord
WHERE ord.total >= 300 AND ord.total <= 2700 AND ord.DATE_ORDERED BETWEEN TO_DATE('11.06.1989', 'DD.MM.YYYY') AND TO_DATE('21.11.1993', 'DD.MM.YYYY');
