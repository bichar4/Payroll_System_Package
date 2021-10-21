from Database import DB_CONFIG, Database


class Payroll:
    def __init__(self, backedUpFile=None, loadDummyData=True):
        self.myDb = Database(DB_CONFIG)
        if(not loadDummyData):
            self.myDb.switch_db(DB_CONFIG['db'])
        else:
            if(backedUpFile is None):
                self.myDb.executeSqlFile(
                    "../Payroll/sqlFiles/create_tables.sql")

                self.myDb.switch_db(DB_CONFIG['db'])
                self.myDb.executeSqlFile("../Payroll/sqlFiles/dummy_data.sql")
            else:
                print("No setting for backupSql provided Yet")
                exit(0)

    # get queries
    def getOrganizations(self):
        return self.myDb.executeSQLCommand("SELECT * FROM  Organization")

    def getEmployees(self):
        return self.myDb.executeSQLCommand("SELECT * FROM  Employee_details")

    def getEmployeesInOrg(self, orgId):
        query = """SELECT Department.Dept_Name, Employee_details.emp_id, Employee_details.full_name, Organization.org_name
            FROM Organization
            Inner JOIN Department ON Department.org_id=Organization.org_id
            Inner JOIN Contract ON Department.dept_id=Contract.dept_id
            Inner JOIN Employee_details ON Employee_details.emp_id=Contract.emp_id
            Where Organization.org_id=%s """
        return self.myDb.executeSQLCommand(query, orgId)

    def getDepartments(self, OrganizationId):
        if (self.myDb.executeSQLCommand("Select * FROM Organization WHERE org_id = %s", (OrganizationId))):
            return self.myDb.executeSQLCommand("Select * FROM Department WHERE org_id = %s", (OrganizationId))
        else:
            print("No such organizations exists")
            return None

    def getLeaves(self, employeeId):
        if self.myDb.executeSQLCommand("Select * FROM  Employee_details WHERE emp_id = %s", (employeeId)):
            return self.myDb.executeSQLCommand("Select * FROM  leaves WHERE emp_id = %s", (employeeId))
        else:
            print("No such Employees exists")
            return None

    def getLeaveDays(self, employeeId):
        return self.myDb.executeSQLCommand("select sum( DATEDIFF(To_Date, From_Date)) as days from leaves where emp_id = %s", (employeeId))

    # Queries for searching the Entities
    def searchEmployeeByName(self, name):
        return self.myDb.executeSQLCommand("SELECT emp_id,full_name FROM Employee_details WHERE full_name LIKE CONCAT('%%',%s,'%%')", (name))

    def searchOrganizationByName(self, name):
        return self.myDb.executeSQLCommand("SELECT org_id,org_name FROM Organization WHERE org_name LIKE CONCAT('%%',%s,'%%')", (name))

    # Queries for inserting the elements
    def insertEmployee(self, employee):
        query = "INSERT INTO `Employee_details` (ssn,full_name,Address,Email,PhoneNo) VALUES (%s,%s,%s,%s,%s)"
        self.myDb.executeSQLCommand(
            query, (employee['ssn'], employee['full_name'], employee['Address'], employee['email'], employee['phone']))
        return self.myDb.executeSQLCommand("SELECT LAST_INSERT_ID()")

    def insertOrganization(self, organization):
        query = "INSERT INTO `Organization` (`Org_Name`,`Address`,`PhoneNo`) VALUES (%s,%s,%s)"
        self.myDb.executeSQLCommand(
            query, (organization['Org_Name'], organization['Address'], organization['PhoneNo']))
        return self.myDb.executeSQLCommand("SELECT LAST_INSERT_ID()")

    def insertDepartment(self, department):
        query = "Insert into `Department` (`Dept_Name`,`org_id`) values (%s,%s)"
        self.myDb.executeSQLCommand(
            query, (department['Dept_Name'], department['org_id']))
        return self.myDb.executeSQLCommand("SELECT LAST_INSERT_ID()")

    def applyForLeave(self, emp_id, fromDate, toDate, reason=None):
        query = "INSERT INTO `leaves` ( `emp_id`, `From_Date`, `To_Date`) VALUES (%s,%s,%s);"
        self.myDb.executeSQLCommand(query, (emp_id, fromDate, toDate))
        return self.myDb.executeSQLCommand("SELECT LAST_INSERT_ID()")

    def hireEmployee(self, employee, departmentId, position, basicPay, join_date, allowance):
        emp_id = self.insertEmployee(employee)[0]['LAST_INSERT_ID()']
        contract_query = "INSERT INTO `Contract` (`emp_id`,`dept_id`,`JobPosition`,`basicpay`,`join_date`) VALUES (%s,%s,%s,%s,%s)"
        self.myDb.executeSQLCommand(
            contract_query, (emp_id, departmentId, position, basicPay, join_date))
        contract_id = self.myDb.executeSQLCommand("SELECT LAST_INSERT_ID()")[
            0]['LAST_INSERT_ID()']
        allowance_query = "INSERT INTO `Allowance` (`DA`,`HRA`,`MA`,`hostel`,`bus`,`security`,`welfare`,`others`,`contract_id`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        self.myDb.executeSQLCommand(allowance_query, (allowance["dearness"], allowance["house_rent"], allowance["medical"],
                                    allowance["hostel"], allowance["bus"], allowance["security"], allowance["welfare"], allowance["other"], contract_id))
        return self.myDb.executeSQLCommand("SELECT LAST_INSERT_ID()")

    def generatePayROll(self, employeeId, date, days):
        totalquery = """ Select emp_id,total,contract_id from (select E.emp_id, total,contract_id from Employee_details inner join
                (select emp_id,contract_id,(C.basicPay+A.HRA+A.DA+A.MA+A.hostel+A.bus+A.security+A.welfare+A.others) as total from Contract C
                natural join Allowance A) as E
                on E.emp_id = Employee_details.emp_id)as A  where A.emp_id = %s;
                """
        totalPay = self.myDb.executeSQLCommand(totalquery, (employeeId))
        payAmount = (days/30)*float(totalPay[0]['total'])
        insertQuery = "INSERT INTO `Payroll` (`payrollamount`,`PayrollDate`,`contract_ids`) VALUES (%s,%s,%s);"
        self.myDb.executeSQLCommand(
            insertQuery, (payAmount, date, totalPay[0]['contract_id']))
        return self.myDb.executeSQLCommand("SELECT LAST_INSERT_ID()")

    def getEmployeePayRollHistory(self, employeeId):
        contractIdQuery = "select contract_id from Contract where emp_id = %s;"
        contractId = self.myDb.executeSQLCommand(
            contractIdQuery, (employeeId))[0]['contract_id']
        payrollQuery = "select payrollamount, PayrollDate  from Payroll where contract_ids = %s;"
        return self.myDb.executeSQLCommand(payrollQuery, (contractId))

    def test(self):
        # print(self.getOrganizations())

        department = {
            "Dept_Name": "Research",
            "org_id": 5002
        }

        print(self.insertDepartment(department))
        # organization = {
        #     'Org_Name':"USD",
        #     'Address' : "Vermillion,South Dakota",
        #     'PhoneNo' : 6056698768
        # }

        # print(self.insertOrganization(organization))
        # employee = {
        #     'ssn':"877",
        #     'full_name':"bichar",
        #     'Address':"530 ELM STREET",
        #     'email':"bichar4@gmail.com",
        #     'phone' :98099898
        # }

        # print("Welcome")
        # # print(self.applyForLeave(1011,'2021-09-12','2021-09-13'))
        # print(self.generatePayROll(1011,'2021-09-13',15))


if __name__ == '__main__':
    mypayroll = Payroll(loadDummyData=False)
    mypayroll.test()
