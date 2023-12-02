import sys

word_to_digit = {'zero': '0o', 'one': 'o1e', 'two': 't2o', 'three': 't3e', 'four': '4', 'five': '5e', 'six': '6', 'seven': '7n', 'eight': 'e8t', 'nine': 'n9e'}

def get_digits_from_string(string):
    return [char for char in string if char.isnumeric()]

def replace_string_with_number(string):
    # avoid destroying overlapping numbers by simply solving any overlap in our word_to_digit dict.
    new_string = string
    for key, value in word_to_digit.items():
        while key in new_string:
            new_string = new_string.replace(key, value)
    return new_string
    
if __name__ == "__main__":
    print("Input Values, end with empty line: ")
    input_line = "0"
    input_array = []
    for line in sys.stdin:
        if line.rstrip() == '':
            break
        input_array.append(line.rstrip())

    input_array = [replace_string_with_number(string) for string in input_array]
    digits = [get_digits_from_string(string) for string in input_array]
    first_and_last_digits = [string[0] + string[len(string)-1] for string in digits]
    numeric_digits = [int(number) for number in first_and_last_digits]
    print(sum(numeric_digits))

        
