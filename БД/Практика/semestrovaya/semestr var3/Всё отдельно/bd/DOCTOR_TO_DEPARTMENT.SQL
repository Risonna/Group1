create table doctor_to_department
(
   ID   NUMBER(7) NOT NULL CONSTRAINT dct_id_pk PRIMARY KEY,
   DEPARTMENT_ID    NUMBER(7) NOT NULL REFERENCES medical_department(DEPARTMENT_ID) ,
   EMPLOYEE_ID NUMBER (7) NOT NULL REFERENCES Medical_Employee(EMPLOYEE_ID)
)
/