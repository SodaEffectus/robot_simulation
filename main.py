#version 0.1




import pygame


width = 800
height = 650
YELLOW = (253, 165, 15)
GREY = (128, 128, 128)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

pygame.init() # инициализация пайгейм
screen = pygame.display.set_mode((width, height)) # создаем окно
pygame.display.set_caption("ROBOT SIMULATION") # название окна
clock = pygame.time.Clock() # время
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

class Robot():
    def __init__(self, x_start, y_start):   # задаем начальные координаты робота
        self.robot_height = 50  # размеры робота
        self.robot_width = self.robot_height
        self.angle = 0  # угол поворота
        self.speed = 0.005    # скорость робота
        self.rotation_speed = 1.8   # скорость поворота
        self.vector = pygame.math.Vector2(0, -1) # вектор направления движения
        self.robot = pygame.Surface((self.robot_height, self.robot_width), pygame.SRCALPHA) # создание поверхности робота
        self.robot.fill(YELLOW) # задивка цветом

        pygame.draw.line(self.robot, WHITE, [10, 0], [37, 0], 9)    # линия на роботе
        self.robot_rect = self.robot.get_rect(center =(x_start,y_start))    # получение координат прямоугольника

    def draw(self):
        self.rotated_robot = pygame.transform.rotozoom(self.robot, self.angle, 0.9)     # повернутая поверхность
        self.robot_rect = self.rotated_robot.get_rect(center=self.robot_rect.center)    # получение координат повернутого прямоугольника
        screen.blit(self.rotated_robot, self.robot_rect)     # отрисовка робота на экране по координатам прямоугольника

    def rotation(self, direction):
        if direction == 1:
            self.angle -= self.rotation_speed # поворот поверхности
            self.vector.rotate_ip(+self.rotation_speed) # поврот вектора движения

        if direction == -1:
            self.angle += self.rotation_speed
            self.vector.rotate_ip(-self.rotation_speed)

    def movement(self, move): #какой то косяк с неровным движением
        if move == 1:
            self.robot_rect.center += self.vector * 5.5
        if move == -1:
            self.robot_rect.center -= self.vector * 5.5






def drawWindow():
    screen.fill(GREY)   # отрисовка фона
    pygame.draw.rect(screen, (28, 32, 40), (0, 0, width, height), 15)


robot = Robot(500,500)

running = True
while running:
    clock.tick(60) # 60 fps

    for event in pygame.event.get(): # перебирает события
        if event.type == pygame.QUIT:
            running = False

    drawWindow()

    robot.draw()
    textsurface = myfont.render(str(robot.vector), False, (0, 0, 0))
    screen.blit(textsurface, (10, 10))

    keys = pygame.key.get_pressed()  # список, в который помещается нажатая кнопка
    if keys[pygame.K_LEFT]:
        robot.rotation(-1)
    if keys[pygame.K_RIGHT]:
        robot.rotation(1)
    if keys[pygame.K_UP]:
        robot.movement(1)
    if keys[pygame.K_DOWN]:
        robot.movement(-1)




    pygame.display.update()  # обновление окна

pygame.quit()
