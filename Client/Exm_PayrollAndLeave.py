import sys
sys.path.append("../Payroll")
import json

from Payroll import Payroll

mypayroll = Payroll(loadDummyData=False)

print("Before any leaves")
leaves_taken = mypayroll.getLeaveDays(1100)
print(leaves_taken)

print("===============================")


# takes some leave
mypayroll.applyForLeave(1100, "2020/06/21","2020/06/22")
mypayroll.applyForLeave(1100, "2020/07/05","2020/07/08")

leaves_taken = mypayroll.getLeaveDays(1100)
print(leaves_taken)
print("===============================")

#generate payrolls
id = mypayroll.generatePayROll(1100,'2021-09-13',15) # generate paytpll for 15 days , paid on 2021-09-13
payroll_history = mypayroll.getEmployeePayRollHistory(1100)

print(payroll_history)