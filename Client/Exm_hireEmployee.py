import sys
sys.path.append("../Payroll")
import json
from Payroll import Payroll

mypayroll = Payroll(loadDummyData=False)

employee = {
    'ssn':"877",
    'full_name':"Mukesh",
    'Address':"530 ELM STREET",
    'email':"Mukesh@gmail.com",
    'phone' :98099898
}

allowances = {
    "dearness":200.00,
    "house_rent":198.80,
    "medical":312.11,
    "hostel": -200.10 ,
    "bus": -78.87,
    "security":-99.98,
    "welfare":-30.34,
    "other":20.24
}

organizationId = 5003
departmentId = 6005
position = 'GA'
basicPay = 1500.00
join_date = "2020/05/21"

print("Employees before hiring new")
employees = mypayroll.getEmployeesInOrg(organizationId)
print(json.dumps(employees,indent=2))

mypayroll.hireEmployee(employee,departmentId,position,basicPay,join_date,allowances)

print("Employees after hiring new")
employees = mypayroll.getEmployeesInOrg(organizationId)
print(json.dumps(employees,indent=2))
