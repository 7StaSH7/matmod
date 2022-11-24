import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint



def main() -> None:
    first_level_of_distrust = 10
    second_level_of_distrust = 10
    
    t = np.linspace(0, 20, 1000)
    
    first_country_weapon_abrasion = 0.5
    second_country_weapon_abrasion = .8
    
    fig, axs = plt.subplots(3, 3, figsize=(10, 6), constrained_layout=True)
    for i, k1 in enumerate([0.5, 1, 1.5]):
        for j, k2 in enumerate([0.5, 1, 1.5]):            
            
            first_country_weapon = k1 * second_country_weapon_abrasion
            second_country_weapon = k2 * first_country_weapon_abrasion    
            
            
            initianal = np.array([100, 50])
            
            def calc_weapon(weapon: np.array, t: np.linspace = 0) -> np.array:
                return np.array([
                    (first_country_weapon * weapon[1] - first_country_weapon_abrasion * weapon[0] + first_level_of_distrust),
                    (second_country_weapon * weapon[0] - second_country_weapon_abrasion * weapon[1] + second_level_of_distrust),
                ])
                
            weapon = odeint(calc_weapon, initianal, t) 

            first_country, _ = weapon.T
    

            axs[i, j].plot(t, first_country)
            axs[i, j].grid()
            axs[i, j].set_xlabel('Время')
            axs[i, j].set_ylabel('Вооружение')    
            axs[i, j].set_title(f'a1/b2: {k1}, a2/b1: {k2}')
            

    first_country_weapon_abrasion = 0.5
    second_country_weapon_abrasion = 0.5
    first_country_weapon = 0.75
    second_country_weapon = 0.75

    fig, axs = plt.subplots(1, 3, figsize=(10, 6), constrained_layout=True)

    for i, k in enumerate([0.5, 1, 1.5]):
        first_level_of_distrust = k * second_level_of_distrust
    
        initianal = np.array([100, 50])
            
        def calc_weapon(weapon: np.array, t: np.linspace = 0) -> np.array:
            return np.array([
                (first_country_weapon * weapon[1] - first_country_weapon_abrasion * weapon[0] + first_level_of_distrust),
                (second_country_weapon * weapon[0] - second_country_weapon_abrasion * weapon[1] + second_level_of_distrust),
            ])
            
        weapon = odeint(calc_weapon, initianal, t) 

        _, second_country = weapon.T

        axs[i].plot(t, second_country)
        axs[i].grid()
        axs[i].set_xlabel('Время')
        axs[i].set_ylabel('Вооружение')    
        axs[i].set_title(f'h1/h2: {k}')

    plt.show()
