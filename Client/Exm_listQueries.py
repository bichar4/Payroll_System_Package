import sys
sys.path.append("../Payroll")
import json
from Payroll import Payroll

mypayroll = Payroll(loadDummyData=False)

organization = mypayroll.getOrganizations()
print(json.dumps(organization,indent=2))
firstOne = organization[0]['org_id']

employee = mypayroll.getEmployeesInOrg(firstOne)
print(json.dumps(employee,indent=2))

