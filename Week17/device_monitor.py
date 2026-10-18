"""Simulated Device Monitoring and Alert System (CPP102 Week 17)."""

def get_initial_readings():
    """Return the starting list of simulated temperature readings."""
    return [28, 31, 35, 37, 29]


def display_menu():
    """Print the main menu."""
    print("SIMULATED DEVICE MONITORING SYSTEM")
    print("----------------------------------")
    print("[1] View Readings")
    print("[2] Add Reading")
    print("[3] Classify Readings")
    print("[4] Generate Summary")
    print("[5] Exit")
    print()


def is_whole_number(text):
    """Return True if text is a whole number such as 3 or -2."""
    if len(text) == 0:
        return False
    start = 0
    if text[0] == "-":    # a minus sign is allowed only at the front
        start = 1
    if start == len(text):    # the text is only "-"
        return False
    for index in range(start, len(text)):
        if text[index] not in "0123456789":
            return False
    return True


def add_reading(readings, lowest, highest):
    """Ask for one reading and add it to the list only if it is valid."""
    text = input("Enter new reading: ")
    print()
    if len(text) == 0:
        print("Invalid input. The reading cannot be empty.")
    elif not is_whole_number(text):
        print("Invalid input. Enter a whole number only.")
    elif int(text) < lowest or int(text) > highest:
        print("Invalid reading. Enter a value from 0 to 100.")
    else:
        readings.append(int(text))
        print("Reading added successfully.")


def classify_reading(reading, warning_limit, critical_limit):
    """Return NORMAL, WARNING, or CRITICAL for one reading."""
    if reading < warning_limit:
        return "NORMAL"
    elif reading <= critical_limit:    # boundary: 35 is still WARNING
        return "WARNING"
    else:
        return "CRITICAL"


def compute_total(readings):
    """Return the total of all readings."""
    total = 0    # total is computed with a loop; sum() is not allowed
    for reading in readings:
        total = total + reading
    return total


def compute_average(readings):
    """Return the average of the readings."""
    return compute_total(readings) / len(readings)


def find_minimum(readings):
    """Return the smallest reading."""
    minimum = readings[0]    # start with the first reading, not 0
    for reading in readings:
        if reading < minimum:
            minimum = reading
    return minimum


def find_maximum(readings):
    """Return the largest reading."""
    maximum = readings[0]
    for reading in readings:
        if reading > maximum:
            maximum = reading
    return maximum


def count_category(readings, warning_limit, critical_limit, category):
    """Return how many readings fall in the given category."""
    count = 0
    for reading in readings:
        if classify_reading(reading, warning_limit, critical_limit) == category:
            count = count + 1
    return count


def compute_percentage(part, whole):
    """Return part as a percentage of whole."""
    return part / whole * 100


def determine_overall_status(warning_count, critical_count):
    """Return the overall status; CRITICAL is checked first."""
    if critical_count >= 1:
        return "ATTENTION REQUIRED"
    elif warning_count >= 1:
        return "MONITOR"
    else:
        return "NORMAL"


def view_readings(readings):
    """Print every reading with its position number."""
    print("CURRENT READINGS")
    print("----------------")
    position = 1
    for reading in readings:
        print(f"Reading {position}: {reading} °C")
        position = position + 1


def classify_readings(readings, warning_limit, critical_limit):
    """Print the classification of every reading."""
    print("READING CLASSIFICATION")
    print("----------------------")
    for reading in readings:
        print(f"{reading} °C -> "
    f"{classify_reading(reading, warning_limit, critical_limit)}")


def generate_summary(readings, warning_limit, critical_limit):
    """Print the numerical summary and the overall status."""
    count = len(readings)
    normal = count_category(readings, warning_limit, critical_limit, "NORMAL")
    warning = count_category(readings, warning_limit, critical_limit, "WARNING")
    critical = count_category(readings, warning_limit, critical_limit, "CRITICAL")

    print("MONITORING SUMMARY")
    print("------------------")
    print(f"Number of readings : {count}")
    print(f"Total of readings  : {compute_total(readings)}")
    print(f"Average temperature : {compute_average(readings):.2f} °C")
    print(f"Minimum temperature : {find_minimum(readings)} °C")
    print(f"Maximum temperature : {find_maximum(readings)} °C")
    print()
    print(f"NORMAL   : {normal} ({compute_percentage(normal, count):.2f}%)")
    print(f"WARNING  : {warning} ({compute_percentage(warning, count):.2f}%)")
    print(f"CRITICAL : {critical} ({compute_percentage(critical, count):.2f}%)")
    print()
    print(f"Overall Status: {determine_overall_status(warning, critical)}")


def main():
    """Control the menu loop of the program."""
    readings = get_initial_readings()
    warning_limit = 30     # 30 and above is at least WARNING
    critical_limit = 35    # boundary: 35 is still WARNING, not CRITICAL
    running = True
    while running:
        display_menu()
        choice = input("Enter choice: ")    # input() gives text, so compare with "1"
        print()
        if choice == "1":
            view_readings(readings)
        elif choice == "2":
            add_reading(readings, 0, 100)
        elif choice == "3":
            classify_readings(readings, warning_limit, critical_limit)
        elif choice == "4":
            generate_summary(readings, warning_limit, critical_limit)
        elif choice == "5":
            print("Thank you for using the Device Monitoring System.")
            running = False
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")
        if running:
            print()


main()