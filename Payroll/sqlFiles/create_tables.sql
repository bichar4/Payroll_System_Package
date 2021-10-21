DROP DATABASE IF EXISTS `payroll_management_system` ;
CREATE DATABASE `payroll_management_system`;
USE `payroll_management_system`;


CREATE TABLE `Employee_details` (
  `emp_id` int NOT NULL AUTO_INCREMENT UNIQUE,
  `ssn` varchar(10) DEFAULT NULL,
  `full_name` varchar(30) NOT NULL,
  `Address` varchar(50) NOT NULL,
  `Email` varchar(70) NOT NULL,
  `PhoneNo` varchar(15) NOT NULL,
  PRIMARY KEY (`emp_id`)
);

CREATE TABLE `leaves` (
  `leaveId` int NOT NULL AUTO_INCREMENT UNIQUE,
  `emp_id` int DEFAULT NULL,
  `From_Date` date DEFAULT NULL,
  `To_Date` date DEFAULT NULL,
  `Reason` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`leaveId`),
  KEY `empodfk_idx` (`emp_id`),
  CONSTRAINT `emp_id` FOREIGN KEY (`emp_id`) REFERENCES `Employee_details` (`emp_id`)
);

CREATE TABLE `Organization` (
  `org_id` int NOT NULL AUTO_INCREMENT UNIQUE,
  `org_name` varchar(20) DEFAULT NULL,
  `Address` varchar(40) DEFAULT NULL,
  `PhoneNo` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`org_id`)
);

CREATE TABLE `Department` (
  `dept_id` int NOT NULL AUTO_INCREMENT UNIQUE,
  `Dept_Name` varchar(20) DEFAULT NULL,
  `org_id` int NOT NULL,
  PRIMARY KEY (`dept_id`),
  KEY `org_id_idx` (`org_id`),
  CONSTRAINT `org_id` FOREIGN KEY (`org_id`) REFERENCES `Organization` (`org_id`)
);


CREATE TABLE `Contract` (
  `contract_id` int NOT NULL AUTO_INCREMENT UNIQUE,
  `emp_id` int NOT NULL,
  `dept_id` int NOT NULL,
  `JobPosition` varchar(30) DEFAULT NULL,
  `basicPay` numeric(9,2) NOT NULL,
  `isPartTime` boolean DEFAULT 0,
  `no_of_hours` int DEFAULT 8,
  `join_date` date NOT NULL,
  PRIMARY KEY (`contract_id`),
  KEY `emp_dfk_idx` (`emp_id`),
  KEY `dept_id_idx` (`dept_id`),
  CONSTRAINT `dept_id` FOREIGN KEY (`dept_id`) REFERENCES `Department` (`dept_id`),
  CONSTRAINT `emp_idk` FOREIGN KEY (`emp_id`) REFERENCES `Employee_details` (`emp_id`)
);


CREATE TABLE `Allowance` (
  `allowance_id` int NOT NULL AUTO_INCREMENT UNIQUE,
  `DA` numeric(9,2) DEFAULT NULL,
  `HRA` numeric(9,2) DEFAULT NULL,
  `MA` numeric(9,2) DEFAULT NULL,
  `hostel` numeric(9,2) DEFAULT NULL,
  `bus` numeric(9,2) DEFAULT NULL,
  `security` numeric(9,2) DEFAULT NULL,
  `welfare` numeric(9,2) DEFAULT NULL,
  `others` numeric(9,2) DEFAULT NULL,
  `contract_id` int NOT NULL,
  PRIMARY KEY (`allowance_id`),
  CONSTRAINT `contract_id` FOREIGN KEY (`contract_id`) REFERENCES `Contract`(`contract_id`)
);

CREATE TABLE `Payroll` (
  `PayrollId` int NOT NULL AUTO_INCREMENT UNIQUE,
  `payrollamount` int NOT NULL,
  `PayrollDate` date NOT NULL,
  `contract_ids` int DEFAULT NULL,
  PRIMARY KEY (`PayrollId`),
  CONSTRAINT `contract_ids` FOREIGN KEY (`contract_ids`) REFERENCES `Contract` (`contract_id`)
);


