from matplotlib.patches import *
import matplotlib.pyplot as plt
import math
import numpy as np


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
maxLength = math.floor((V0**2*math.sin(2*alpha0)) / g)
maxTime = 2 * V0 * math.sin(alpha0) / g

print("V0: ", V0)
print("maxLength: ", maxLength)
print("math.sin(alpha0): ", math.sin(alpha0))
print("maxTime: ", maxTime)


def rotate(origin, point, angle):
    """
    Rotate a point counterclockwise by a given angle around a given origin.

    The angle should be given in radians.
    """
    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return qx, qy


def calcAngle(vector1, vector2):
    x1, y1 = vector1
    x2, y2 = vector2
    inner_product = x1 * x2 + y1 * y2
    len1 = math.hypot(x1, y1)
    len2 = math.hypot(x2, y2)
    return math.acos(inner_product / (len1 * len2))


def ccw(A, B, C):
    return (C[1] - A[1]) * (B[0] - A[0]) > (B[1] - A[1]) * (C[0] - A[0])


def isIntersect(A, B, C, D):
    return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)


def calcIsScored(playerX, playerY):
    playerCords = np.array([playerX, playerY])
    goalCordsWithoutRotate = np.array([playerX + maxLength, playerY])

    angle = calcAngle(np.array([gateX, gateYMiddle] - playerCords),
                      np.array([playerX + maxLength, playerY]) - playerCords)

    if playerY > fieldWidth / 2:
        angle = -angle

    goalCords = rotate(playerCords, goalCordsWithoutRotate, angle)
    timeToGateX = (goalCords[0] - playerX) / (V0 * math.cos(alpha0))
    if timeToGateX > maxTime:
        timeToGateX = 0

    isHop = V0 * math.sin(alpha0) * timeToGateX - (g * timeToGateX **
                                                   2) / 2 > gateHeight if timeToGateX > 0 else False

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
for playerX in range(fieldLength):
    for playerY in range(fieldWidth):
        isScored = calcIsScored(playerX, playerY)
        if isScored:
            ax.add_patch(plt.Circle((playerX, playerY), 0.6, color="black"))

print('Вычислено')
plt.show()
