#calculate the 10.6% fee for CCSS and store it in a variable
#Calculate the 1.5% fee for Banco Popular and store it in a variable
#Calculate the net salary and store it in a variable
#percentage = percentage / 100

print("Thanks for using the net salary calculator")
name = input('Please tell me your name: ')
salary = int(input('Provide me your salary: '))

ccss_fee = (salary * 10.6) /100 #CCSS 10.6% fee 
bp_fee = (salary * 1.5) /100 #Banco Popular 1.5% fee 
net_salary = salary - (ccss_fee +bp_fee )

"""print(ccss_fee)
print(bp_fee)
print(net_salary)
this was the test to make sure every operation works individually and that the result was correct
"""

print(f"Hello {name}, your net salary is: {net_salary}. Your CCSS' fee is: {ccss_fee} and the Banco Popular's fee is {bp_fee}" )