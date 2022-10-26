import math
import random

dots_quantity = 1_000_000
PI = math.pi


def main() -> None:
    def quater_circle() -> float:
        result_pi = 0.0
        for dot in range(dots_quantity):
            x = random.random()  # [0.0, 1.0)
            y = random.random()  # [0.0, 1.0)
            if math.sqrt(x**2 + y**2) <= 1.0:
                result_pi += 1.0
        result_pi = 4 * (result_pi / dots_quantity)

        return result_pi

    def full_circle() -> float:
        result_pi = 0.0
        for dot in range(dots_quantity):
            x = random.uniform(-1.0, 1.0)
            y = random.uniform(-1.0, 1.0)
            if math.sqrt(x**2 + y**2) <= 1.0:
                result_pi += 1.0
        result_pi = 4 * (result_pi / dots_quantity)

        return result_pi

    tests_quantity = 5

    quater_cicle_average_PI, full_cicle_average_PI = 0.0, 0.0

    for i in range(tests_quantity):
        quater_cicle_average_PI += quater_circle()
        full_cicle_average_PI += full_circle()

    quater_cicle_average_PI /= tests_quantity
    full_cicle_average_PI /= tests_quantity

    print(
        f"Точность числа PI для четверти круга на {tests_quantity} при {dots_quantity} бросаниях:",
        PI / quater_cicle_average_PI,
    )
    print(
        f"Точность числа PI для целого круга на {tests_quantity} при {dots_quantity} бросаниях:",
        PI / full_cicle_average_PI,
    )
