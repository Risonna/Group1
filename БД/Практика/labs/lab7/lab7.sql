--zadanie 1
CREATE SEQUENCE DEPT_ID_SEQ
INCREMENT BY 1
START WITH 76
MAXVALUE 80
NOCACHE
NOCYCLE;
--zadanie 2
CREATE SEQUENCE WORKER_ID_SEQ
INCREMENT BY 1
START WITH 204
MAXVALUE 9999999
CACHE 5
NOCYCLE;
--zadanie 3
SELECT cache_size, max_value, 
increment_by, last_number
FROM user_sequences
WHERE SEQUENCE_NAME LIKE 'WORKER_ID_SEQ'
OR SEQUENCE_NAME LIKE 'DEPT_ID_SEQ';
--zadanie 4
INSERT INTO DEPARTMENT(ID, NAME)
VALUES (DEPT_ID_SEQ.NEXTVAL, 'Education');
INSERT INTO DEPARTMENT(ID, NAME)
VALUES (DEPT_ID_SEQ.NEXTVAL, 'Administration');

SELECT *
FROM DEPARTMENT;

SELECT cache_size, max_value,
increment_by, last_number
FROM user_sequences
WHERE SEQUENCE_NAME LIKE 'WORKER_ID_SEQ'
OR SEQUENCE_NAME LIKE 'DEPT_ID_SEQ';
--zadanie 5
ALTER TABLE WORKER ADD TITLE CHAR(25);

SELECT *
FROM WORKER;

SELECT *
FROM DEPARTMENT;

INSERT INTO WORKER(ID, LAST_NAME, FIRST_NAME, DEPT_ID, TITLE)
VALUES (WORKER_ID_SEQ.NEXTVAL, 'Lira', 'Tomas', DEPT_ID_SEQ.CURRVAL, 'president');

INSERT INTO DEPARTMENT(ID, NAME)
VALUES (DEPT_ID_SEQ.NEXTVAL, 'Finance');

INSERT INTO WORKER(ID, LAST_NAME, FIRST_NAME, DEPT_ID, TITLE)
VALUES (WORKER_ID_SEQ.NEXTVAL, 'Seigher', 'Anna', DEPT_ID_SEQ.CURRVAL, 'vice president');

SELECT cache_size, max_value,
increment_by, last_number
FROM user_sequences
WHERE SEQUENCE_NAME LIKE 'WORKER_ID_SEQ'
OR SEQUENCE_NAME LIKE 'DEPT_ID_SEQ';
--zadanie 6
CREATE INDEX worker_dept_id_idx
ON WORKER(DEPT_ID);

CREATE INDEX worker_last_name_idx
ON WORKER(LAST_NAME);
--zadanie 7
SELECT ic.index_name, ix.uniqueness
FROM user_indexes ix, user_ind_columns ic
WHERE ic.index_name = ix.index_name
AND ic.table_name = 'WORKER' OR ic.table_name = 'DEPARTMENT';
--zadanie 8
ALTER TABLE WORKER
DROP PRIMARY KEY;

SELECT ic.index_name, ix.uniqueness
FROM user_indexes ix, user_ind_columns ic
WHERE ic.index_name = ix.index_name
AND ic.table_name = 'WORKER' OR ic.table_name = 'DEPARTMENT';
--zadanie 9
ALTER TABLE WORKER ADD CONSTRAINT worker_id_pk PRIMARY KEY (ID);

SELECT ic.index_name, ix.uniqueness
FROM user_indexes ix, user_ind_columns ic
WHERE ic.index_name = ix.index_name
AND ic.table_name = 'WORKER' OR ic.table_name = 'DEPARTMENT';
--zadanie 10
DROP INDEX worker_last_name_idx;

SELECT ic.index_name, ix.uniqueness
FROM user_indexes ix, user_ind_columns ic
WHERE ic.index_name = ix.index_name
AND ic.table_name = 'WORKER' OR ic.table_name = 'DEPARTMENT';
