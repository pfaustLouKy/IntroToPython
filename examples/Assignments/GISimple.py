import random

def GISimple(impSpd=(1, 9), golemSpd=(3, 5), headStart=5, exitPosition=50):
    imp_position = headStart
    golem_position = 0

    while imp_position < exitPosition and golem_position < exitPosition:
        imp_move = random.randint(impSpd[0], impSpd[1])
        golem_move = random.randint(golemSpd[0], golemSpd[1])

        imp_position += imp_move
        golem_position += golem_move

        if imp_position >= exitPosition:
            return True
        elif golem_position >= imp_position:
            return False

result = GISimple()
print(result)
