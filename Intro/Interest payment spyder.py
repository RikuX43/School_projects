# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 14:09:43 2021

@author: Riku
"""

price=float(input('Enter the purchase price: '))

month_number=1 

int_rate=0.12

down_payment=price*.10 
monthly_payment=(price-down_payment)*.05

current_balance=price-down_payment

print('{:<15s} {:<20s} {:<20s} {:<20s} {:<20s} {:<20s}'.format('Month','Starting Balance','Interest to Pay',

      'Principal to Pay','Payment','Ending Balance'))

while current_balance>0:

    if current_balance<monthly_payment:

        int_amt=0

        principal=current_balance

        payment=current_balance

        ending_balance=0

    else:

        int_amt=current_balance*(int_rate/12)


        principal=monthly_payment-int_amt


        payment=int_amt+principal


        ending_balance=current_balance-principal


    print('{:<15d} {:<20.2f} {:<20.2f} {:<20.2f} {:<20.2f} {:<20.2f}'.format(month_number, current_balance, int_amt,

                                                                             principal, payment, ending_balance))


    current_balance=ending_balance

    month_number+=1