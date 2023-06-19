import matplotlib.pyplot as plt
import math


def create_fractal(iterations: int, initial_word: str, rules: dict) -> str:
    word = initial_word

    for _ in range(iterations):
        next_word = ""
        for char in word:
            if char in rules:
                next_word += rules[char]
            else:
                next_word += char
        word = next_word
    return word


def get_x_and_y_coordinates(fractal_string: str, angle: int) -> tuple:
    list_position_and_a = []
    coordinate = [0, 0]
    a = -45
    coordinates = []

    for char in fractal_string:
        if char == "F":
            new_position = [coordinate[0] + math.cos(a), coordinate[1] + math.sin(a)]
            coordinates.append(new_position)
            coordinate = new_position
        elif char == "-":
            a = a + math.radians(angle)
        elif char == "+":
            a = a - math.radians(angle)
        elif char == "[":
            list_position_and_a.append((coordinate, a))
        elif char == "]":
            coordinate, a = list_position_and_a.pop()

    return [x[0] for x in coordinates], [y[1] for y in coordinates]


def display_plot(x: list, y: list) -> None:
    plt.plot(x, y, color="green")
    plt.gca().invert_yaxis()
    plt.axis("equal")
    plt.show()

#Provide number of iterations
iterations_ = 6


initial_word_ = "X"
rules_ = {
    "X": "F+[[X]-X]-F[-FX]+X",
    "F": "FF"
}
angle_ = 25

fractal_ = create_fractal(iterations_, initial_word_, rules_)

x_, y_ = get_x_and_y_coordinates(fractal_, angle_)

display_plot(x_, y_)
