from unittest.mock import patch
from grade_calculator import calculate_average_grade

def test_calculate_average_grade():
    with patch('builtins.input', side_effect=['John Doe', '85', '90', '92']):
        assert calculate_average_grade() == ('John Doe', 89)