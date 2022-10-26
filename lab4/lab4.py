import matplotlib.pyplot as plt
import math
import numpy as np


def main() -> None:
    spring_stiffness_koef = 40  # Н/м

    vent_weigth = 1  # кг
    vent_radius = 0.01  # м

    vent_oscillation_period = 2
    spring_oscillation_period = 2 * np.pi * np.sqrt(vent_weigth / spring_stiffness_koef)

    vent_freq =  np.pi / vent_oscillation_period

    t = np.linspace(0, 10 * spring_oscillation_period, 1000)

    x = np.cos(vent_oscillation_period * t) + vent_radius * np.sin(vent_freq * t)

    plt.plot(t, x)
    plt.plot(t, -x)
    plt.show()
