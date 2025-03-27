import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE) # рисуем окно, делаем его изменяемым
screen.fill([255, 255, 255])
pygame.display.set_caption('Первая программа в pygame') # заголовок окна

# Создание кургов с разными способами задания цвета
pygame.draw.circle(screen, 'red', [200, 100], 30, width=0)
pygame.draw.circle(screen, [255, 154, 13], [100, 400], 50, width=15)
pygame.draw.circle(screen, '#FFEE54', [400, 300], 100, width=5)

# Создать прямоугольник
pygame.draw.rect(screen, 'yellow', [300, 10, 200, 100], 0)

# Создать пять рандомных по размеру и положению прямоугольников
for i in range(5):
    top = random.randint(50, 700)
    left = random.randint(50, 500)
    w = random.randint(10, 200)
    h = random.randint(10, 100)
    color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
    pygame.draw.rect(screen, color, [top, left, w, h], 4)

# Создание домика
# Стены домика
house_x = 350
house_y = 300
house_width = 100
house_height = 100
pygame.draw.rect(screen, 'brown', [house_x, house_y, house_width, house_height])

# Крыша домика
roof_points = [
    (house_x, house_y),                         # Нижний левый угол
    (house_x + house_width / 2, house_y - 50), # Верхний центр
    (house_x + house_width, house_y)           # Нижний правый угол
]
pygame.draw.polygon(screen, 'red', roof_points)

# Яблоко на экране
apple = pygame.image.load('apple.png')
screen.blit(apple, [600, 450])
pygame.display.flip()

# Передвинуть изображение в новые координаты
pygame.time.delay(2000)
pygame.draw.rect(screen, 'white', [600, 450, 77, 75], 0)
screen.blit(apple, [500, 350])
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
