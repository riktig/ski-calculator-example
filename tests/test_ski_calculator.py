import pytest
from ski_calculator.calculator import Skier, calculate_ski_length


@pytest.mark.parametrize('length, age, style, expected', [
        (80,  4,  Skier.classic,   (80,  80)),
        (80,  5,  Skier.classic,   (90,  100)),
        (140, 9,  Skier.classic,   (160, 160)),
        (187, 30, Skier.classic,   (207, 207)),
        (180, 30, Skier.freestyle, (190, 195)),
])

def test_calculate_ski_length(length, age, style, expected):
    skier = Skier(length, age, style)
    ski_length = calculate_ski_length(skier)
    assert expected == ski_length


@pytest.mark.parametrize('length, age, style', [
        (188,     30,   Skier.classic), # Skier too long
        (180,     30,   "Invalid Ski Type"),
])

def test_calculate_ski_length_value_error(length, age, style):
    skier = Skier(length, age, style)
    with pytest.raises(ValueError):
        ski_length = calculate_ski_length(skier)
