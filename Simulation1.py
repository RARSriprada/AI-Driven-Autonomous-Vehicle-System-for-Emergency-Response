import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Autonomous Vehicle System")

BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
LANE_CENTERS = [150, 300, 450, 600]


class Vehicle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.width = 40
        self.height = 60
        self.color = color
        self.speed = 1.5
        self.detected = False

    def move(self):
        if not self.detected:
            self.y += self.speed
        else:
            self.y += self.speed // 2
        if self.y > HEIGHT:
            self.y = -self.height
            self.x = random.choice(LANE_CENTERS) - 20  # Move between lanes, not directly on them

    def change_lane(self):
        if self.detected:
            new_lane = random.choice([lane for lane in LANE_CENTERS if lane != self.x]) - 20
            self.x = new_lane

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x - self.width // 2, self.y, self.width, self.height))


cars = [Vehicle(random.choice(LANE_CENTERS) - 20, random.randint(-600, 0), BLUE) for _ in range(5)]
ambulance = Vehicle(300 - 20, -100, RED)
ambulance.speed = 2.5


def check_detection():
    for car in cars:
        if abs(car.y - ambulance.y) < 100 and abs(car.x - ambulance.x) < 50:
            car.detected = True
            car.change_lane()
        else:
            car.detected = False


def draw_road():
    screen.fill(GRAY)
    for lane in LANE_CENTERS:
        pygame.draw.rect(screen, WHITE, (lane - 5, 0, 10, HEIGHT))


running = True
zoomed_in = False
zoom_timer = 0
while running:
    screen.fill(GRAY)
    draw_road()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ambulance.move()
    check_detection()

    if any(car.detected for car in cars):
        if not zoomed_in:
            WIDTH, HEIGHT = 1000, 800
            screen = pygame.display.set_mode((WIDTH, HEIGHT))
            zoomed_in = True
            zoom_timer = pygame.time.get_ticks()

    if zoomed_in and pygame.time.get_ticks() - zoom_timer > 3000:
        WIDTH, HEIGHT = 800, 600
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        zoomed_in = False

    for car in cars:
        car.move()
        car.draw(screen)

    ambulance.draw(screen)
    pygame.display.flip()
    pygame.time.delay(50)

pygame.quit()
