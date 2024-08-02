from datetime import datetime

def calculate_age(birth_date):
    today = datetime.today()
    age = today.year - birth_date.year
    
    # Adjust for months and days
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1

    return age

def main():
    # Get user input
    try:
        day = int(input("Enter your birth day (DD): "))
        month = int(input("Enter your birth month (MM): "))
        year = int(input("Enter your birth year (YYYY): "))
        
        birth_date = datetime(year, month, day)
        
        age = calculate_age(birth_date)
        print(f"You are {age} years old.")
    
    except ValueError:
        print("Invalid date format. Please enter numeric values for day, month, and year.")

if __name__ == "__main__":
    main()
