revenue = int(input("Enter the revenue: "))
cost = int(input("Enter the cost: "))
profit = revenue - cost
print('The business profit is: ' + str(profit))

cost_bar = '#' * int((cost / revenue) * 25)
profit_bar = '#' * int((profit / revenue) * 25)
print('  cost: ' + cost_bar)
print('profit: ' + profit_bar)