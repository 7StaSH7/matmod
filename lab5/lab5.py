import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

pray_birth = 1.
pray_death_due_to_predators = 0.1
predator_death = 1.5
predator_groth = 0.75


def calc_populate(population: np.array, t: np.linspace = 0) -> np.array:
       return np.array([ pray_birth*population[0] - pray_death_due_to_predators*population[0]*population[1],
                        -predator_death*population[1] + pray_death_due_to_predators*predator_groth*population[0]*population[1] ])
    
def main() -> None:
    N0 = predator_death / predator_groth
    M0 = pray_birth / pray_death_due_to_predators
    print("N0", N0)
    print("M0", M0)
    # print("T", 8*np.pi/(M0 / N0))  !!! НАЙТИ !!!
    initianal = np.array([M0, N0])
    t = np.linspace(0, 17, 1000)
    # ode - ordinary differential equation или обыкновенное дифференциальное уравнение
    population, infodict = odeint(calc_populate, initianal, t, full_output=True) 
    
    print(infodict['message'])
    
    prays, predators = population.T
    
    plt.figure()
    plt.plot(t, predators, '-r', label='Хищники')
    plt.plot(t, prays, '-b', label='Жертвы')
    plt.legend(loc='upper right')
    plt.xlabel('Время')
    plt.ylabel('Популяция')
    plt.title('Эволюция популяций хищников и жертв')
    plt.show()
