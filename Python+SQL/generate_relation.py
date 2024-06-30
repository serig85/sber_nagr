import random
import cx_Oracle
from config_base import authorization_data as ad

conn = cx_Oracle.connect(user=ad.user_name, password=ad.user_pass, dsn=ad.dsn)
cur = conn.cursor()
count_credit = [i+1 for i in range(10)]
client_list = count_credit.copy()


def rnd():
    v = random.choice(count_credit)
    count_credit.remove(v)
    return int(v)


for i in range(10):
    cur.execute(f'INSERT INTO "C##SERG"."RELATION" (ID, Client, Credit)'
                f' VALUES ({i+1}, {random.choice(client_list)}, {rnd()})')
conn.commit()
print(count_credit)
