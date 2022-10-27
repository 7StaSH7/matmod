import matplotlib.pyplot as plt
import math
import numpy as np

spring_stiffness_koef = 0.9

vent_weigth = 1
vent_radius = 5


def calc(koef: int, spring_oscillation_period: float) -> None:
    vent_oscillation_period = koef * spring_oscillation_period

    t = np.linspace(0, vent_oscillation_period, 1000)

    spring_y = -10 * np.cos(np.sqrt(spring_stiffness_koef / vent_weigth) * t)

    rx = vent_radius * np.cos(((2 * np.pi) / (vent_oscillation_period)) * t)
    ry = vent_radius * np.sin(((2 * np.pi) / (vent_oscillation_period)) * t)

    ry += spring_y
    plt.figure()
    plt.title(f"Соотношение = {vent_oscillation_period / spring_oscillation_period}")
    plt.plot(rx, ry)
    plt.ylabel("Проекция радиус вектора ry")
    plt.xlabel("Проекция радиус вектора rx")


def main() -> None:
    spring_oscillation_period = 2 * np.pi * np.sqrt(vent_weigth / spring_stiffness_koef)

    for koef in range(1, 11):
        calc(koef, spring_oscillation_period)
    plt.show()
