print('\nThis program calculates strawberry sales ' 
      'for the month.\n')

more_sales_data = input('Do you have strawberry sales '
						'data to enter? (y/n): ')
					
total_sales_data = 0

while more_sales_data == "y":
	new_sales_data = int(input('\nEnter the quantity of '
							   'sales in pints: '))
	total_sales_data += new_sales_data
	more_sales_data = input('\nDo you have more strawberry '
							'sales data to enter? (y/n): ')
							
print('\nTotal strawberry sales in pints: {}'.format(total_sales_data))
	
