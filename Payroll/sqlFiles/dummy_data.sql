INSERT INTO `Employee_details` VALUES (1011,'456','Hedley Dunn','303, prince street','laoreet.ipsum.curabitur@rc.org','98632463'),(1025,'489','Jordan Summers','948-5836 Proin St.','sem@consequat.net','73418501'),(1065,'412','Talon Conley','173-8456 Tellus St.','in@egetipsum.net','72142878'),(1098,'487','Ursa Joseph','Ap #731-6938 Vulputate, St.','tellus@dictum.org','34587365'),(1099,'456','Emily Ward','867-2637 Posuere, Road','felis.purus@nonummyfusce.com','5469978');

INSERT INTO `Organization` (`org_id`,`Org_Name`,`Address`,`PhoneNo`) VALUES
  (5001,"Google","California",9084171908),
  (5002,"Facebook","Sanfrancisco",9701682844);
  
Insert into `Department` (`dept_id`, `Dept_Name`,`org_id`) values
(6001,"Sales",5001),
(6002,"Production",5002),
(6003,"Sales",5002),
(6004,"Marketing",5001);

INSERT INTO `payroll_management_system`.`leaves` (`leaveId`, `emp_id`, `From_Date`, `To_Date`) VALUES ('5011', '1011', '2021-02-12', '2021-02-13');
INSERT INTO `payroll_management_system`.`leaves` (`leaveId`, `emp_id`, `From_Date`, `To_Date`) VALUES ('5012', '1025', '2021-03-13', '2021-03-15');
INSERT INTO `payroll_management_system`.`leaves` (`leaveId`, `emp_id`, `From_Date`, `To_Date`) VALUES ('5013', '1065', '2021-03-05', '2021-03-07');
INSERT INTO `payroll_management_system`.`leaves` (`leaveId`, `emp_id`, `From_Date`, `To_Date`) VALUES ('5014', '1098', '2021-09-06', '2021-09-07');
INSERT INTO `payroll_management_system`.`leaves` (`leaveId`, `emp_id`, `From_Date`, `To_Date`) VALUES ('5015', '1099', '2021-05-03', '2021-05-04');
INSERT INTO `payroll_management_system`.`leaves` (`leaveId`, `emp_id`, `From_Date`, `To_Date`) VALUES ('5016', '1099', '2021-05-09', '2021-05-14');

INSERT INTO `Contract` (`contract_id`,`emp_id`,`dept_id`,`JobPosition`,`basicpay`,`join_date`)
VALUES
  (609,1011,6001,"Manager",13800.00,'2019-02-12'),
  (610,1025,6002,"CEO",11200.00,'2018-02-12'),
  (611,1065,6003,"HR",10600.00,'2019-02-12'),
  (612,1098,6004,"Software Developer",10600.00,'2019-02-12'),
  (613,1099,6001,"Tester",10600.00,'2019-02-12');


INSERT INTO `Allowance` (`allowance_id`,`DA`,`HRA`,`MA`,`hostel`,`bus`,`security`,`welfare`,`others`,`contract_id`)
VALUES
  (114,200.00,1700.00,2000.00,2100.00,-900.00,-400.00,-100.00,-100.00,609),
  (115,300.00,1900.00,2000.00,2020.00,-600.00,-400.00,-100.00,-100.00,610),
  (116,200.00,1200.00,1200.00,2100.00,-900.00,-400.00,-100.00,-100.00,611),
  (117,400.00,1600.00,1500.00,2440.0,-700.00,-100.00,-100.00,-100.00,612),
  (118,200.00,1500.00,1900.00,2380.00,-800.00,-300.00,-100.00,-100.00,613);