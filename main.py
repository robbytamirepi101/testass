#You can enter the investment rate as a whole number like 5
interestRate = int(input("Please enter your yearly rate: " ))
print()

#You can enter the investment amount as a full amount like 50,000
investment_amount = float(input("Please enter your investment amount: "))

newinvestmentAmount = investment_amount = float(input("Please enter your investment amount: "))

year = 0

print()    
while newinvestmentAmount <= (investmentAmount * 2):
    newinvestmentAmount = newinvestmentAmount + (newinvestmentAmount * (interestRate / 100))
    year +=1
    print("The investment for the year : " + str (year)+ " is "  + str(round(newinvestmentAmount, 2)))


print("we checking for changes on code")
print()
print("It will take ", str (year) + " years to double your investment" )
#added a comment that we changed the code and testing 