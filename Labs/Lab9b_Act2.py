# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names:          Cedar Maxwell
# Section:        537
# Assignment:     Lab 9b Activity 2
# Date:           1 November 2019

LoanAmount = float(input("Please enter the amount of the loan: "))
AnnualInterestRate = float(input("Please enter the annual interest rate: "))
MonthlyAmount = float(input("Please enter the amount being paid monthly: "))
FileName = input("Please name the file to which data will be saved: ") + '.csv'

MonthlyInterestRate = AnnualInterestRate / 12 #To simplify later process
InterestAccrued = 0

with open(FileName, 'w') as table:
	RemainingAmount = LoanAmount #So that original loan amount can be referenced later, if needed
	MonthCount = 0
	InitialConcatenatedString = str(MonthCount) + ',' + str(InterestAccrued) + ',' + str(RemainingAmount) + '\n'
	Title = "Month number, Interest accrued, Amount remaining on loan\n"
	table.write(Title)
	table.write(InitialConcatenatedString)
	while (MonthCount <= 29) and (RemainingAmount >= 0):
		RemainingAmount -= MonthlyAmount
		RemainingAmount += (RemainingAmount * (MonthlyInterestRate / 100)) #Convert from percentage to decimal
		InterestAccrued += (RemainingAmount * (MonthlyInterestRate / 100))
		MonthCount += 1 
		#The next line exists because write() accepts only one argument
		ConcatenatedString = str(MonthCount) + ',' + str(InterestAccrued) + ',' + str(RemainingAmount) + '\n'
		table.write(ConcatenatedString)