try:                                            #try block to make sure user input a number
    hours = float(input("Enter hors: "))        #user input hours and convert to float
    rate = float(input("Enter rate: "))         #user input rate per hour
except:                                         #except block printing error message and stop running the code
    print("Error, please enter numeric number")
    quit()
regular_pay = hours * rate                      #multiply hours and rate to create the pay variable
overtime_pay = (hours - 40) * (rate * 0.5)      #calculate overtime to pay 1.5 times above 40 hours

if hours > 40:
    print("Overtime, pay:", regular_pay + overtime_pay) 
else:
    print("Regular, pay: ", regular_pay)
