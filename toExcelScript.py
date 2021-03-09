import pandas as pd 


def Employee_csv():
    colNames = ['Fname', 'Mname', 'Lname', 'EmpNumber', 'DOB.', 'Address', 'Gender', 'Salary', 'SupervisorNo.', 'DeptNo']
    data = pd.read_csv('EMPLOYEE.txt', delimiter=', ', names = colNames, engine='python')
    # data.to_csv('EMPLOYEE_1.csv', index = False)
    #replacing the columns with null :
    # print(data.isnull().sum())
    newDataFile = data.fillna(value='NULL')
    newDataFile.to_csv('EMPLOYEE.csv', index = False)

def WorksOn_csv():
    colNames = ['EmpNo', 'ProjectNo', 'Hours']
    data = pd.read_csv('WORKS_ON.txt', delimiter=', ', names = colNames, engine='python')
    #replacing the columns with null :
    # print(data.isnull().sum())
    newDataFile = data.fillna(value='NULL')
    newDataFile.to_csv('WORKS_ON.csv', index = False)

def Project_csv():
    colNames = ['Name', 'ProjectNo', 'loc', 'DeptNo']
    data = pd.read_csv('PROJECT.txt', delimiter=', ', names = colNames, engine='python')
    # replacing the columns with null :
    # print(data.isnull().sum())
    newDataFile = data.fillna(value='NULL')
    newDataFile.to_csv('PROJECT.csv', index = False)

def DepLocation_csv():
    colNames = ['DeptNo', 'loc']
    data = pd.read_csv('DEPT_LOCATIONS.txt', delimiter=', ', names = colNames, engine='python')
    # replacing the columns with null :
    # print(data.isnull().sum())
    newDataFile = data.fillna(value='NULL')
    newDataFile.to_csv('DEPT_LOCATIONS.csv', index = False)

def Department():
    colNames = ['Name', 'loc', 'ManagerNo', 'startDate']
    data = pd.read_csv('DEPARTMENT.txt', delimiter=', ', names = colNames, engine='python')
    # replacing the columns with null :
    # print(data.isnull().sum())
    newDataFile = data.fillna(value='NULL')
    newDataFile.to_csv('DEPARTMENT.csv', index = False)


# Function Calls
Employee_csv()
WorksOn_csv()
Project_csv()
DepLocation_csv()
Department()