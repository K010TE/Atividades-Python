#Um hotel onde os hóspedes têm algumas restrições quanto a localização de seu quarto, seguindo as seguintes regras: 
#• O rato não pode ficar ao lado do gato. 
#• O cão não pode ficar ao lado do osso. 
#• O gato não pode ficar ao lado do cão. 
#• O queijo não pode ficar ao lado do rato 

#O jogo é composto por 4 fases, onde cada fase (a partir da fase 2) só é desbloqueada se a anterior for concluída com êxito.

#O código foi feito utilizando procedures para ocasiões repetitivas

print('\n\n   HOTEL DOS BICHOS   \n\n')
print('Especificando posições:')
print('[1, 2, 3, 4]')
print('[5, 6, 7, 8]')

fase = 1

#a procedure fasen recebe o numero da fase como parâmetro para personalizar a mensagem de acordo com a fase do jogo
def fasen(fase):
    print('\n\nBem-vinde à fase {}'.format(fase))
    print('Na fase {}, o jogador deve alocar: '.format(fase))



lista1 = ['*', '*', '_', 'G']
lista2 = ['R', '_', '*', '*']

fasen(fase)
print('o RATO e o GATO na seguinte matriz que representa os quartos:')

#função que mostra a distribuição de espaços no hotel
def mostralistas():
    print(lista1)
    print(lista2)
mostralistas()

#procedures de pergunta muda de acordo com fase do jogo, mas é importante porque serve de validação e recursividade

def pergunta():
    global p1
    p1= int(input('Em qual posição quer alocar o RATO? '))
    global p2
    p2 = int(input('Em qual posição quer alocar o GATO? '))
    if((p1 > 8 or p1 < 1) or (p2 > 8 or p2 < 1)):
        print('Número inválido')
        pergunta()

def pergunta2():
    global p1
    p1= int(input('Em qual posição quer alocar o CÃO? '))
    global p2
    p2 = int(input('Em qual posição quer alocar o outro CÃO? '))
    global p3
    p3 = int(input('Em qual posição quer alocar o OSSO? '))
    if((p1 > 8 or p1 < 1) or (p2 > 8 or p2 < 1) or (p3 > 8 or p3 < 1)):
        print('Número inválido')
        pergunta2()

def pergunta3():
    global p1
    p1= int(input('Em qual posição quer alocar o GATO? '))
    global p2
    p2 = int(input('Em qual posição quer alocar o RATO? '))
    global p3
    p3 = int(input('Em qual posição quer alocar o OSSO? '))
    if((p1 > 8 or p1 < 1) or (p2 > 8 or p2 < 1) or (p3 > 8 or p3 < 1)):
        print('Número inválido')
        pergunta3()

def pergunta4():
    global p1
    p1= int(input('Em qual posição quer alocar o QUEIJO? '))
    global p2
    p2 = int(input('Em qual posição quer alocar o outro QUEIJO? '))
    global p3
    p3 = int(input('Em qual posição quer alocar o OSSO? '))
    if((p1 > 8 or p1 < 1) or (p2 > 8 or p2 < 1) or (p3 > 8 or p3 < 1)):
        print('Número inválido')
        pergunta4()

#O restante da aplicação foi feita com sistema de condições if e else e acabou ficando longo e complexo apesar da lógica ser simples

pergunta()
if((p1 !=6) or(p2!=3)):
    print('GAME OVER!!')
else:
    print('PARABÉNS!!')
    print('Vamos à próxima fase')

    fase = 2
    fasen(fase)
    print('dois CÃES e o OSSO na seguinte matriz que representa os quartos:')
    lista1 = ['_', '*', '*', '*']
    lista2 = ['*', 'C', '_', '_']

    mostralistas()
    pergunta2()
    if(p1 == 6):
        print('Posição inválida. Espaço já alocado')
        pergunta2()
    else:
        if(p2 == p1):
            print('Posição inválida. Espaço já alocado')
            pergunta2()
        else:
            if(p3 == p2 or p3 == p1 or p3 == 2 or p3 ==3 or p3 == 4 or p3 == 5):
                print('Posição inválida. Espaço já alocado')
                pergunta2()
            else:
                if(p3 != 1):
                    print('GAME OVER!!')
                else:
                    print('PARABÉNS!!')
                    print('Vamos à próxima fase')


                    fase = 3
                    fasen(fase)
                    print('o GATO, o RATO e o OSSO na seguinte matriz que representa os quartos:')
                    lista1 = ['_', '*', '*', '*']
                    lista2 = ['_', 'G', '_', '*']

                    mostralistas()
                    pergunta3()

                    if ((p1 > 1 and p1 < 5) or p1 == 6 or p1 == 8):
                        print('Posição inválida. Espaço já alocado')
                        pergunta3()
                    else:
                        if(p2 == p1):
                            print('Posição inválida. Espaço já alocado')
                            pergunta3()
                        else:
                            if ((p2 > 1 and p2 < 5) or p2 == 6 or p2 == 8):
                                print('Posição inválida. Espaço já alocado')
                                pergunta3()
                            else:
                                if(p3 == p2 or p3 == p1 or (p3 > 1 and p3 < 5) or p3 == 6 or p3 == 8):
                                    print('Posição inválida. Espaço já alocado')
                                    pergunta3()
                                else:
                                    if(p2 != 1):
                                        print('GAME OVER!!')
                                    else:
                                        print('PARABÉNS!!')
                                        print('Vamos à próxima fase')

                                        fase = 4
                                        fasen(fase)
                                        print('dois QUEIJOs e o OSSO na seguinte matriz que representa os quartos:')
                                        lista1 = ['_', '_', '_', '*']
                                        lista2 = ['*', 'R', '*', '*']

                                        mostralistas()
                                        pergunta4()

                                        if(p1>3):
                                            print('Posição inválida. Espaço já alocado')
                                            pergunta4()
                                        else:
                                            if(p2 == p1 or p2 > 3):
                                                print('Posição inválida. Espaço já alocado')
                                                pergunta4()
                                            else:
                                                if(p3 == p2 or p3 == p1 or p3 > 3):
                                                    print('Posição inválida. Espaço já alocado')
                                                    pergunta4()
                                                else:
                                                    if(p3 != 2):
                                                        print('GAME OVER!!')
                                                    else:
                                                        print('PARABÉÉÉNNSSSS')
                                                        print(('VOCÊ GANHOU'))
