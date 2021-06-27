SET SQLBLANKLINES ON;
drop table medical_employee  cascade constraints;

drop table medical_establishment cascade constraints;

drop table hospitals cascade constraints;

drop table med_department cascade constraints;

drop table doctor_to_department cascade constraints;

drop table chambers cascade constraints;

drop table patients cascade constraints;

/*==============================================================*/
/* Table: medical_employee                                      */
/*==============================================================*/


create table medical_employee 
(
   EMPLOYEE_ID   NUMBER(7) NOT NULL CONSTRAINT EMP_ID_PK PRIMARY KEY,
   EXPERIENCE    NUMBER(7) NOT NULL,
   POSITION      VARCHAR(255),
   LAST_NAME     VARCHAR(30),
   FIRST_NAME    VARCHAR(30),
   PATRONYMIC    VARCHAR(20)
);

/*==============================================================*/
/* Table: medical_establishment                                 */
/*==============================================================*/


create table medical_establishment
(
   ESTABLISHMENT_ID   NUMBER(7) NOT NULL CONSTRAINT EST_ID_PK PRIMARY KEY,
   NAME VARCHAR(255) NOT NULL,
   ADRESS VARCHAR(100) NOT NULL
);

/*==============================================================*/
/* Table: hospitals                                             */
/*==============================================================*/


create table hospitals
(
    HOSPITAL_ID   NUMBER(7) NOT NULL,
     ESTABLISHMENT_ID    NUMBER(7) NOT NULL  CONSTRAINT EST_ID_FK REFERENCES medical_establishment (ESTABLISHMENT_ID),
     NUMBER_OF_CHAMBERS NUMBER(7) NOT NULL,
     NUMBER_OF_BEDS NUMBER(7) NOT NULL,
     CONSTRAINT HOST_PK PRIMARY KEY (HOSPITAL_ID, ESTABLISHMENT_ID)
);

/*==============================================================*/
/* Table: med_department                                        */
/*==============================================================*/


create table med_department 
(
   DEPARTMENT_ID  NUMBER(7) NOT NULL CONSTRAINT DEP_ID_PK PRIMARY KEY,
   ESTABLISHMENT_ID   NUMBER(7) NOT NULL,
   HOSPITAL_ID      NUMBER(7) NOT NULL,
   CASE_NUMBER NUMBER(7) NOT NULL,
   NUMBER_OF_CHAMBERS NUMBER(7) NOT NULL,
   NUMBER_OF_BEDS NUMBER(7) NOT NULL,

   CONSTRAINT MED_DEP_FK FOREIGN KEY (ESTABLISHMENT_ID, HOSPITAL_ID) REFERENCES hospitals (ESTABLISHMENT_ID, HOSPITAL_ID)
);


/*==============================================================*/
/* Table: doctor_to_department                                  */
/*==============================================================*/


create table doctor_to_department
(
   ID   NUMBER(7) NOT NULL CONSTRAINT dct_id_pk PRIMARY KEY,
   DEPARTMENT_ID    NUMBER(7) NOT NULL REFERENCES med_department(DEPARTMENT_ID) ,
   EMPLOYEE_ID NUMBER (7) NOT NULL REFERENCES medical_employee(EMPLOYEE_ID)
);

/*==============================================================*/
/* Table: chambers                                              */
/*==============================================================*/


create table chambers 
(
   CHAMBER_ID    NUMBER(7) NOT NULL CONSTRAINT CHAM_ID_PK PRIMARY KEY,
   DEPARTMENT_ID NUMBER(7) NOT NULL REFERENCES med_department (DEPARTMENT_ID),
   CHAMBER_NUMBER NUMBER (7) NOT NULL
);

/*==============================================================*/
/* Table: patients                                              */
/*==============================================================*/


create table patients 
(
   PATIENT_ID   NUMBER(7) NOT NULL CONSTRAINT PAT_ID_PK PRIMARY KEY,
   CHAMBER_ID NUMBER (7) NOT NULL REFERENCES chambers (CHAMBER_ID),
   RECEIPT_DATE DATE,
   DIAGNOSIS VARCHAR(255),
   LAST_NAME VARCHAR(30),
   FIRST_NAME  VARCHAR(30),
   PATRONYMIC    VARCHAR(20),
   BIRTH_DAY DATE
);