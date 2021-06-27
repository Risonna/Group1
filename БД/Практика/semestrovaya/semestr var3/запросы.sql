--1
SELECT last_name, first_name
FROM medical_employee
WHERE position = 'surgeon';
--4
SELECT last_name, first_name
FROM medical_employee
WHERE position = 'surgeon' AND experience > 12;
--6
SELECT last_name, first_name, receipt_date, diagnosis
FROM patients
WHERE CHAMBER_ID = 10;
--Количество больных в мед. Учреждениях:
select est.name, count(pt.last_name) "кол-во"
from patients pt, chambers ch, med_department dep, hospitals hos, medical_establishment est
where pt.chamber_id = ch.chamber_id and ch.department_id = dep.department_id
and dep.hospital_id = hos.hospital_id and hos.establishment_id = est.establishment_id
group by est.name
