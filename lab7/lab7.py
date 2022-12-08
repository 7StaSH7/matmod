import numpy as np 
import matplotlib.pyplot as plt

def fx(x):
    return 0.1 * np.sqrt(x) 

def main() -> None:
    alpha = 0.01
    beta = 0.5
    gamma = 0.7 
    R0 = 40
    M0 = 200

    t = np.linspace(0, 100, 1000)

    M = M0 * np.exp((gamma - beta) * t)
    I = gamma * M

    A = alpha * I
    R = R0 * np.exp(alpha * t)

    x = R / M
    f = fx(x)

    Y = M * f

    otn = (Y - A) / A

    cm = (f - alpha * (alpha - beta)) / x 
    
    norm = A / Y
    
    plt.figure()
    plt.title("Число работающих")
    plt.xlabel('Время')
    plt.plot(t, R)
    
    plt.figure()
    plt.title("Соотношение потребления и накопления")
    plt.xlabel('Время')
    plt.plot(t, otn)

    plt.figure()
    plt.title("Max душевное потребление")
    plt.xlabel('Время')
    plt.plot(t, cm)

    plt.figure()
    plt.title("Норма накопления")
    plt.xlabel('Время')
    plt.plot(t, norm)


    plt.show()