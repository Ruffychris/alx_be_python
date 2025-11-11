#prompt user for their financial details
monthly_income = float(input("Enter your monthly income:")) #ask for monthly income
monthly_expenses = float(input("Enter your total monthly expenses:")) #ask for total monthly expenses

#calculate user's mothly savings
monthly_savings = monthly_income- monthly_expenses

#project user's annual savings with 5% interest
projected_savings = (monthly_savings * 12) + (monthly_savings * 12 * 0.05)

#dislay the results
print("Your monthly savings are $",monthly_savings)
print("Projected savings after one year, with interest, is: $",projected_savings)