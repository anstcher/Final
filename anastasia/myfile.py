import random, time
def anastasia_game():
    adiv = {
            "viento" : "Silva sin labios, corre sin pies. En la espalda te pega pero no lo ves.",
            "pizza" : "Un cuadrado tiene de envase, redonda es su base y triangular la porción.",
            "silencio" : "Si me nombras, ya no estoy. Desaparezco.",
            "mapa" : "Hay ríos, pero no agua. Ciudades pero no casas, hay bosques pero no árboles. ¿Dónde?",
            "reloj" : "Todo el día sin parar de trabajar, y no se mueve del sitio."
            }
    def welcome():
        
        print("\nBienvenido al juego de adivinar palabras!")
        print("\nAdivina la palabra letra por letra.\n\nTienes 5 vidas y ayuda - una letra abierta.\n\nAl utilizar la ayuda - te bajarán 50 puntos, al derrotar al boss.")

    def generar_palabra():
        print("\nPensando en la palabra secreta...")
        secretword = random.choice(list(adiv))
        
        time.sleep(0.5)
        print("\n'"+adiv[secretword]+"'")
        print("\n"," _ " *len(secretword))
        
        return secretword
        
    def restar_vida(x):
        
        x-= 1
        print("\n\nJaja! Te equivocsaste!\n\nTe quedan",x, "vidas.")

                
    def help(secretword):
            
            print("\n\nPor lo visto esta adivinanza está difícil para ti...\nBueno... Te bajo la puntuación y seguimos!")
            
            help_l= random.choice(list(secretword))
            print("\nLa letra de ayuda, que te ha tocado es '", help_l,"'")
            return help_l

    def agrupar_letras(secretword,lista_acertada,cont,letras_faltan):
        
        for i in secretword:
            if i in lista_acertada:
                cont += i
            else:
                cont += " _ "
                letras_faltan += 1
                
        print(cont)
        if letras_faltan == 0:
            print("Ganaste!")
        
        return cont
                
        
                
    def main():
        
        vidas = 5
        lista_acertada = []
        cont = ""
        letras_faltan = 0            
        
        welcome()
        
        u = input("\n¿Jugamos?(si/no) -  ")
        u = u.lower()
        
        while True:
            if u == "si" or u == "s":
                secretword = generar_palabra()
                break
                
            elif u == "no" or u == "n":
                print("\nYa veo... Tienes miedo! Mejor...")
                return 99
            
            else:
                print("\nCarecter equivocado.\nIntenta de nuevo")
                        
        x = 0
        while vidas > 0 and secretword != x:
            letra = input("\nIntroduce letra o 33 para ayuda: ")
            letra = letra.lower()
            
            if letra == "33":
                help(secretword)
                
            elif letra not in secretword:
                vidas -=1
                print("\nJaja! Te equivocsaste!\n\nTe quedan",vidas, "vidas.")
            
            elif letra in secretword:
                print();print()
                print("Acertaste la letra")
                
                lista_acertada.append(letra)
                
                x = agrupar_letras(secretword,lista_acertada,cont,letras_faltan)

        if vidas > 0:
            print("\nGanaste!")
            return True
        else:
            print("\nHas perdido. La palabra era: ", secretword)
            return False
    main()
    
anastasia_game()