# Aksharkumar Patel

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="devroot#",
    database="Company"
)

#print(mydb)

mycursor = mydb.cursor() # obj that communicates with mysql server

# Query #1 - Q4
print("Query 1")

deptName = input("Enter a department name to retrive all the names and salaries of all employees in that department: ")

mycursor.execute("SELECT FirstName, LastName, Salary FROM Employee, Department WHERE DeptName= '"+deptName+"' AND Department.DeptNo=Employee.DeptNo")
for q1 in mycursor:
	print(q1)

print("\n")

# Query #2 - Q5
print("Query 2")

lName = input("Enter an employee last name: ")
fName = input("Enter an employee first name: ") 

mycursor.execute("SELECT ProjectName, Hours FROM Project, WorksOn, Employee WHERE Employee.LastName='"+lName+"' AND Employee.FirstName='"+fName+"' AND Employee.EmpNo = WorksOn.EmpNo AND WorksOn.ProjectNo = Project.ProjectNo")
for q2 in mycursor:
	print(q2)

print("\n")

# Query #3 - Q6
print("Query 3")
mycursor.execute("ALTER TABLE Employee MODIFY Salary INTEGER")
DepartmentName = input("Enter a department name and retrieve the total of all employee salaries who work in the department: ") 
mycursor.execute("SELECT SUM(Salary) FROM Employee, Department WHERE DeptName='"+DepartmentName+"' AND Department.ManagerNo=Employee.SupervisorNo")
for q3 in mycursor:
 	print(q3)

print("\n")

# Query #4 - Q7 
print("Query 4")
mycursor.execute("SELECT DeptName, COUNT(*) FROM Department INNER JOIN Employee ON Employee.SupervisorNo = Department.ManagerNo GROUP BY Department.ManagerNo, DeptName ORDER BY COUNT(*) DESC")
for q4 in mycursor:
	print(q4)

print("\n")

#Query #5 - Q8
print("Query 5")
mycursor.execute("SELECT FirstName, LastName FROM Employee WHERE SupervisorNo IS NULL ")
for q5 in mycursor:
	print(q5)

