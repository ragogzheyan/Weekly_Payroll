import os; os.system('cls')
from decimal import Decimal
import numbers
import math
import statistics as st
import sys 


#Nested dictionary 
weekly_payroll = { 
    "1.":{"employee": "Linus Breeze" , "Rate": "27.50", "Hours":"40.25", "Dependents":"4"},
    "2.":{"employee": "Juan Santiago" , "Rate":"18.75", "Hours":"56.00", "Dependents":"1"},
    "3.":{"employee": "James Webb" , "Rate":"28.35", "Hours":"38.00", "Dependents":"3"},
    "4.":{"employee": "Kylie Sabol" , "Rate":"21.50", "Hours":"46.50", "Dependents":"6"},
    "5.":{"employee": "Amber Ali" , "Rate":"19.35", "Hours":"17.00", "Dependents":"2"},
    "6.":{"employee": "Kevin Goldstein" , "Rate":"17.05", "Hours":"28.00", "Dependents":"5"}
    }


# Add New Employee (new)
weekly_payroll["7."] = {"employee": "Lee Chang" , "Rate":"17.05", "Hours":"28.00", "Dependents":"5"}
weekly_payroll["8."] = {"employee": "Albert Fritz" , "Rate":"28.35", "Hours":"38.75", "Dependents":"3"}

# Remove Employee (new)
weekly_payroll.pop("6.")


# Using get: get a value that might not be there
definition = weekly_payroll.get("6.")
if definition:
    print(definition)
else:
    print("Key doesn't exist")
       

# KEYWORD, FUNCTION NAME, 0 TO MANY PARAMETER(S)
def extract_info(wp): # wp = weekly payroll nested dictionary
    """ Extract info from nested dictionary

    Arg: 
        Weekly payroll as nested dictionary

    Returns:
        This function retuns list of Employee, Rate, Hours, Dependents
    """

# Empty list for key
    employee = []
    Rate = []
    Hours = []
    Dependents = []

#For loop nested dictionary
    for i in wp:
        employee.append(wp[i]["employee"])

    for i in wp:
        Rate.append(float(wp[i]["Rate"]))

    for i in wp:
        Hours.append(float(wp[i]["Hours"]))

    for i in wp:
        Dependents.append(float(wp[i]["Dependents"]))
    return employee, Rate, Hours, Dependents

    

#Total (Gross Pay)
def total_gross_pay (rate, hours):
    tgp=0 #initial Total Gross pay
    for i in range (len(rate)):
        tgp = tgp + (rate[i] * hours[i])
    tgp = round(tgp,2)
    return tgp


# (Individual Gross Pay without overtime)
# def ind_gross_pay (rate, hours):
#     igp=[]
#     for i in range (len(rate)):
#         igp.append(round(rate[i] * hours[i],2))
#     return igp


# (Individual Gross Pay with overtime) (new)
def ind_gross_pay (rate, hours):
    igp=[]
    for i in range (len(rate)):
        if hours[i] <= 40:
            igp.append(round(rate[i] * hours[i],2))
        else:
            igp.append(round((rate[i] * hours[i]) + (.5 * rate[i] * (hours[i] - 40)),2))
   
    return igp


# Calculate State Tax = .06  NEED TO CHANGE
def state_tax (igp):
    s_tax = []
    for items in igp:
        s_tax.append(round(items * .032,2))
    return s_tax

    
#Federal Tax: flat_rate = [.22] 
# Withholding_allowance_per_dependent = [38.46] NEED TO CHANGE
def federal_tax (igp, dep):
    federal_tax=[]
    for i in range (len(igp)):
        federal_tax.append(round(.20*(igp[i]-(dep[i]*38.46)),2)) 
    return federal_tax



# Net Pay before SS and Medicare   
def net_pay (igp,federal_tax, state_tax):
    net_pay = []
    for i  in range (len(igp)):
        net_pay.append(round(igp[i]-(federal_tax[i] + state_tax[i]),2))
    return net_pay

   

# Final Net Pay add Social Security and Medicare deductions (NEW)
def final_net_pay (igp,federal_tax, state_tax, social_security, medicare):
    net_pay = []
    for i  in range (len(igp)):
        net_pay.append(round(igp[i]-(social_security[i] + medicare[i] + federal_tax[i] + state_tax[i]),2))
    return net_pay

   
