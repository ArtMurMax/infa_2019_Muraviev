from graph import *
import random
import math

width, height = windowSize()


Time = 0


def background(top_sky_color='#fed5a2', mid_sky_color='#fed5c4', bot_sky_color='#fed594', ground_color='#b38694', ):
    penColor(top_sky_color)
    brushColor(top_sky_color)
    rectangle(0, 0, width, height // 6)

    penColor(mid_sky_color)
    brushColor(mid_sky_color)
    rectangle(0, height // 6, width, height // 3)

    penColor(bot_sky_color)
    brushColor(bot_sky_color)
    rectangle(0, height // 3, width, height // 2)

    penColor(ground_color)
    brushColor(ground_color)
    rectangle(0, height // 2, width, height)


def sun(sun_color='#fcee21', x=width // 2, y=height // 6, r=50):
    penColor(sun_color)
    brushColor(sun_color)
    circle(x, y, r)


def half_ellipse(xc, yc, rx, ry, fi: int):
# функция рисования половинок злипсов
# xc, xy - координаты центра элипса
# rx, ry - полуоси элипса
# fi - угол в градусах, на который будет повёрнут элипс
    pos = []
    fi *= math.pi / 180
    for i in range(181):
        x = round(rx * math.cos(i * math.pi / 180))
        y = round(ry * math.sin(i * math.pi / 180))

        x0 = x * math.cos(fi) - y * math.sin(fi)
        y0 = x * math.sin(fi) + y * math.cos(fi)

        pos.append((xc + x0, yc + y0))
    polygon(pos)


def birdman(x, y, k):
# функция рисования чёрной птички
# x, y - координаты нижней точки птицы - хвоста
# k - коэффициент растяжения
    penColor('black')
    brushColor(penColor())
    half_ellipse(x - 7 * k, y - 10 * k, 10 * k, 5 * k, 35)
    half_ellipse(x + 7 * k, y - 10 * k, 10 * k, 5 * k, -25)
    half_ellipse(x - 7 * 2.8 * k, y - 10 * 1.2 * k, 10 * k / 1.5, 5 * k / 1.5, -25)
    half_ellipse(x + 7 * 2.8 * k, y - 10 * 1.1 * k, 10 * k / 1.5, 5 * k / 1.5, 35)


def birdman_drive(dt=0.01):
    global width, height, Time, pos1, pos2, pos3

    background()

    sun()

    # mountains
    N = 20

    penColor('#fc9831')
    brushColor(penColor())

    # pos1 = [(0, height // 3)]
    pos1[1] = pos1[1][1:-2]

    pos1[1].append(height // 3 - N * (height // 3 - height // 4) // N - random.randint(0, 100))
    #pos1[1][-1] - (height // 3 - height // 4) // N - random.randint(0, 10)

    pos1[1].append(height // 4)
    pos1[1].append(height // 3)

    polygon(list(zip(pos1[0], pos1[1])))

    penColor('#ac4334')
    brushColor(penColor())

    pos2 = [(0, height // 2)]

    for i in range(N + 1):
        pos2.append((i * width // N, height // 2 - random.randint(0, 100)))

    pos2.append((width, height // 2))

    polygon(pos2)

    for i in range(random.randint(1, 3)):
        n = random.randint(2, 7)
        j = random.randint(1, n - 1)
        half_ellipse(j * width // n, height // 2, 50, 100, 180)

    penColor('#ac4259')
    brushColor(penColor())

    pos3 = [(0, height)]

    for i in range(N + 1):
        pos3.append((i * width // N, height * 0.95 - (i - 10) * (i - 10) / 30 * random.randint(0, 100)))

    pos3.append((width, height))

    polygon(pos3)

    data = [
        (width // 2 + 50 * (1 + Time), height // 2 - 70 * (1 + Time), 2),
        (width // 2 + 90 * (1 + Time), height // 2 + 130 * (1 + Time), 2),
        (width // 2 - 200 * (1 + Time), height // 2 + 15 * (1 + Time), 2),
        (width // 2 + 90 * (1 + Time), height // 2 - 100 * (1 + Time), 1),
        (width // 2 + 130 * (1 + Time), height // 2 + 100 * (1 + Time), 1),
        (width // 2 + 110 * (1 + Time), height // 2 + 180 * (1 + Time), 2),
        (width // 2 + 150 * (1 + Time), height // 2 + 380 * (1 + Time), 2)
    ]
    for i in range(len(data)):
        birdman(data[i][0], data[i][1], data[i][2])

    Time += 0.01


background()


sun()

# mountains
N = 20

penColor('#fc9831')
brushColor(penColor())

pos1 = [[], []]

for i in range(N + 1):
    pos1[0].append(i * width // N)
    pos1[1].append(height // 3 - i * (height // 3 - height // 4) // N - random.randint(0, 100))

pos1[0].append(width)
pos1[1].append(height // 4)
pos1[0].append(0)
pos1[1].append(height // 3)

polygon(list(zip(pos1[0], pos1[1])))

penColor('#ac4334')
brushColor(penColor())

pos2 = [(0, height // 2)]

for i in range(N + 1):
    pos2.append((i * width // N, height // 2 - random.randint(0, 100)))

pos2.append((width, height // 2))

polygon(pos2)

for i in range(random.randint(1, 3)):
    n = random.randint(2, 7)
    j = random.randint(1, n - 1)
    half_ellipse(j * width // n, height // 2, 50, 100, 180)



penColor('#ac4259')
brushColor(penColor())

pos3 = [(0, height)]

for i in range(N + 1):
    pos3.append((i * width // N, height * 0.95 - (i - 10) * (i - 10) / 30 * random.randint(0, 100)))

pos3.append((width, height))

polygon(pos3)

# birdman(width // 2 + 50, height // 2 - 70, 2)
# birdman(width // 2 + 90, height // 2 + 130, 2)
# birdman(width // 2 - 200, height // 2 + 15, 2)
# birdman(width // 2 + 50 + 40, height // 2 - 70 - 30, 1)
# birdman(width // 2 + 90 + 40, height // 2 + 130 - 30, 1)
# birdman(width // 2 + 50 + 60, height // 2 - 70 + 250, 2)
# birdman(width // 2 + 90 + 60, height // 2 + 130 + 250, 2)

onTimer(birdman_drive, 10)
run()