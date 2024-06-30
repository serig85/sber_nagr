--------------------------------------------------------
--  File created - воскресенье-июня-30-2024   
--------------------------------------------------------
--------------------------------------------------------
--  DDL for Table CLIENT
--------------------------------------------------------

  CREATE TABLE "C##SERG"."CLIENT" 
   (	"ID" NUMBER(10,0), 
	"FIRST_NAME" VARCHAR2(20 BYTE), 
	"LAST_NAME" VARCHAR2(20 BYTE), 
	"MIDDLE_NAME" VARCHAR2(20 BYTE)
   ) SEGMENT CREATION IMMEDIATE 
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 
 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
--------------------------------------------------------
--  DDL for Table CREDIT
--------------------------------------------------------

  CREATE TABLE "C##SERG"."CREDIT" 
   (	"ID" NUMBER(10,0), 
	"CREDIT_NUMBER" NUMBER(10,0), 
	"AMOUNT" NUMBER(10,0), 
	"BALANCE" NUMBER(10,0)
   ) SEGMENT CREATION IMMEDIATE 
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 
 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
--------------------------------------------------------
--  DDL for Table RELATION
--------------------------------------------------------

  CREATE TABLE "C##SERG"."RELATION" 
   (	"ID" NUMBER(3,0), 
	"CLIENT" NUMBER(3,0), 
	"CREDIT" NUMBER(3,0)
   ) SEGMENT CREATION IMMEDIATE 
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 
 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
REM INSERTING into C##SERG.CLIENT
SET DEFINE OFF;
Insert into C##SERG.CLIENT (ID,FIRST_NAME,LAST_NAME,MIDDLE_NAME) values ('1','Smith','John','Alexander');
Insert into C##SERG.CLIENT (ID,FIRST_NAME,LAST_NAME,MIDDLE_NAME) values ('2','Brown','Olivia','Emma');
Insert into C##SERG.CLIENT (ID,FIRST_NAME,LAST_NAME,MIDDLE_NAME) values ('3','Taylor','Sophia','Michael');
Insert into C##SERG.CLIENT (ID,FIRST_NAME,LAST_NAME,MIDDLE_NAME) values ('4','Anderson','James','William');
Insert into C##SERG.CLIENT (ID,FIRST_NAME,LAST_NAME,MIDDLE_NAME) values ('5','Martinez','Isabella','David');
Insert into C##SERG.CLIENT (ID,FIRST_NAME,LAST_NAME,MIDDLE_NAME) values ('6','Wilson','Emily','Benjamin');
Insert into C##SERG.CLIENT (ID,FIRST_NAME,LAST_NAME,MIDDLE_NAME) values ('7','Garcia','Ava','Matthew');
Insert into C##SERG.CLIENT (ID,FIRST_NAME,LAST_NAME,MIDDLE_NAME) values ('8','Lewis','Lily','Jacob');
Insert into C##SERG.CLIENT (ID,FIRST_NAME,LAST_NAME,MIDDLE_NAME) values ('9','Moore','Grace','Christopher');
Insert into C##SERG.CLIENT (ID,FIRST_NAME,LAST_NAME,MIDDLE_NAME) values ('10','Patel','Mia','Ethan');
Insert into C##SERG.CLIENT (ID,FIRST_NAME,LAST_NAME,MIDDLE_NAME) values ('11','abt','ghj','fff');
REM INSERTING into C##SERG.CREDIT
SET DEFINE OFF;
Insert into C##SERG.CREDIT (ID,CREDIT_NUMBER,AMOUNT,BALANCE) values ('10','888','888','1111');
Insert into C##SERG.CREDIT (ID,CREDIT_NUMBER,AMOUNT,BALANCE) values ('1','875','1985','1043');
Insert into C##SERG.CREDIT (ID,CREDIT_NUMBER,AMOUNT,BALANCE) values ('2','1667','1912','281');
Insert into C##SERG.CREDIT (ID,CREDIT_NUMBER,AMOUNT,BALANCE) values ('3','1393','1206','1577');
Insert into C##SERG.CREDIT (ID,CREDIT_NUMBER,AMOUNT,BALANCE) values ('4','1906','1747','1604');
Insert into C##SERG.CREDIT (ID,CREDIT_NUMBER,AMOUNT,BALANCE) values ('5','264','102','1315');
Insert into C##SERG.CREDIT (ID,CREDIT_NUMBER,AMOUNT,BALANCE) values ('6','1042','1525','990');
Insert into C##SERG.CREDIT (ID,CREDIT_NUMBER,AMOUNT,BALANCE) values ('7','1730','691','720');
Insert into C##SERG.CREDIT (ID,CREDIT_NUMBER,AMOUNT,BALANCE) values ('8','1270','608','539');
Insert into C##SERG.CREDIT (ID,CREDIT_NUMBER,AMOUNT,BALANCE) values ('9','815','719','542');
REM INSERTING into C##SERG.RELATION
SET DEFINE OFF;
Insert into C##SERG.RELATION (ID,CLIENT,CREDIT) values ('1','2','5');
Insert into C##SERG.RELATION (ID,CLIENT,CREDIT) values ('2','3','4');
Insert into C##SERG.RELATION (ID,CLIENT,CREDIT) values ('3','8','8');
Insert into C##SERG.RELATION (ID,CLIENT,CREDIT) values ('4','4','10');
Insert into C##SERG.RELATION (ID,CLIENT,CREDIT) values ('5','9','3');
Insert into C##SERG.RELATION (ID,CLIENT,CREDIT) values ('6','3','1');
Insert into C##SERG.RELATION (ID,CLIENT,CREDIT) values ('7','1','7');
Insert into C##SERG.RELATION (ID,CLIENT,CREDIT) values ('8','8','2');
Insert into C##SERG.RELATION (ID,CLIENT,CREDIT) values ('9','7','9');
Insert into C##SERG.RELATION (ID,CLIENT,CREDIT) values ('10','7','6');
--------------------------------------------------------
--  Constraints for Table CLIENT
--------------------------------------------------------

  ALTER TABLE "C##SERG"."CLIENT" MODIFY ("ID" NOT NULL ENABLE);
--------------------------------------------------------
--  Constraints for Table CREDIT
--------------------------------------------------------

  ALTER TABLE "C##SERG"."CREDIT" MODIFY ("ID" NOT NULL ENABLE);
--------------------------------------------------------
--  Constraints for Table RELATION
--------------------------------------------------------

  ALTER TABLE "C##SERG"."RELATION" MODIFY ("ID" NOT NULL ENABLE);
  ALTER TABLE "C##SERG"."RELATION" MODIFY ("CLIENT" NOT NULL ENABLE);
  ALTER TABLE "C##SERG"."RELATION" MODIFY ("CREDIT" NOT NULL ENABLE);
