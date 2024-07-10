'''Test task'''
import csv
import datetime
from cx_Oracle import connect
from config_base import authorization_data as ad

conn = connect(user=ad.user_name, password=ad.user_pass, dsn=ad.dsn)

date = datetime.date.today().strftime('%d.%m.%Y')
with open(f'report_{date}.csv', 'a' , encoding='utf-8') as file:
    file_writer = csv.writer(file, delimiter=',', lineterminator="\r")
    file_writer.writerow(['first_name', 'last_name', 'Credit_Number', 'Balance'])
    cur = conn.cursor()
    for row in cur.execute("SELECT first_name, last_name, Credit_Number, Balance FROM client "
                           "JOIN relation on client.id = relation.client "
                           "JOIN credit ON credit = credit.id "
                           "WHERE Balance >1000"):
        print(row)
        file_writer.writerow(row)
