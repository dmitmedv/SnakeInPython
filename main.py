# подключение игрового движка pygame
import pygame
# подключение модуля случайных чисел
# для генерации яблок итд
import random

# инициализация pygame
pygame.init()

# коды цветов использующиеся в игре
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# размеры игрового поля
dis_width = 600
dis_height = 400

# инициализация окна
dis = pygame.display.set_mode((dis_width, dis_height))
# установка текста окна
pygame.display.set_caption('Snake by MEDVEDEV IT SCHOOL')

# создание объекта Clock для работы со временем
clock = pygame.time.Clock()

# размер блока змейки
snake_block = 10
# скорость игры
snake_speed = 10

# создание шрифтов
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# функция вывода счета игры
def Your_score(score):
    # создание выводимого текста
    text = score_font.render("Your Score: " + str(score), True, yellow)
    # добавление текста в окно с координатами (0, 0)
    dis.blit(text, [0, 0])

# функция отрисовки тела змейки
def our_snake(snake_block, snake_list):
    # цикл перебирает все элементы змейки
    for x in snake_list:
        # отрисовка прямоугольника
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

# функция для отображения сообщения msg
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

# функция запуска игры
def gameLoop():
    # переменная хранит состояние игры: True - конец игры, иначе False
    game_over = False
    game_close = False # для фиксации game

    # вычисление изначального положения змейки
    x1 = dis_width / 2
    y1 = dis_height / 2

    # вспомогательные переменные для движения змейки
    x1_change = 0   # смещение по оси Х
    y1_change = 0   # смещение по оси У

    # список для хранения звеньев змейки
    snake_List = []
    # длина змейки
    Length_of_snake = 1

    # генерация координат для яблока
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    # основной игровой цикл
    while not game_over:
        # цикл для обработки конца игры
        while game_close == True:
            # заполнение поля цветом
            dis.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # обработка событий
        for event in pygame.event.get():
            # если нажат крестик в окне игры
            if event.type == pygame.QUIT:
                game_over = True
            # если нажата любая клавиша
            if event.type == pygame.KEYDOWN:
                # если нажата стрелка влево
                if event.key == pygame.K_LEFT:
                    # смещение по Х будет отрицательным
                    x1_change = -snake_block
                    # смещение по У не будет т.к. движение влево
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # проверка ухода змейки за границы экрана
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        # смещение головы змейки в соответсвующем направлении
        x1 += x1_change
        y1 += y1_change
        # заполнение фона
        dis.fill(blue)

        # отрисовка яблока
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])

        # создание звена змейки
        snake_Head = []
        # добавление координат звена змейки
        snake_Head.append(x1)
        snake_Head.append(y1)
        # добавление звена змейки в общий список звеньев
        snake_List.append(snake_Head)

        # если кол-во звеньев змейки больше длины
        if len(snake_List) > Length_of_snake:
            # удаляем звено из хвоста
            del snake_List[0]

        # проверка столкновения головы и хвоста
        for x in snake_List[:-1]:
            # если элемент змейки равен голове
            if x == snake_Head:
                game_close = True

        # отрисовка змейки
        our_snake(snake_block, snake_List)
        # отрисовка счета
        Your_score(Length_of_snake - 1)

        # перерисовка нового кадра игры
        pygame.display.update()

        # проверка столкновения с яблоком
        if x1 == foodx and y1 == foody:
            # генерация новых координат яблока
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            # увеличение длины змейки
            Length_of_snake += 1

        # установка скорости игры
        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Запуск игры
gameLoop()