# YTD (new)
YTD_Social_Security =[4974.00, 5540.20, 4254.00, 5553.90, 3447.60]


# Add New Employee YTD
YTD_Social_Security.append(4825.50)
YTD_Social_Security.append(5553.90)

# Tax rate .062 for social security (new)
Social_Security_Tax = .062
# Tax rate .0145 for medicare (new)
Medicare_tax = .0145

# Social Security deduction (new)
def social_security (igp):
    global Social_Security_Tax
    social_security =[]
    for i in range (len(igp)):
        social_security.append(round(igp[i] * Social_Security_Tax ,2))
    return social_security


# Maximum Soc. Sec. (new) 
Social_Security_Limit = 5553.90

#Social Security deduction  (with maximum amount applied) (new)
def social_security_limited (ind_gross_pay, YTD_Social_Security):
    global Social_Security_Tax 
    global Social_Security_Limit
    social_security =[]
    for i in range (len(ind_gross_pay)):
        if (YTD_Social_Security[i] + (Social_Security_Tax * ind_gross_pay[i])) >= Social_Security_Limit:
           social_security.append(round(Social_Security_Limit - YTD_Social_Security[i],2))
        else:
            social_security.append(round(Social_Security_Tax * ind_gross_pay[i],2))
    
         
    return social_security

#print( "****")

# Medicare deduction (new)
def medicare(igp):
    global Medicare_tax
    medicare = []
    for i in range (len(igp)):
        medicare.append(round(igp[i] * Medicare_tax ,2))
    return medicare


  
employee, Rate, Hours, Dependents = extract_info(weekly_payroll)
Total_Gross_Pay = total_gross_pay(Rate, Hours)
Ind_Gross_Pay = ind_gross_pay(Rate, Hours)  
State_Tax = state_tax(Ind_Gross_Pay)
Federal_Tax = federal_tax(Ind_Gross_Pay, Dependents)
Net_Pay = net_pay(Ind_Gross_Pay, State_Tax, Federal_Tax)
Social_Security = social_security(Ind_Gross_Pay) 
Medicare = medicare( Ind_Gross_Pay)
Social_Security_Limited = social_security_limited(Ind_Gross_Pay, YTD_Social_Security)
Final_Net_Pay = final_net_pay(Ind_Gross_Pay,Federal_Tax, State_Tax, Social_Security_Limited, Medicare)
#print(Final_Net_Pay)


# Total Hours $264.50
Total_Hours = sum(Hours)
print(sum(Hours))

# Total YTD Soc. Sec.
Total_YTD_Social_Security = sum(YTD_Social_Security)

# Total Social Security
Total_Social_Security = sum(Social_Security)

# Total Medicare
Total_Medicare = sum(Medicare)

# Total Federal tax
Total_Federal_Tax = sum(Federal_Tax)

# Total State Tax 
Total_State_Tax = sum(State_Tax)

# Total Net Pay
Total_Net_Pay = sum(Final_Net_Pay)


print("***")
#Mean Rate
Mean_rate = round(st.mean(Rate),2)
print(Mean_rate)
#Mean Hours
Mean_hours = round(st.mean(Hours),2)
print(Mean_hours)
#Mean YTD
Mean_YTD_Social_Security = round(st.mean(YTD_Social_Security),2)
print(Mean_YTD_Social_Security)



#Median Rate
Median_rate = round(st.median(Rate),2)
print(Median_rate)
#Median Hours
Median_hours = round(st.median(Hours),2)
print(Median_hours)
#Median YTD
Median_YTD_Social_Security = round(st.median(YTD_Social_Security),2)
print(Median_YTD_Social_Security)


#Mode Rate
Mode_rate = round(st.mode(Rate),2)
print(Mode_rate)
#Mode Hours
Mode_hours = round(st.mode(Hours),2)
print(Mode_hours)
#Mode YTD
Mode_YTD_Social_Security = round(st.mode(YTD_Social_Security),2)
print(Mode_YTD_Social_Security)
