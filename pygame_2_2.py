import pygame
import random
pygame.init()

# Размеры окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Анимация фигур")

# Цвета
def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Определение фигур
shapes = [
    {"type": "rectangle", "rect": pygame.Rect(50, 50, 100, 50), "color": random_color(), "dx": 3},
    {"type": "circle", "pos": [300, 150], "radius": 30, "color": random_color(), "dx": 4},
    {"type": "triangle", "points": [(500, 300), (550, 250), (550, 350)], "color": random_color(), "dx": 5}
]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            for shape in shapes:
                if shape["type"] == "rectangle" and shape["rect"].collidepoint(mouse_pos):
                    shape["color"] = random_color()
                elif shape["type"] == "circle" and ((mouse_pos[0] - shape["pos"][0]) ** 2 + (mouse_pos[1] - shape["pos"][1]) ** 2) ** 0.5 < shape["radius"]:
                    shape["color"] = random_color()
                elif shape["type"] == "triangle" and pygame.mouse.get_pressed()[0]:
                    if pygame.draw.polygon(screen, shape["color"], shape["points"]).collidepoint(mouse_pos):
                        shape["color"] = random_color()

    # Движение фигур
    screen.fill((255, 255, 255))  # Цвет фона
    for shape in shapes:
        if shape["type"] == "rectangle":
            shape["rect"].x += shape["dx"]
            if shape["rect"].left < 0 or shape["rect"].right > WIDTH:
                shape["dx"] = -shape["dx"]
                shape["color"] = random_color()
            pygame.draw.rect(screen, shape["color"], shape["rect"])

        elif shape["type"] == "circle":
            shape["pos"][0] += shape["dx"]
            if shape["pos"][0] - shape["radius"] < 0 or shape["pos"][0] + shape["radius"] > WIDTH:
                shape["dx"] = -shape["dx"]
                shape["color"] = random_color()
            pygame.draw.circle(screen, shape["color"], (int(shape["pos"][0]), int(shape["pos"][1])), shape["radius"])

        elif shape["type"] == "triangle":
            for i in range(3):
                shape["points"][i] = (shape["points"][i][0] + shape["dx"], shape["points"][i][1])
            if shape["points"][0][0] < 0 or shape["points"][1][0] > WIDTH:
                shape["dx"] = -shape["dx"]
                shape["color"] = random_color()
            pygame.draw.polygon(screen, shape["color"], shape["points"])

    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()