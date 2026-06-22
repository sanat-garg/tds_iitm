import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Test with an empty list, expecting 0."""
    assert longest_positive_streak([]) == 0

def test_all_positive():
    """Test with a list of all positive numbers."""
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_with_negatives_breaking_streak():
    """Test where a negative number breaks a streak."""
    assert longest_positive_streak([1, 2, -1, 3, 4]) == 2

def test_with_zeros_breaking_streak():
    """Test where a zero breaks a streak."""
    assert longest_positive_streak([1, 2, 0, 3, 4, 5]) == 3

def test_multiple_streaks_longest_wins():
    """Test with multiple streaks to ensure the longest is returned."""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_streak_at_the_end():
    """Test a scenario where the longest streak is at the end of the list."""
    assert longest_positive_streak([-1, 0, 1, 2, 3]) == 3

def test_no_positive_numbers():
    """Test a list with no positive numbers."""
    assert longest_positive_streak([-1, -2, -3, 0]) == 0

def test_single_positive_number():
    """Test a list with a single positive number."""
    assert longest_positive_streak([5]) == 1

def test_single_non_positive_number():
    """Test a list with a single non-positive number."""
    assert longest_positive_streak([-5]) == 0

def test_long_list_with_streaks():
    """Test with a longer list and multiple streaks."""
    assert longest_positive_streak([1] * 100 + [-1] + [1] * 50) == 100

def test_example_from_prompt():
    """Test the specific example from the prompt."""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_another_example_from_prompt():
    """Test another example from the prompt."""
    assert longest_positive_streak([1, 1, 1]) == 3