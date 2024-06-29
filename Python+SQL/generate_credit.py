import random
import cx_Oracle

conn = cx_Oracle.connect(user="SYS", password='123', dsn='orcl1', mode = cx_Oracle.SYSDBA)
cur = conn.cursor()
def rnd():
    return int(random.uniform(0, 2000))

for i in range(10):
    cur.execute(f'INSERT INTO "SYS"."CREDIT" (ID, CREDIT_NUMBER, AMOUNT, BALANCE) VALUES ({i+1}, {rnd()}, {rnd()}, {rnd()})')
conn.commit()