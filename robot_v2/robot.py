#import pygame
from settings import *
from draw import *

class Robot():
    def __init__(self, x_start, y_start):   # задаем начальные координаты робота
        self.robot_height = 50  # размеры робота
        self.robot_width = self.robot_height
        self.angle = 0  # угол поворота
        self.speed = 0.005    # скорость робота
        self.rotation_speed = 1.8   # скорость поворота
        self.cargoTaken = False
        self.vector = pygame.math.Vector2(0, -1) # вектор направления движения
        self.robot = pygame.Surface((self.robot_height, self.robot_width), pygame.SRCALPHA) # создание поверхности робота
        self.robot.fill(YELLOW) # заливка цветом

        pygame.draw.line(self.robot, WHITE, [10, 0], [37, 0], 9)    # линия на роботе
        self.robot_rect = self.robot.get_rect(center =(x_start,y_start))    # получение координат прямоугольника


        self.previous_x_pos = 0
        self.previous_y_pos = 0

    def draw(self):
        self.rotated_robot = pygame.transform.rotozoom(self.robot, self.angle, 0.9)     # повернутая поверхность
        self.robot_rect = self.rotated_robot.get_rect(center=self.robot_rect.center)    # получение координат повернутого прямоугольника
        screen.blit(self.rotated_robot, self.robot_rect)     # отрисовка робота на экране по координатам прямоугольника

    def rotation(self, direction):
        if direction == 1:
            self.angle -= self.rotation_speed # поворот поверхности
            if self.angle <= -359: self.angle = 0
            self.vector.rotate_ip(+self.rotation_speed) # поврот вектора движения

        if direction == -1:
            self.angle += self.rotation_speed
            if self.angle >= 359: self.angle = 0
            self.vector.rotate_ip(-self.rotation_speed)

    def movement(self, move): #какой то косяк с неровным движением
        if move == 1:
            self.robot_rect.center += self.vector * 5.5
        if move == -1:
            self.robot_rect.center -= self.vector * 5.5

    def getRobotPos(self):
        return self.robot_rect.center

    #def goTo(self, x_pos, y_pos):



