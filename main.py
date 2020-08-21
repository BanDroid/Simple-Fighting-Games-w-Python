# importing random modules, so the action value will be randomly generated
import random

# here we're making the player and the enemy health value, because why not?
player = 100 # player's health
enemy = 100 # enemy's health

# we need to limit the skills action, so the player will not easily win, and not getting bored
skills = 1 # you can change the limit of skills action

# and we need the NPS guy that will guide you through the journey
guide = "attack, defends, skills,\nor surrender?"

# and because this is a game, we need to make the code always running until the player lose or win
while True: # so we're making the condition always True

# and here, the code section will get more crazy
# yeah, we're making the gameplay and its action

# for the first action, need to make a condition if the player's health was 0 or less, when it comes to 0, the player lost
  if player <= 0:
    print("you lost!")
    break # when the player lost, we need to stop the game, so we break the loop

# for the second action, we need to make the condition when the enemy's health is 0 or less
# of course we want the enemy can be defeated right?
  elif enemy <= 0:
    print("you win!")
    break # like the player's, when enemy lost, we stop the game, so we break the loop

# for the third action, we make the gameplay, what is this game about, and the battle is executed here
  else: # of course we dont need elif anymore, cause this is the last condition

# for the gameplay action, we will asking the player what action should he/she do
# dont forget the guide guy, he will give you a guide what action you will choose
    action = input(guide)

# and for the action, you'll know it from the names right? like attack, defends, skills, or surrender. you know what that means right?
    if action == "attack":

      # here it comes the random function, the player and the enemy takes the same range damages, so this is fair
      enemy = enemy - random.randint(1, 31)
      player = player - random.randint(1, 31)

  # this code block will executed if there's no available skill moves, so we put it upper the skills action block, and if we can't use skills anymore, the guide guy will inform us, and continue the loop
    elif skills <= 0:
      guide = "no more skills"
      continue

  # this is the skills action, almost same like attacking, but we give it more damage, and the enemy will give us less damage
    elif action == "skills":
      enemy = enemy - random.randint(10, 41)
      player = player - random.randint(1, 26)
      skills -= 1 # and because we're using skills, so the available skill moves decrease to 0, so in the next action, we can't use the skills

  # this is the defends action, and because of the names "defends", we can't give the enemy a damage, but this tactic will decrease the damage that we take
    elif action == "defends":
      player = player - random.randint(1, 11)

  # for the last choosen action was surrender, we dont need to write the condition, cause this is the last action that we could choose, so if the player given a number input, another words like "BanDroid is handsome", or something else, this code will executed, the program will taking a surrender action
    else:
      print("you're surrender")
      break # and we're break the loop

  # and after all the code above executed, and if the battle is not over, the guide guy will inform you about the rest of yours and enemies health, and the player must continue this battle until find who's the winner
    guide = "your health : " + str(player) + "\nenemy health : " + str(enemy)