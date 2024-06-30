import random
import cx_Oracle
from config_base import authorization_data as ad


conn = cx_Oracle.connect(user=ad.user_name, password=ad.user_pass, dsn=ad.dsn)
cur = conn.cursor()


def rnd():
    return int(random.uniform(0, 2000))


for i in range(10):
    cur.execute(f'INSERT INTO "C##SERG"."CREDIT" (ID, CREDIT_NUMBER, AMOUNT, BALANCE) VALUES '
                f'({i+1}, {rnd()}, {rnd()}, {rnd()})')
conn.commit()
