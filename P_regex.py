import os; os.system('cls')

import re

text = open('payroll.csv', 'r')
text = ' '.join([i for i in text])
# print(text)
text = text.replace(',', " ")

#Employee ID
Employee_ID = re.findall(r'\s\d\d-\d\d\d\d', text)
if Employee_ID :
    print(Employee_ID)
else:
    print('did no not find Employee ID')

# SSN   
SSN = re.findall(r'\s\d{3}-\d{2}-\d{4}', text)
if SSN :
    print(SSN)
else:
    print('did not find SSN') 

# Emails
Emails= re.findall(r'([a-zA-Z0-9.-]+@[a-zA-Z-]+\.[a-z|A-Z]{2,})', text)
if Emails :
    print(Emails)
else:
    print('did not find Emails') 
    
# Phone Number
Phone_Number = re.findall(r'\s\w{3}-\w{3}-\w{4}', text)
if Phone_Number :
    print(Phone_Number)
else:
    print('did not find Phone_number')
