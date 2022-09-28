from matplotlib.patches import *
import matplotlib.pyplot as plt
import math
import numpy as np
from shapely.geometry import LineString

V0 = (float(input("Введите скорость мяча после удара (км/ч): ")) * 1000) / 3600
alpha0 = math.radians(
    float(input("Введите угол, под которым был ударен мяч (градусы): ")))


g = 9.8
fieldLength, fieldWidth = 105, 68,
gateHeight, gateWidth = 2.44, 7.32


gateX = fieldLength
gateYMiddle, gateYBottom, gateYUpper = fieldWidth / 2, fieldWidth / 2 - \
    gateWidth / 2, fieldWidth / 2 + gateWidth / 2


gateButtomCords = np.array([gateX, gateYBottom])
gateUpperCords = np.array([gateX, gateYUpper])
maxLength = math.floor((V0**2 * math.sin(2 * alpha0)) / g)
maxTime = 2 * V0 * math.sin(alpha0) / g

print("V0: ", V0)
print("maxLength: ", maxLength)
print("math.sin(alpha0): ", math.sin(alpha0))
print("maxTime: ", maxTime)


def rotate(origin, point, angle):

    R = np.array([[np.cos(angle), -np.sin(angle)],
                  [np.sin(angle),  np.cos(angle)]])
    o = np.atleast_2d(origin)
    point = np.atleast_2d(point)
    return np.squeeze((R @ (point.T-o.T) + o.T).T)


def dotproduct(v1, v2):
    return sum((a * b) for a, b in zip(v1, v2))


def length(v):
    return math.sqrt(dotproduct(v, v))


def angleBetween(v1, v2):
    if length(v1) * length(v2) == float(0):
        return 0
    return math.acos(dotproduct(v1, v2) / (length(v1) * length(v2)))


def ccw(A, B, C):
    return (C[1] - A[1]) * (B[0] - A[0]) > (B[1] - A[1]) * (C[0] - A[0])


def isIntersect(A, B, C, D):
    return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)


def angle_between(v1, v2):
    if length(v1) * length(v2) == float(0):
        return 0
    return math.acos(dotproduct(v1, v2) / (length(v1) * length(v2)))


def calcIsScored(playerX, playerY):
    playerCords = np.array([playerX, playerY])
    goalCordsWithoutRotate = np.array([playerX + maxLength, playerY])

    angle = angleBetween(np.array([gateX, gateYMiddle] - playerCords),
                         np.array(goalCordsWithoutRotate - playerCords),)

    if playerY > fieldWidth / 2:
        angle = -angle

    goalCords = rotate(playerCords, goalCordsWithoutRotate, angle)

    timeToGateX = (gateX - playerX) / (V0 * math.cos(alpha0))

    if timeToGateX > maxTime:
        timeToGateX = 0

    isHop = V0 * math.sin(alpha0) * timeToGateX - \
        (g * timeToGateX**2) / 2 > gateHeight

    if (isIntersect(playerCords, goalCords, [gateX, gateYBottom], [gateX, gateYUpper]) and not isHop):
        return True

    return False


fig = plt.figure()
fig.set_size_inches(7, 5)
ax = fig.add_subplot(1, 1, 1)

Pitch = Rectangle([0, 0], width=fieldLength, height=fieldWidth, fill=False)

Gate = Rectangle(
    [fieldLength - 0.5, fieldWidth / 2 - gateWidth / 2], width=1, height=gateWidth, fill=True)

element = [Pitch, Gate]
for i in element:
    ax.add_patch(i)

plt.ylim(-2, 82)
plt.xlim(-2, 122)
plt.axis('off')

print('Вычисляем...')
for playerX in range(fieldLength + 1):
    for playerY in range(fieldWidth + 1):
        isScored = calcIsScored(playerX, playerY)
        if isScored:
            ax.add_patch(plt.Circle((playerX, playerY), 0.6, color="black"))

print('Вычислено')
plt.show()
