class Skier:
    def __init__(self, length, age, style):
        self.length = length
        self.age = age
        self.style = style

    classic = 'classic'
    free_style = 'free_style'

def calculate_ski_length(skier):
    if skier.age <= 4:
        return skier.length
    if skier.age <= 8:
        return skier.length + 10
    if skier.style == Skier.classic:
        return skier.length + 20
    if skier.style == Skier.free_style:
        return skier.length + 10
