#WAP to creaate database wuh python and mysql
import mysql.connector as m
mym = m.connect(host="localhost",user="root",passwd="root",database="python")
cursor = mym.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS students(id INT NOT NULL AUTO_INCREMENT,name VARCHAR(50),age INT,PRIMARY KEY(id))")
cursor.execute("INSERT INTO students(name,age) VALUES('John',25)")
cursor.execute("INSERT INTO students(name,age) VALUES('Tom',30)")
cursor.execute("INSERT INTO students(name,age) VALUES('Peter',35)")
cursor.execute("INSERT INTO students(name,age) VALUES('Sarah',40)")
cursor.execute("INSERT INTO students(name,age) VALUES('Michael',45)")
cursor.execute("INSERT INTO students(name,age) VALUES('Jenny',50)")
mym.commit()
mym.close()
rows = cursor.fetchall()
for row in rows:
    print(row)

#WAP to create employee database using mysql and input 5 employees' details
import mysql.connector as m
mym = m.connect(host="localhost",user="root",passwd="root",database="employee")
cursor = mym.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS employee(id INT NOT NULL AUTO_INCREMENT,name VARCHAR(50),salary INT,PRIMARY KEY(id))")
for i in range(5):
    name = input("Enter name of employee: ")
    salary = int(input("Enter salary of employee: "))
    cursor.execute("INSERT INTO employee(name,salary) VALUES(%s,%s)",(name,salary))
mym.commit()
mym.close()

#WAP to display the details of all employees using curcor
import mysql.connector as m
mym = m.connect(host="localhost",user="root",passwd="root",database="employee")
cursor = mym.cursor()
cursor.execute("SELECT * FROM employee")
rows = cursor.fetchall()
for row in rows:
    print(row)

#WAP to search employee using employee id entered by the user
import mysql.connector as m
mym = m.connect(host="localhost",user="root",passwd="root",database="employee")
cursor = mym.cursor()
id = int(input("Enter employee id: "))
cursor.execute("SELECT * FROM employee WHERE id=%s",(id))
rows = cursor.fetchall()
for row in rows:
    print(row)

#WAP to update employee salary using employee id entered by the user
import mysql.connector as m
mym = m.connect(host="localhost",user="root",passwd="root",database="employee")
cursor = mym.cursor()
id = int(input("Enter employee id: "))
salary = int(input("Enter new salary: "))
cursor.execute("UPDATE employee SET salary=%s WHERE id=%s",(salary,id))
mym.commit()
mym.close()