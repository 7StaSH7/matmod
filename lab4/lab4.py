import matplotlib.pyplot as plt
import math
import numpy as np


def main() -> None:
    spring_stiffness_koef = 0.9

    vent_weigth = 1
    vent_radius = 5

    spring_oscillation_period = 2 * np.pi * np.sqrt(vent_weigth / spring_stiffness_koef)
    vent_oscillation_period = 5 * spring_oscillation_period

    print(
        "Отношение периода вращения вентилятора к периоду колебания пружины:",
        vent_oscillation_period / spring_oscillation_period,
    )

    t = np.linspace(0, vent_oscillation_period, 1000)

    spring_y = -10 * np.cos(np.sqrt(spring_stiffness_koef / vent_weigth) * t)

    rx = vent_radius * np.cos(((2 * np.pi) / (vent_oscillation_period)) * t)
    ry = vent_radius * np.sin(((2 * np.pi) / (vent_oscillation_period)) * t)

    ry += spring_y

    # plt.plot(t, spring_x)
    plt.plot(rx, ry)
    plt.ylabel("Проекция радиус вектора ry")
    plt.xlabel("Проекция радиус вектора rx")
    plt.show()
