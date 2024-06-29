import random
import cx_Oracle

conn = cx_Oracle.connect(user="SYS", password='123', dsn='orcl1', mode = cx_Oracle.SYSDBA)
cur = conn.cursor()
l = [i+1 for i in range(10)]
l2 = l.copy()
def rnd():
    v = random.choice(l)
    l.remove(v)
    return int(v)

for i in range(10):
    cur.execute(f'INSERT INTO "SYS"."RELATION" (ID, Client, Credit) VALUES ({i+1}, {random.choice(l2)}, {rnd()})')
conn.commit()
print(l)