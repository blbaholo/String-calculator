import re


NEGATIVE_INT_PATTERN = r"(-[0-9]+)"
INT_PATTERN = r"[0-9]+"
DELIMITER_PATTERN = r"(//(.*?)\n)"


def verify_user_input(user_input):
    if not isinstance(user_input, str):
        raise TypeError("User input is of incorrect type. Please insert a string")


def invalid_input():
    raise ValueError("ERROR: invalid input")


def checking_string_input(user_input):
    if re.search(NEGATIVE_INT_PATTERN, user_input):
        return handling_negative_integers(user_input)
    if (
        re.search(r"^([0-9])", user_input) == None
        or re.search(r"([0-9])$", user_input) == None
    ):
        invalid_input()
    return user_input


def handling_negative_integers(user_input):
    find_negative_integers = re.findall(NEGATIVE_INT_PATTERN, user_input)
    negative_integers = ",".join(find_negative_integers)
    if find_negative_integers:
        raise ValueError(str(f"ERROR: negatives not allowed {negative_integers}"))
    if negative_integers == "":
        return user_input


def identifying_delimiters(user_input):
    find_delimiter = re.findall(r"^((//)(.*?)(\n))", user_input)
    length_find_delimiter = len(find_delimiter)
    match_delimiter = re.search(DELIMITER_PATTERN, user_input)
    if length_find_delimiter == 0 and match_delimiter != None:
        invalid_input()
    if length_find_delimiter == 0 and match_delimiter == None:
        return checking_string_input(user_input)
    delimiter_format = find_delimiter[0][0]
    delimiter = find_delimiter[0][2]
    remove_delimiter_format = re.sub(re.escape(delimiter_format), "", user_input)
    new_string = re.sub(re.escape(delimiter), ",", remove_delimiter_format)
    if re.search(r"\W$", new_string):
        invalid_input()
    for n in range(len(new_string) - 1):
        if (
            new_string[n] == ","
            and new_string[n + 1] == ","
            or new_string[n] == ","
            and new_string[n + 1] in delimiter
        ):
            invalid_input()
    count_delimiter = remove_delimiter_format.count(delimiter)
    if count_delimiter != (len(re.findall(INT_PATTERN, new_string)) - 1):
        invalid_input()
    if re.search(NEGATIVE_INT_PATTERN, new_string):
        return handling_negative_integers(new_string)
    return new_string


def add(user_input):
    verify_user_input(user_input)
    if user_input == "":
        return 0
    total = 0
    string_list = list(re.findall(INT_PATTERN, identifying_delimiters(user_input)))
    for number in string_list:
        total += int(number)
    return total
