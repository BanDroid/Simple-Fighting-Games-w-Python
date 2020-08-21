import random

player = 100
enemy = 100

skills = 1

guide = "attack, defends, skills,\nor surrender?"

while True:
    if player <= 0:
        print("you lost!")
        break
    elif enemy <= 0:
        print("you win!")
        break
    else:
        action = input(guide)

        if action == "attack":
            enemy = enemy - random.randint(1, 31)
            player = player - random.randint(1, 31)

        elif skills <= 0:
            guide = "no more skills"
            continue

        elif action == "skills":
            enemy = enemy - random.randint(10, 41)
            player = player - random.randint(1, 26)
            skills -= 1

        elif action == "defends":
            player = player - random.randint(1, 11)

        else:
            print("you're surrender")
            break

        guide = "your health : " + str(player) + "\nenemy health : " + str(enemy)
