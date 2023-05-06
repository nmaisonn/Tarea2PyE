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
        
# Tirada de Maria conociendo la tirada de Juan, utilizando la estrategia desarrollada por el equipo.
def TiradaMaria(tiradaJuan):
    # Maria tira dados por primera vez.
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)

    # Verificamos si alguno de los dados es un 4.
    if dice1 == 4:
        # Si el puntaje de maria es menor al de Juan, tira nuevamente el dado que no es un 4.
        if dice2 < tiradaJuan:
            dice2 = random.randint(1,6)
        # Si el puntaje de maria es igual al de Juan, tira nuevamente el dado que no es un 4, solo si la probabilidad de que el dado sea mayor a 4 es mayor o igual a 4/6.
        # Es decir, Maria tira nuevamente solo si empatan en un puntaje menor o igual a 3.
        elif dice2 == tiradaJuan:
            if ( (6 - tiradaJuan)/6 ) >= 4/6:  # (6 - tiradaJuan)/6 es la probabilidad de obtener un puntaje mayor o igual al de Juan.
                dice2 = random.randint(1,6)
        return dice2
    elif dice2 == 4:
        # Lo mismo que antes pero con el otro dado.
        if dice1 < tiradaJuan:
            dice1 = random.randint(1,6)
        elif dice1 == tiradaJuan:
            if ( (6 - tiradaJuan)/6 ) > 0.5:
                dice1 = random.randint(1,6)
        return dice1
    
    # Si ninguno de los dados es un 4, se tira nuevamente.
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
