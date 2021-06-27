--1
select id, last_name|| '('||title||')' "last_name (title)", round(salary*1.15) "salary"
from s_emp;
--2
Select name 
from s_customer 
where lower(name) like '%sport';
--3(1)
Select name 
from s_product 
where name like 'Pro%' order by name asc;
--3(2)
select name, short_desc 
from s_product 
where lower(short_desc) like '%ski%';
--4(1)
select name, ID, credit_rating 
from s_customer 
where sales_rep_id = 11;
--4(2)
select name "Company", ID "Company ID", credit_rating "Rating" 
from s_customer 
WHERE sales_rep_id = 11;
--5(1) DESCRIBE s_emp;
--5(2)
select first_name || ' ' || last_name "Employees", dept_id
FROM s_emp
where dept_id = 10 OR dept_id = 50 ORDER BY last_name ASC;
--5(3)
select first_name, start_date
from S_EMP
where start_date BETWEEN TO_DATE('14-05-1990', 'dd-mm-yyyy') AND TO_DATE('26-05-1991', 'dd-mm-yyyy') order BY START_DATE DESC;
--5(4)
SELECT last_name  "Employee Name", salary "MONTHLY SALARY"
from s_emp
WHERE (dept_id = 31 or dept_id = 42 OR dept_id = 50) and salary BETWEEN 1000 AND 2500;
--6
SELECT last_name || ' is paid ' || salary || ' per month, but wants to get paid ' || salary*3 || ' per month '
from s_emp;
--7
select last_name, floor(months_between(SYSDATE, start_date)) "months have passed",
to_char(start_date, 'day') "day of hiring"
from s_emp
ORDER by 2 DESC;
--8
SELECT last_name, TO_CHAR(start_date, 'fmdd.fmmm.fmyyyy') "Start Date", TO_CHAR(NEXT_DAY(ADD_MONTHS(start_date, 6), 'MONDAY'), 'fmdd.fmmm.fmyyyy') "Date of salary change"
from s_emp;