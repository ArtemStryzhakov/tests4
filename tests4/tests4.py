import random
import time

carts = ["шестерка", "семерка", "восьмерка", "девятка", "десятка", "валет", "дама", "король", "туз"] * 4
balls = [6, 7, 8, 9, 10, 2, 3, 4, 11] * 4

print("Добро пожаловать в игру под названием '21'. Ваша задача набрать больше всего очков среди опонентов, при этом очки не должны привысить 21 очка.\nВ начале игры ваш и вашему опоненту выдадут две карты.")
buffer = input("Как вы хотите сыграть? [1-с ботом, 2-с другом]: ")
if buffer == "1":
    balls_for_bot = 0
    for x in range(2): #Раздаём две карты боту
        random_for_bot1 = random.choice(carts)
        index_bot1 = carts.index(random_for_bot1)
        balls_for_bot += balls[index_bot1]
        print(f"Боту выдали карту {random_for_bot1} с достоинством {balls[index_bot1]}.")
        carts.remove(random_for_bot1)
        balls.pop(index_bot1)

    balls_for_player = 0
    for y in range(2): #Раздаём две карты игроку
        random_for_game1 = random.choice(carts)
        index_ball1 = carts.index(random_for_game1)
        balls_for_player += balls[index_ball1]
        print(f"Вам выдали карту {random_for_game1} с достоинством {balls[index_ball1]}.")
        carts.remove(random_for_game1)
        balls.pop(index_ball1)

    print(f"У бота очков {balls_for_bot}")
    print(f"У вас очков {balls_for_player}.")

    def bot(carts, balls):
        random_Gay = random.randint(1, 100)
        if random_Gay < 80:
            random_for_One = random.choice(carts)
            index_bot = carts.index(random_for_One)
            global balls_for_bot
            balls_for_bot += balls[index_bot]
            if balls_for_bot > 21:
                print(f"Боту выпала карта {random_for_One} с достоинством {balls[index_bot]}.")
                print(f"У бота очков {balls_for_bot}.")
                print("Вы выйграли, бот проиграл.")
                time.sleep(3)
                raise SystemExit()
            else:
                print(f"Боту выпала карта {random_for_One} с достоинством {balls[index_bot]}.")
                print(f"У бота очков {balls_for_bot}.")
                carts.remove(random_for_One)
                balls.pop(index_bot)
        else:
            print("Бот не берёт карту.")
            pass

    while True:
        if balls_for_player > 21 and balls_for_bot > 21:
            print("Ничья.")
        if balls_for_player == 21:
            print("У вас блэк джек, чистая победа!")
            time.sleep(3)
            break
        elif balls_for_bot == 21:
            print("У бота блэк джек, вы проиграли в сухую!")
            time.sleep(3)
            break
        quetion = input("Хотите взять карту? [да/нет]: ")
        if quetion == "да" or quetion == "yes":
            random_for_game = random.choice(carts)
            index_ball = carts.index(random_for_game)
            balls_for_player += balls[index_ball]
            if balls_for_player > 21:
                print(f"Вам выпала карта {random_for_game} с достоинством {balls[index_ball]}.")
                print(f"У вас очков {balls_for_player}.")
                print("Вы проиграли, бот выйграл.")
                time.sleep(3)
                break
            else:
                print(f"Ваш выпала карта {random_for_game} с достоинством {balls[index_ball]}.")
                print(f"У вас очков {balls_for_player}.")
            carts.remove(random_for_game)
            balls.pop(index_ball)
            if balls_for_bot >= 18:
                random_for_Gay = random.randint(1,100)
                if random_for_Gay < 60:
                    bot(carts, balls)
                else:
                    print("Бот не берёт карту.")
                    pass
            else:
                bot(carts, balls)

        elif quetion == "нет" or quetion == "no":
            bot(carts, balls)
        else:
            print("Таковой команды нет. ")
elif buffer == "2":
    balls_for_one = 0
    for x in range(2): #Раздаём две карты вам
        random_for_one = random.choice(carts)
        index_player1 = carts.index(random_for_one)
        balls_for_one += balls[index_player1]
        print(f"Первому игроку выдали карту {random_for_one} с достоинством {balls[index_player1]}.")

    balls_for_second = 0
    for y in range(2): #Раздаём две карты второму игроку
        random_for_two = random.choice(carts)
        index_player2 = carts.index(random_for_two)
        balls_for_second += balls[index_player2]
        print(f"Второму игроку карту {random_for_two} с достоинством {balls[index_player2]}.")

    print(f"У первого игрока очков {balls_for_one}")
    print(f"У второго игрока очков {balls_for_second}.")

    while True:
        if balls_for_one > 21 and balls_for_second > 21:
            print("Ничья.")
        if balls_for_one == 21:
            print("У первого игрока блэк джек, победа за первым игроком!")
            time.sleep(3)
            break
        elif balls_for_second == 21:
            print("У второго игрока блэк джек, победа за вторым игроком!")
            time.sleep(3)
            break
        For_player1 = input("Первый игрок хочет взять карту? [да/нет]: ")
        if For_player1 == "да" or For_player1 == "yes":
            cart_for_player1 = random.choice(carts)
            index_player_1 = carts.index(cart_for_player1)
            balls_for_one += balls[index_player_1]
            if balls_for_one > 21:
                print(f"Первому игроку выпала карта {cart_for_player1} с достоинством {balls[index_player_1]}.")
                print(f"У первого игрока очков {balls_for_one}.")
                print("Первый игрок проиграл, второй игрок выйграл.")
                time.sleep(3)
                break
            else:
                print(f"Первому игроку выпала карта {cart_for_player1} с достоинством {balls[index_player_1]}.")
                print(f"У первого игрока очков {balls_for_one}.")
            carts.remove(cart_for_player1)
            balls.pop(index_player_1)
        elif For_player1 == "нет" or For_player1 == "no":
            print("Первый игрок пропускает ход.")
            pass
        else:
            print("Такой команды нет.")

        if balls_for_one == 21:
            print("У первого игрока блэк джек, победа за первым игроком!")
            time.sleep(3)
            break

        For_player2 = input("Второй игрок хочет взять карту? [да/нет]: ")
        if For_player2 == "да" or For_player2 == "yes":
            cart_for_player2 = random.choice(carts)
            index_player_2 = carts.index(cart_for_player2)
            balls_for_second += balls[index_player_2]
            if balls_for_second > 21:
                print(f"Второму игроку выпала карта {cart_for_player1} с достоинством {balls[index_player_1]}.")
                print(f"У второго игрока очков {balls_for_one}.")
                print("Второй игрок проиграл, первый игрок выйграл.")
                time.sleep(3)
                break
            else:
                print(f"Второму игроку выпала карта {cart_for_player1} с достоинством {balls[index_player_1]}.")
                print(f"У второго игрока очков {balls_for_one}.")
            carts.remove(cart_for_player1)
            balls.pop(index_player_1)
        elif For_player1 == "нет" or For_player1 == "no":
            print("Второй игрок пропускает ход.")
            pass
        else:
            print("Такой команды нет.")

        if balls_for_second == 21:
            print("У второго игрока блэк джек, победа за вторым игроком!")
            time.sleep(3)
            break
