import pytest
from ski_calculator.calculator import Skier, calculate_ski_length


@pytest.mark.parametrize('length, age, style, expected', [
#        Length, Age, Style,            Expected Value
        (80,     4,   Skier.classic,    80),
        (80,     5,   Skier.classic,    90),
        (80,     10,  Skier.classic,    100),
        (80,     10,  Skier.free_style, 90),
])

def test_calculate_ski_length(length, age, style, expected):
    skier = Skier(length, age, style)
    ski_length = calculate_ski_length(skier)
    assert expected == ski_length
