class Skier:
    def __init__(self, length, age, style):
        self.length = length
        self.age = age
        self.style = style

    classic = 'classic'
    freestyle = 'freestyle'

_MAX_SUPPORTED_CLASSIC_SKI_LENGTH = 207

def calculate_ski_length(skier):
    if skier.age <= 4:
        return _calculate_baby_ski_length(skier)
    if skier.age <= 8:
        return _calculate_child_ski_length(skier)
    if skier.style == Skier.classic:
        return _calculate_classic_ski_length(skier)
    if skier.style == Skier.freestyle:
        return _calculate_freestyle_ski_length(skier)
    raise ValueError(f"Ski style {skier.style} is unsupported")

def _calculate_baby_ski_length(skier):
    return (skier.length, skier.length)

def _calculate_child_ski_length(skier):
    return (skier.length + 10, skier.length + 20)

def _calculate_classic_ski_length(skier):
    ski_length_min, ski_length_max = (skier.length + 20, skier.length + 20)
    if ski_length_max > _MAX_SUPPORTED_CLASSIC_SKI_LENGTH:
        raise ValueError(f"Calculated classic ski length is {ski_length_max}, "
                          "max supported length is {_MAX_SUPPORTED_CLASSIC_SKI_LENGTH}")
    return ski_length_min, ski_length_max

def _calculate_freestyle_ski_length(skier):
    return (skier.length + 10, skier.length + 15)
