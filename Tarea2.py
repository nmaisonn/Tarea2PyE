import random


def TiradaJuan():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    if dice1 == 4:
        if dice2 <= 3:
            dice2 = random.randint(1,6)
        return dice2
    elif dice2 == 4:
        if dice1 <= 3:
            dice1 = random.randint(1,6)
        return dice1
    else:
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        if dice1 == 4:
            return dice2
        elif dice2 == 4:
            return dice1
        else:
            return 0
        
def TiradaMaria(tiradaJuan):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    if dice1 == 4:
        if dice2 < tiradaJuan:
            dice2 = random.randint(1,6)
        else if dice2 == tiradaJuan
            if (tiradaJuan/6) > 0.5:
                dice2 = random.randint(1,6)
        return dice2
    elif dice2 == 4:
        if dice1 < tiradaJuan:
            dice1 = random.randint(1,6)
            else if dice1 == tiradaJuan
            if (tiradaJuan/6) > 0.5:
                dice1 = random.randint(1,6)
        return dice1
    else:
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        if dice1 == 4:
            return dice2
        elif dice2 == 4:
            return dice1
        else:
            return 0

def Juego():
    juan = TiradaJuan()
    maria = TiradaMaria(juan)
    if juan > maria:
        #print("Juan gana el Juego.")
        return "Juan"
    elif maria > juan:
        #print("Maria gana el Juego.")
        return "Maria"
    else:
        #print("El Juego termina en empate.")
        return "Empate"
    
def nJuegos(n):
    juan = 0
    maria = 0
    empate = 0
    for i in range(n):
        juego = Juego()
        if juego == "Juan":
            juan += 1
        elif juego == "Maria":
            maria += 1
        else:
            empate += 1
    print("Juan gano",juan,"veces.")
    print("Maria gano",maria,"veces.")
    print("Empate",empate,"veces.") 



print(Juego())
nJuegos(100000)
