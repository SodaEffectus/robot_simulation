
from robot import Robot
from beer import Beer
from draw import *
import messages
import math



robot = Robot(width/2, height/2)
beer = Beer()

running = True
while running:
    clock.tick(60) # 60 fps

    for event in pygame.event.get(): # перебирает события
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:# -------------------------------------------------
            if event.key == pygame.K_SPACE: robot.goTo() # если нажали пробел, то робот едет на точку

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE: print("bbb")

    drawWindow()

    beer.draw()

    robot.draw()

    pygame.image.save(screen, 'pic.png')

    if robot.robot_rect.collidepoint(beer.getBeerPos()): # определяет пересечение поверхности робота и поверхности пива
        robot.cargoTaken = True
        beer.beerTaken()    # при взятии пива удаляет его с экрана

    if robot.robot_rect.collidepoint(deliver_pos) and robot.cargoTaken: # если робот попадает в зону доставки, то
        beer.setBeerPos(deliver_pos)    # меняем позицию пива на позицию внутри круга доставка
        robot.cargoTaken = False

#--------------------------

    dx = robot.getRobotPos()[0] - beer.getBeerPos()[0]
    dy = robot.getRobotPos()[1] - beer.getBeerPos()[1]
    dist = math.sqrt(dx*dx + dy*dy)
    if dist !=0:
        vec_x = dx/dist
        vec_y = dy/dist
    vec = (-vec_x, -vec_y)# мб с минусом

    vec2 = pygame.math.Vector2(-vec_x, -vec_y)
    vec2.normalize()



    if vec2.as_polar()[1] < 0:
        if math.fabs(robot.vector.as_polar()[1] - vec2.as_polar()[1]) > 2:
            robot.rotation(-1)
        if math.fabs(robot.vector.as_polar()[1] - vec2.as_polar()[1]) <= 2:
            robot.rotation(1)

    if vec2.as_polar()[1] > 0:
        if math.fabs(robot.vector.as_polar()[1] - vec2.as_polar()[1])  > 2:
            robot.rotation(1)
        if math.fabs(robot.vector.as_polar()[1] - vec2.as_polar()[1]) <= 2:
            robot.rotation(-1)


    print(vec2)

    #robot.vector = vec2
    #robot.vector.update(-vec_x, -vec_y)

# --------------------------
    textsurface = myfont.render("calc vec: " + str(math.floor(vec2.as_polar()[1])), False, (0, 0, 0))
    #textsurface = myfont.render("calc vec: " + str(vec2.as_polar()) + ' calc angle: ' + str(math.degrees(math.acos(vec_y))) + " " + str(math.degrees(math.asin(vec_x))), False, (0, 0, 0))
    textsurface2 = myfont.render("R   vec: " + str(robot.vector), False, (0, 0, 0))
    textsurface3 = myfont.render("polar: " + str(math.floor(robot.vector.as_polar()[1])), False, (0, 0, 0))
    screen.blit(textsurface, (10, 10))
    screen.blit(textsurface2, (10, 50))
    screen.blit(textsurface3, (10, 100))

    keys = pygame.key.get_pressed()  # список, в который помещается нажатая кнопка
    if keys[pygame.K_LEFT]:
        robot.rotation(-1)
    if keys[pygame.K_RIGHT]:
        robot.rotation(1)
    if keys[pygame.K_UP]:
        robot.movement(1)
    if keys[pygame.K_DOWN]:
        robot.movement(-1)

    #if keys[pygame.K_SPACE]:
        #pygame.image.save(screen, 'pic.png')

    pygame.display.update()  # обновление окна

pygame.quit()