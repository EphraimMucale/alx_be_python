from datetime import datetime, timedelta, date

def display_current_datetime():
    date = datetime.now()
    current_date = date.strftime("%Y-%m-%d %H:%M:%S")

    print(f"Current date and time: {current_date}")

display_current_datetime()

def ask():
    days_to_add = ("Enter the number of days to add to the current date: ")
    return days_to_add

def interger(number_given):
    if number_given.isdigit():
        plus = int(number_given)
        return plus
    
    else:
        print("Invalid input")

def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add: ")) 
    delta = timedelta(days=number_of_days)
    day = date.today()
    future_date = day + delta

    print(f"Future date: {future_date}")

display_current_datetime()
calculate_future_date()
