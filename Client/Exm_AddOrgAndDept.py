import sys
sys.path.append("../Payroll")
import json
from Payroll import Payroll

mypayroll = Payroll(loadDummyData=True)


organization = {
    'Org_Name':"USD",
    'Address' : "Vermillion,South Dakota",
    'PhoneNo' : 6056698768
}

print("Previos organizations record")
organizations = mypayroll.getOrganizations() #out package module api call
print(json.dumps(organizations,indent = 2))
print("===================================")

#ADding the organizations
org_id = mypayroll.insertOrganization(organization)[0]['LAST_INSERT_ID()'] #extract id of recently added value 
print(org_id)

print("organizations record after Adding")
organizations = mypayroll.getOrganizations()
print(json.dumps(organizations,indent = 2))
print("===================================")

department = {
    "Dept_Name": "Research",
    "org_id": org_id
}

print("Current Department in recently added organization")
departments = mypayroll.getDepartments(org_id) #getting the department 
print(json.dumps(departments,indent = 2))
print("===================================")

mypayroll.insertDepartment(department) #Adding the department

print("Departments after adding ")
departments = mypayroll.getDepartments(org_id)
print(json.dumps(departments,indent = 2))
print("===================================")


