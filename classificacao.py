#questao 1
#Este algoritmo pede nome e idade da criança para classificar em etapa de ensino


op = 0

while(op != 1):
    #variavel nome recebe entrada do nome da criança
    nome = input('Nome da criança: ')
    #variavel idade recebe entrada do usuario convertendo para int
    idade = int(input('Idade: '))

    #testando condições e usando função format para composição
    if (idade >=1 and idade <= 5):
        print('Estudante {} tem {} anos e está no ensino infantil'.format(nome, idade))
    elif (idade >= 6 and idade <=10):
        print('Estudante {} tem {} anos e está no ensino fundamental I'.format(nome, idade))
    elif (idade >=11 and idade <=14):
        print('Estudante {} tem {} anos e está no ensino fundamental II'.format(nome, idade))
    elif (idade >= 15):
        print('Estudante {} tem {} anos e está no ensino médio'.format(nome, idade))
    else:
        print('Idade inválida')

    print('\nDeseja continuar?')
    op = int(input('0 - Sim        1 - Não \n'))
    if(op !=1 and op !=0):
        print('opção inválida é entendida como sim. Haha')
        continue
