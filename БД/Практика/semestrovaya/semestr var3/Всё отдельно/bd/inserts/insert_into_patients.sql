SET SQLBLANKLINES ON;

INSERT INTO patients
(PATIENT_ID, CHAMBER_ID, RECEIPT_DATE, DIAGNOSIS, LAST_NAME, FIRST_NAME, PATRONYMIC, BIRTH_DAY)
VALUES
(111, 10, to_date('11.05.2020','dd.mm.yyyy'), 'fracture', 'Kirov', 'Mark', 'Petrovich', to_date('11.05.2000','dd.mm.yyyy') );

INSERT INTO patients
(PATIENT_ID, CHAMBER_ID, RECEIPT_DATE, DIAGNOSIS, LAST_NAME, FIRST_NAME, PATRONYMIC, BIRTH_DAY)
VALUES
(112, 11, to_date('01.12.2020','dd.mm.yyyy'), 'fracture', 'Krakov', 'Andrey', 'Andreevich', to_date('13.04.1900','dd.mm.yyyy') );

INSERT INTO patients
(PATIENT_ID, CHAMBER_ID, RECEIPT_DATE, DIAGNOSIS, LAST_NAME, FIRST_NAME, PATRONYMIC, BIRTH_DAY)
VALUES
(113, 12, to_date('18.11.2020','dd.mm.yyyy'), 'fracture', 'Limonov', 'Kirill', 'Kirillovich', to_date('29.03.1990','dd.mm.yyyy') );