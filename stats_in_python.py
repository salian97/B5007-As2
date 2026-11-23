import sys
import math

def load_data(filepath:str, column:int)->tuple[list, int]:
    # TODO - Complete the function so it loads the data from the file into a list
    # The function returns a tuple that contains the list of values and the total number 
    # of values in the column
    numbers = []
    total_values = 0
    filename = filepath.rsplit("/", 1)[-1]

    with open(filepath, "r") as infile:
        for line_num, line in enumerate(infile, start=1):
            line = line.rstrip("\n")
            if line == "":
                continue
            try:
                value = line.split("\t")[column]
            except IndexError:
                print(
                    f"Exiting: There is no valid 'list index' in column {column} "
                    f"in line {line_num} in file: {filename}"
                )
                sys.exit()

            total_values += 1
            try:
                num = float(value)
                if math.isnan(num):
                    continue
                numbers.append(num)
            except ValueError:
                continue

    if len(numbers) == 0:
        print(
            f"Error: There were no valid number(s) in column {column} "
            f"in file: {filename}"
        )
        sys.exit()

    return numbers, total_values


def calculate_average(numbers:list)->float:
    # TODO - Complete the function to return the average of the list of numbers
    return sum(numbers) / len(numbers)


def get_max_and_min(numbers:list)->tuple[float, float]:
    # TODO - Complete the function to return a tuple with the maximum and minimum
    # values in the list, in that order
    return max(numbers), min(numbers)


def calculate_variance(numbers:list)->float:
    # TODO - Complete the function to return the variance of the numbers in the list
    n = len(numbers)
    if n < 2:
        return 0.0
    mean = calculate_average(numbers)
    squared_diffs = 0.0
    for num in numbers:
        squared_diffs += (num - mean) ** 2
    return squared_diffs / (n - 1)


def calculate_std_dev(numbers:list)->float:
    # TODO - Complete the function to return the standard deviation of the numbers in the list
    return math.sqrt(calculate_variance(numbers))


def calculate_median(number:list)->float:
    # TODO - Complete the function to return the median of the numbers in the list
    sorted_nums = sorted(number)
    n = len(sorted_nums)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    return float(sorted_nums[mid])
