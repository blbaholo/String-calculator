import pytest
from string_calculator.calculator import add


def test_incorrect_input_type():
    with pytest.raises(
        TypeError, match=r"User input is of incorrect type. Please insert a string"
    ):
        add([1, 2, 3, 11])
        add(12)


@pytest.mark.parametrize("user_input, expected_value", [("", 0), ("1", 1), ("1,1", 2)])
def test_up_to_two_integers(user_input, expected_value):
    assert add(user_input) == expected_value


@pytest.mark.parametrize(
    "user_input, expected_value", [("1,2,3,4", 10), ("1,2,3,5,6", 17)]
)
def test_multiple_integers(user_input, expected_value):
    assert add(user_input) == expected_value


@pytest.mark.parametrize(
    "user_input, expected_value", [("1\n2,3", 6), ("1\n2,3\n5,6", 17)]
)
def test_newlines_between_integers(user_input, expected_value):
    assert add(user_input) == expected_value


def test_negative_integers():
    with pytest.raises(ValueError, match=r"ERROR: negatives not allowed -1,-2"):
        add("-1,-2,3,4")


@pytest.mark.parametrize(
    "user_input, expected_value", [("//88\n18820882", 23), ("//***\n1***2***3", 6)]
)
def test_delimiter_handling(user_input, expected_value):
    assert add(user_input) == expected_value


def test_invalid_input():
    with pytest.raises(ValueError, match=r"ERROR: invalid input"):
        add("//88\n18882")
        add("//4\n14244")
        add("1,2,3//,\n1,2,3")
        add("//,\n1:2:3:4")