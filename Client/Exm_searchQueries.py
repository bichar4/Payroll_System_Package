import sys
sys.path.append("../Payroll")

from Payroll import Payroll

mypayroll = Payroll(loadDummyData=False)
employee = mypayroll.searchEmployeeByName("Dunn")

print("Results: ",employee)

organization = mypayroll.searchOrganizationByName("us")
print("Results:", organization)
