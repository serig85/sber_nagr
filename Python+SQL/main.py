import csv
import datetime
import cx_Oracle


conn = cx_Oracle.connect(user="SYS", password='123', dsn='orcl1', mode=cx_Oracle.SYSDBA)

date = datetime.date.today().strftime('%d.%m.%Y')
with open(f'report_{date}.csv', 'a') as file:
    file_writer = csv.writer(file, delimiter=',', lineterminator="\r")
    file_writer.writerow(['first_name', 'last_name', 'Credit_Number', 'Balance'])
    cur = conn.cursor()
    for row in cur.execute("SELECT first_name, last_name, Credit_Number, Balance "
                           "FROM (SELECT * FROM client JOIN relation on client.id = relation.client) "
                           " JOIN credit ON credit = credit.id WHERE Balance >1000"):
        print(row)
        file_writer.writerow(row)
