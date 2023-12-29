def convert(time_str):
    # Split the time string into hours and minutes
    hours, minutes = map(int, time_str.split(':'))

    # Convert the time to a float representation
    return hours + minutes / 60


def main():
    # Prompt the user for a time
    user_time = input("What time is it? ")

    # Convert the input time to float
    time_in_hours = convert(user_time)

    # Check and print the corresponding meal time
    if 7 <= time_in_hours <= 8:
        print("breakfast time.")
    elif 12 <= time_in_hours <= 13:
        print("unch time.")
    elif 18 <= time_in_hours <= 19:
        print("dinner time.")


main()
