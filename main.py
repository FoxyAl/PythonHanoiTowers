import pygame
from tkinter import *

window = Tk()
window.title("Настройка Ханойских башен")
window.geometry('1000x600')


def pygame_window(q, speed):
    screen_width = 800
    screen_height = 600
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Ханойские башни")
    sticks = [[i for i in range(q)], [], []]
    COLOR = (0, 255, 0)
    builds_center_positions = [screen_width / 4 * i for i in range(1, 4)]
    min_disk_width = 16
    max_disk_width = screen_width / 4 - 10
    disk_height = 10

    def get_disk_length(i_build, i_disk):
        return min_disk_width + (max_disk_width - min_disk_width) / q * (q -
                                                                     sticks[i_build][i_disk])

    def get_coord_disk(i_build, i_disk):
        y = screen_height - (disk_height * (i_disk + 1))

        w = get_disk_length(i_build, i_disk)
        x = builds_center_positions[i_build] - w / 2
        h = disk_height
        return x, y, w, h

    def draw():
        pygame.draw.rect(screen, (0, 0, 0), (0, 0, screen_width, screen_height))

        for i in range(len(sticks)):
            for j in range(len(sticks[i])):
                x, y, w, h = get_coord_disk(i, j)
                pygame.draw.rect(screen, COLOR, (x, y, w, h))

    def game_tick():
        draw()

        pygame.display.update()
        pygame.time.delay(speed)

    def Hanoi(q, source, destination, auxiliary):
        if q == 0:
            return

        Hanoi(q - 1, source, auxiliary, destination)
        game_tick()
        sticks[destination].append(sticks[source].pop())
        Hanoi(q - 1, auxiliary, destination, source)
    Hanoi(q, 0, 2, 1)
    game_tick()
    pygame.quit()


lbl3 = Label(window, text="", font=("Arial Bold", 20))
lbl3.grid(column=0, row=4)


def q_change(q):
    if ((2 ** q - 1) % 10 == 1):
        lbl3['text'] = f"Всего нам понадобился {2 ** q - 1} ход."
    elif ((2 ** q - 1) % 10 == 3):
        lbl3['text'] = f"Всего нам понадобилось {2 ** q - 1} хода."
    else:
        lbl3['text'] = f"Всего нам понадобилось {2 ** q - 1} ходов."


item_1 = Spinbox(window, from_=1, to=16, width=5)
item_1.grid(row=1, column=2)
item_2 = Spinbox(window, from_=100, to=1000, width=5, increment=100)
item_2.grid(row=2, column=2)


def play():
    q = int(item_1.get())
    if q > 10 or q < 1:
        lbl3['text'] = "Введите число дисков от 1 до 10"
    else:
        speed = int(item_2.get())
    if speed > 1000 or speed < 100:
        lbl3['text'] = "Введите скорость перемещения дисков от 100 до 1000"
    else:
        q_change(q)
    pygame_window(q, speed)


lbl = Label(window, text="Выберите количество дисков", font=("Arial Bold",
                                                             20))
lbl.grid(column=0, row=1)
lbl = Label(window, text="Выберите скорость перемещения дисков",
            font=("Arial Bold", 20))
lbl.grid(column=0, row=2)
btn = Button(window, text="Запустить", font=("Arial Bold", 20), command=play)
btn.grid(column=2, row=3)
window.mainloop()
