from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays the current date and time in the format YYYY-MM-DD HH:MM:SS
    """
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")


def calculate_future_date(days_to_add):
    """
    Calculates the future date after adding a given number of days
    Parameters:
        days_to_add (int): Number of days to add to the current date
    """
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days_to_add)
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")


def main():
    # Part 1: Display current date and time
    display_current_datetime()

    # Part 2: Calculate future date
    while True:
        try:
            days_input = int(input("Enter the number of days to add to the current date: "))
            if days_input < 0:
                print("Please enter a non-negative number.")
                continue
            calculate_future_date(days_input)
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")


if __name__ == "__main__":
    main()