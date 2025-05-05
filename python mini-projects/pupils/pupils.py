import csv


# Each row in the pupils.csv file contains three elements.
# These are the indexes of the elements in each row.
GIVEN_NAME_INDEX = 0
SURNAME_INDEX = 1
BIRTHDATE_INDEX = 2

def main():
    filename = "pupils.csv"
    students_list = read_compound_list(filename)
    print_list(students_list)
    get_birthdate(students_list)
    get_given_name(students_list)


def read_compound_list(filename):
    """Read the text from a CSV file into a compound list.
    The compound list will contain small lists. Each small
    list will contain the data from one row of the CSV file.

    Parameter
        filename: the name of `the CSV file to read.
    Return: the compound list
    """
    # Create an empty list.
    compound_list = []

    # Open the CSV file for reading.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(csv_file)

        # The first line of the CSV file contains column headings
        # and not a student's I-Number and name, so this statement
        # skips the first line of the CSV file.
        next(reader)

        # Process each row in the CSV file.
        for row in reader:

            # Append the current row at the end of the compound list.
            compound_list.append(row)

    return compound_list


def print_list(students_list):
    print(*students_list, sep = "\n")

def get_birthdate(students_list):
    birth_func = lambda birthday: birthday[BIRTHDATE_INDEX]

    sorted_list = sorted(students_list, key=birth_func )

    print()
    print('Ordered from Oldest to Youngest')
    print_list(sorted_list)

def get_given_name(students_list):
    name_func = lambda name: name[GIVEN_NAME_INDEX]

    sorted_list = sorted(students_list, key=name_func )

    print()
    print('Ordered by Given Name')
    print_list(sorted_list)


# Each row in the pupils.csv file contains three elements.
# These are the indexes of the elements in each row.
GIVEN_NAME_INDEX = 0
SURNAME_INDEX = 1
BIRTHDATE_INDEX = 2

def main():
    filename = "pupils.csv"
    students_list = read_compound_list(filename)
    print_list(students_list)
    get_birthdate(students_list)
    get_given_name(students_list)


def read_compound_list(filename):
    """Read the text from a CSV file into a compound list.
    The compound list will contain small lists. Each small
    list will contain the data from one row of the CSV file.

    Parameter
        filename: the name of the CSV file to read.
    Return: the compound list
    """
    # Create an empty list.
    compound_list = []

    # Open the CSV file for reading.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(csv_file)

        # The first line of the CSV file contains column headings
        # and not a student's I-Number and name, so this statement
        # skips the first line of the CSV file.
        next(reader)

        # Process each row in the CSV file.
        for row in reader:

            # Append the current row at the end of the compound list.
            compound_list.append(row)

    return compound_list


def print_list(students_list):
    print(*students_list, sep = "\n")

def get_birthdate(students_list):
    birth_func = lambda birthday: birthday[BIRTHDATE_INDEX]

    sorted_list = sorted(students_list, key=birth_func )

    print()
    print('Ordered from Oldest to Youngest')
    print_list(sorted_list)

def get_month_day(students_list):
    name_func = lambda month: month[GIVEN_NAME_INDEX]

    sorted_list = sorted(students_list, key=name_func )

    print()
    print('Ordered by Given Name')
    print_list(sorted_list)

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()