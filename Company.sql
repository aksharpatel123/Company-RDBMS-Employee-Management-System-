CREATE DATABASE Company;
USE Company;
        
CREATE TABLE Employee (
        FirstName varchar(255),
        MiddleName varchar(255),
        LastName varchar(255),
        EmpNo varchar(255),
        BDate varchar(255),
        Street varchar(255),
        City varchar(255),
        State varchar(255),
        Gender varchar(255),
        Salary varchar(255),
        SupervisorNo varchar(255),
        DeptNo varchar(255)
        );
SELECT * FROM Employee;

CREATE TABLE WorksOn (
        EmpNo varchar(255),
        ProjectNo varchar(255),
        Hours varchar(255)
        );
SELECT * FROM WorksOn;

CREATE TABLE Project (
        ProjectName varchar(255),
        ProjectNo varchar(255),
        loc varchar(255),
        DeptNo varchar(255)
        );
SELECT * FROM Project;

CREATE TABLE Dep_Location (
        DeptNo varchar(255),
        loc varchar(255)
        );
        
SELECT * FROM Dep_Location;
 
CREATE TABLE Department (
        DeptName varchar(255),
        DeptNo varchar(255),
        ManagerNo varchar(255),
        startDate varchar(255)
        );

SELECT * FROM Department;
