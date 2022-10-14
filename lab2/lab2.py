import numpy as np
import matplotlib.pyplot as plt

def main() -> None:
    first_space_speed = 7.9 # км/с
    fuel_combustion_rate = 3 # км/с
    payload_weight = .1
    stage_stracture_lam = .1
    stages_fuel_weight = [5, 4] # [1 ступень, 2 ступень, 3 ступень, ...]
    max_rocket_speed = 0
    skip = 0

    for index, fuel_weight in enumerate(stages_fuel_weight):
        fuel_weight_linspace = np.linspace(0, (1 - stage_stracture_lam) * fuel_weight, 100)
        rocket_speed = max_rocket_speed + fuel_combustion_rate * np.log((payload_weight + sum(stages_fuel_weight[index:])) / \
                        (payload_weight + sum(stages_fuel_weight[index:]) - fuel_weight_linspace))
        
        max_rocket_speed = rocket_speed[-1]
        
        if index >= 1:
            skip += (1 - stage_stracture_lam) * stages_fuel_weight[index - 1] 
        
        plt.plot(fuel_weight_linspace + skip, rocket_speed)
        

    print("Максимальная скорость ракеты: ", max_rocket_speed)
    
    if max_rocket_speed > first_space_speed:
        print("Ракету можно вывести на орбиту")
    else:
        print("Ракету нельзя вывести на орбиту")

    plt.xlabel("Масса использованного топлива, т")
    plt.ylabel("Скорость, км/с")
    plt.show()

    